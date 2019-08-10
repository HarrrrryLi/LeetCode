class Solution:
    def basicCalculatorIV(
        self, expression: str, evalvars: List[str], evalints: List[int]
    ) -> List[str]:
        return solve(expression, evalvars, evalints)


class Term:
    """ represent a term, e.g. 8 * a * b, in this situation,
        number = 8, vars = ['a', 'b'] """

    def __init__(self, vars=[], number=1):
        self.number = number
        self.vars = vars
        pass

    def __mul__(self, ot):
        d = self.number * ot.number
        vs = self.vars + ot.vars
        vs.sort()
        return Term(vs, d)

    def __add__(self, ot):
        assert self.vars == ot.vars
        return Term(self.vars, self.number + ot.number)

    def __neg__(self):
        return Term(self.vars, -self.number)

    def __repr__(self):
        vars = [str(self.number)] + self.vars
        return "*".join(vars)


class Terms:
    """ represent many terms, e.g. 8 * a * b - 7 * b, in this situation,
        terms = [
            Term(number=8, vars=['a', 'b']),
            Term(number=-7, vars=['b']),
        ]
    """

    def __init__(self, ts=None):
        """ terms: list of Term object"""
        self.terms = ts if ts else []

    def __add__(self, ots):
        new_ts = Terms(self.terms + ots.terms)
        return new_ts.normalize()

    def __sub__(self, ots):
        return self + (-ots)

    def __mul__(self, ots):
        new_ts = Terms([t1 * t2 for t1 in self.terms for t2 in ots.terms])
        return new_ts.normalize()

    def __neg__(self):
        return Terms([-t for t in self.terms])

    def normalize(self):
        """ normalize, turn '3*a + b - a' to '2*a + b'  """
        ts = self.terms[:]
        ts.sort(key=lambda t: (-len(t.vars), t.vars))
        prev = None
        ret = []
        for i in range(0, len(ts)):
            current = ts[i]
            if prev is not None:
                if prev.vars == current.vars:
                    prev = prev + current
                else:
                    if prev.number != 0:
                        # check number, dont put '0*xx' in ret
                        ret.append(prev)
                    prev = current
            else:
                prev = current
        if prev and prev.number != 0:
            ret.append(prev)
        return Terms(ret)

    def __repr__(self):
        return str(self.terms)

    def to_str_list(self):
        return [str(t) for t in self.terms]


def get_tokens(s):
    """ get_tokens("ee + 88 - aa + 55") => ["ee", "+", 88, "-", "aa", "+", 55] """
    tokens = []
    word = ""
    value = None
    for x in s:
        if x in "()+-* ":
            if value is not None:
                tokens.append(value)
                value = None
            if word:
                tokens.append(word)
                word = ""
            if x != " ":
                tokens.append(x)
        elif word:
            word += x
        elif value is not None:
            value = value * 10 + int(x)
        elif x.isdigit():
            value = int(x)
        else:
            word = x
    if value is not None:
        tokens.append(value)
    if word:
        tokens.append(word)
    return tokens


def solve(expression, evalvars, evalints):
    intvars = {v: i for v, i in zip(evalvars, evalints)}
    tokens = get_tokens(expression)
    # make a stack, each time we call stack.pop(), we get a token, from left to right
    tokens = list(reversed(tokens))

    # operators priority
    priority = {"+": 1, "-": 1, "*": 2}

    def _solve():
        """ return a Terms object """
        # use two stacks to resolve the operators priority problem
        # list of Terms
        data = []
        # list of operators: '+' '-' '*'
        ops = []

        def handle_new_op(new_op_priority):
            while ops and priority[ops[-1]] >= new_op_priority:
                b = data.pop()
                a = data.pop()
                op = ops.pop()
                if op == "*":
                    c = a * b
                elif op == "+":
                    c = a + b
                elif op == "-":
                    c = a - b
                data.append(c)
            pass

        while tokens:
            x = tokens.pop()
            if x == "(":
                # start a subroutine for '(xx)'
                data.append(_solve())
            elif x == ")":
                # finish current routine
                break
            elif isinstance(x, int):
                # if x is 0, we get Terms([])
                data.append(Terms([Term(number=x)] if x else []))
            elif x in "+-*":
                handle_new_op(priority[x])
                ops.append(x)
            else:
                # x is a variable, e.g. 'a'
                if x in intvars:
                    x = intvars[x]
                    data.append(Terms([Term(number=x)] if x else []))
                else:
                    data.append(Terms([Term(vars=[x])]))
            pass
        handle_new_op(-1)
        assert not ops
        assert len(data) == 1
        return data[0]

    ret = _solve()
    return ret.to_str_list()
