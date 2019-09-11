class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split('=')
        leftv, leftc = self.str2equ(left)
        rightv, rightc = self.str2equ(right)

        if leftv == rightv:
            if leftc == rightc:
                return 'Infinite solutions'
            else:
                return 'No solution'

        result = (rightc - leftc) // (leftv - rightv)
        return 'x={}'.format(result)

    def str2equ(self, s):
        coefficient = 0
        const = 0
        variable = 0
        sign = 1
        isVariable = False

        for idx, c in enumerate(s):
            if c in '+-':
                if not isVariable:
                    const += coefficient * sign
                else:
                    variable += coefficient * sign
                coefficient = 0
                isVariable = False
                sign = 1
                if c == '-':
                    sign *= -1
            elif c == 'x':
                isVariable = True
                if idx == 0 or s[idx - 1] in '+-':
                    coefficient = 1
            else:
                coefficient *= 10
                coefficient += int(c)

        if not isVariable:
            const += coefficient * sign
        else:
            variable += coefficient * sign

        return variable, const
