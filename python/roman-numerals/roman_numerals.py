def numeral(number):
    output = ''

    if number >= 1000:
        output += 'M' * (number//1000)
        number = number % 1000
    if number >= 900:
        output += 'CM'
        number = number % 900
    if number >= 500:
        output += 'D' + ((number - 500) // 100) * 'C'
        number = number % 500
    if number >= 400:
        output += 'CD'
        number = number % 400
    if number >= 100:
        output += 'C' * (number//100)
        number = number % 100
    if number >= 90:
        output += 'XC'
        number = number % 90
    if number >= 50:
        output += 'L' + ((number - 50) // 10) * 'X'
        number = number % 10
    if number >= 40:
        output += 'XL'
        number = number % 40
    if number >= 10:
        output += 'X'*(number//10)
        number = number % 10
    if number >= 9:
        output += 'IX'
        number = number %9
    if number >= 5:
        output += 'V'
        number = number%5
    if number >= 4:
        output += 'IV'
        number = number%4
    if number >= 1:
        output += 'I' * number

    return output
