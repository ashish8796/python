import re
class Integer:

    def __init__(self, roman):
        self.roman = roman

    def roman_to_integer(self):
        d = {"CD":400, "XL":40, "IX":9, "IV":4, "XC":90, "CM":900, "M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        num = 0
        string = self.roman
        
        while len(string) > 0:
            for i in d.keys():
                if re.search("{}".format(i), string):
                    num += d[i]+ (self.roman.count(i)-1)*d[i]
                    string = string.replace(i, "")
            return num

number = Integer("DCCXXXV")
print(number.roman_to_integer())     