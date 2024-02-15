import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators = {'+':operator.add,
                    '-': operator.sub,
                    '*': operator.mul,
                    '/': lambda x, y: int(x/y)}

        stack = []

        for each in tokens:

            if each not in operators:
                num = int(each)
                stack.append(num)
            else:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                # 这里注意一个顺序问题，因为是后进先出，率先运算的是num2
                result = operators[each](num2,num1)
                stack.append(result)

        return stack.pop()




        