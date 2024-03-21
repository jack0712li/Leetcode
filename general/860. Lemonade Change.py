class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        five = 0
        ten = 0

        for i in bills:
            if i == 5:
                five += 1

            if i == 10:
                if five <= 0:
                    return False
                five -= 1
                ten += 1

            if i == 20:
                if five <= 0:
                    return False
                if five <= 2 and ten <= 0:
                    return False
                if ten > 0:
                    ten -=1 
                    five -= 1
                else:
                    five -= 3

        return True