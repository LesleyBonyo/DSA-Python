def assignShoes(shoes):
    interval = 0
    countL = 0
    countR = 0
    for sides in shoes:
        if sides == 'R':
            countR += 1
        else:
            countL += 1
        if countL == countR:
            interval += 1
            countR = 0
            countL = 0
    return interval
