def obtain_note_name(note):
    # 48 -> C3
    # 50 -> D3
    # 52 -> E3
    # 53 -> F3
    # 55 -> G3
    # 57 -> A3
    # 59 -> B3

    if note < 48 or note > 95:
        return

    if note <= 59:
        ret = '3'
        note -= 48
    elif note <= 71:
        ret = '4'
        note -= 60
    elif note <= 83:
        ret = '5'
        note -= 72
    else:
        ret = '6'
        note -= 84

    if note < 2:
        ret = 'C' + ret
    elif note < 4:
        ret = 'D' + ret
    elif note < 5:
        ret = 'E' + ret
    elif note < 7:
        ret = 'F' + ret
    elif note < 9:
        ret = 'G' + ret
    elif note < 11:
        ret = 'A' + ret
    else:
        ret = 'B' + ret
    return ret


KEYS = [['z', 'x', 'c', 'v', 'b', 'n', 'm'], ['a', 's', 'd', 'f', 'g', 'h', 'j'], ['q', 'w', 'e', 'r', 't', 'y', 'u']]


def obtain_key(note_name):
    i = int(note_name[1]) - int('3')
    pitch = note_name[0]
    if pitch == 'A':
        j = 5
    elif pitch == 'B':
        j = 6
    elif pitch == 'C':
        j = 0
    elif pitch == 'D':
        j = 1
    elif pitch == 'E':
        j = 2
    elif pitch == 'F':
        j = 3
    else:
        j = 4
    return KEYS[i][j]


def obtain_key_with_falling_tone(note_name):
    i = int(note_name[1]) - int('3')
    if i > 2:
        i = 2
    pitch = note_name[0]
    if pitch == 'A':
        j = 5
    elif pitch == 'B':
        j = 6
    elif pitch == 'C':
        j = 0
    elif pitch == 'D':
        j = 1
    elif pitch == 'E':
        j = 2
    elif pitch == 'F':
        j = 3
    else:
        j = 4
    return KEYS[i][j]
