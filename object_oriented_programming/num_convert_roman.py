class Roman:
    def __init__(self, num):
        self.num = num

    def num_to_roman(self):
        d = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
        roman_str = ""
        while self.num > 0:
            def check():
                for j in d.keys():
                    if self.num >= j:
                        return j
            if self.num >= check():
                roman_str += d[check()]
                self.num -= check()
        return roman_str

roman = Roman(8590)
print(roman.num_to_roman())