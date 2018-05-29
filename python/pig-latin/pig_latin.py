def translate(text):
    words = text.lower().split()
    pig = []
    vowels  = ['a', 'e', 'i', 'o', 'u']

    for word in words:
        if word[0] in vowels or word[0:2] == 'xr' or word[0:2] == 'yt':
            pig.append(word + 'ay')
        elif word[0:2] == 'qu':
            pig.append(word[2:] + word[0:2] + 'ay')
        elif word[0] not in vowels and word[1:3] == 'qu':
            pig.append(word[3:] + word[0:3] + 'ay')
        elif word[0] not in vowels and word[1] == 'y':
            pig.append(word[1:] + word[0] + 'ay')
        elif word[0] not in vowels and word[1] not in vowels and word[2] == 'y':
            pig.append(word[2:] + word[0:2] + 'ay')
        else:
            x = 0
            for char in word:
                if char not in vowels:
                    x += 1
                else:
                    break
            pig.append(word[x:] + word[:x] + 'ay')

    return " ".join(pig)