class Solution(object):
    def plusOne(self, digits):
       for j in range(len(digits)):
        digits[j] = str(digits[j])
       digit_string = ''.join(digits)
       
       digit_int = int(digit_string) + 1 
       new_string = str(digit_int)
       new_number = []
       for i in range(len(new_string)):
        new_number.append(int(new_string[i]))
       return new_number
        