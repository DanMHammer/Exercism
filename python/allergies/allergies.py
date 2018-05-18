class Allergies(object):


    def __init__(self, score):
        self._lst = []
        allergy_dict = {1: "eggs", 2: "peanuts", 4: "shellfish",
                        8: "strawberries", 16: "tomatoes", 32: "chocolate",
                        64: "pollen", 128: "cats"}
        key_list = [128, 64, 32, 16, 8, 4, 2, 1]

        if score > 255:
            score = score % 256

        for item in key_list:
            if score >= item:
                self.lst.append(allergy_dict.get(item))
                score -= item
            else:
                continue

    def is_allergic_to(self, item):
        return item in self.lst

    @property
    def lst(self):
        return self._lst
