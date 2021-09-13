#!/bin/python3


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    '''
    6 4
    give me one grand today night
    give one grand today
    completely contain in magazine as in note
    :param magazine:
    :param note:
    :return:
    '''
    d = {}
    for word in magazine:
        d.setdefault(word, 0)
        d[word] += 1
        print(d)
    for word in note:
        if word in d:
            d[word] -= 1
        else:
            return False
    
    return all([x >= 0 for x in d.values()])

#from collections import Counter

#def ransom_note(magazine, rasom):
#    return (Counter(rasom) - Counter(magazine)) == {}

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

