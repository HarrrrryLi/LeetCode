class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        inhand = 0
        inhandCnter = collections.Counter()

        for bill in bills:
            if bill == 5:
                inhand += bill
                inhandCnter[bill] += 1
            else:
                change = bill - 5
                if change > inhand:
                    return False
                else:
                    change = bill - 5
                    while change:
                        if change == 5:
                            if 5 not in inhandCnter:
                                return False
                            else:
                                inhandCnter[5] -= 1
                                if not inhandCnter[5]:
                                    del inhandCnter[5]
                                change -= 5
                                inhand -= 5
                        else:
                            if 10 in inhandCnter:
                                inhandCnter[10] -= 1
                                if not inhandCnter[10]:
                                    del inhandCnter[10]
                                change -= 10
                                inhand -= 10
                            else:
                                if 5 not in inhandCnter:
                                    return False
                                else:
                                    inhandCnter[5] -= 1
                                    if not inhandCnter[5]:
                                        del inhandCnter[5]
                                    change -= 5
                                    inhand -= 5
                inhand += bill
                inhandCnter[bill] += 1
        return True
