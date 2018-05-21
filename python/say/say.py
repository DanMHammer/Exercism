def say(number):
<<<<<<< HEAD
    pass
=======
    words = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
                6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
                11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
                15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
                19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
                50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
                90: 'ninety', 100: 'hundred', 1000: 'thousand'}

    places = {"millions": '', "thousands": '', "hundreds": '', "tens": '', "ones" : ''}

    if number//100 > 0:
        places.update({'hundreds': words.get(number - number % 100)})
        number = number % 100
    if number//10 > 0:
        places.update({"tens": words.get(number - number % 10)})
        number = number % 10

    places.update({"ones": words.get(number)})

    return " ".join([places.get("hundreds"), places.get("tens"), places.get("ones")])
>>>>>>> 0691b24f2618d6fbec61361e36bb04b1a603ce35
