class Luhn(object):
    def __init__(self, card_num):
        try:
            self.card_num = [int(x) for x in card_num.replace(" ", "")]
        except(ValueError):
            self.card_num = []
    def is_valid(self):
        if len(self.card_num) <= 1:
            return False
        sum_digits = 0
        number = self.card_num[::-1]

        for x in range(0, len(number)):
            if x % 2 == 1:
                if number[x] * 2 < 9:
                    sum_digits += number[x] * 2
                else:
                    sum_digits += number[x] * 2 - 9
            else:
                sum_digits += number[x]

        return sum_digits % 10 == 0
