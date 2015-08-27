import random
import re
import os

A = [] * 30
D = ['.txt', '.dat', '.src']

i = 1
while i <= 30:
    a = random.randint(10, 50)
    b = str(a) + random.choice(D)
    if A.count(b) < 1:
        A.append(b)
        f = open(b, 'w')
        f.close()
        i += 1

B = [] * 30

i = 1
n = 30
while i <= 30:
    a = random.randint(10, 50)
    b = str(a) + random.choice(D)
    if B.count(b) < 1:
        if A.count(b) < 1:
            B.append(b)
            f = open(b, 'w')
            f.write('new')
            f.close()
            i += 1
        else:
            B.insert(n, b)
            l = A.index(b)
            A.remove(b)
            # A.insert(l, None)
            f = open(b, 'w')
            f.write('old')
            f.close()
            i += 1
            n -= 1

C = A + B

for i in C:
    p = re.match('^1', i)
    if p is not None:
        p = re.match('txt$', i)
        if p is not None:
            if C.count(i[0] + i[1] + ".src") < 1:
                os.rename(i, i[0] + i[1] + ".src")
            else:
                os.remove(i[0] + i[1] + ".src")
                os.rename(i, i[0] + i[1] + ".src")

OLD = [] * 30
NEW = [] * 30
EMPTY = [] * 30
List = os.listdir()
for i in List:
    j = 0
    if re.search('[0-9]', i):
            j = 1
    if j == 1:
        f = open(i)
        file = f.read()
        f.close()
        if file == "new": NEW.append(i)
        if file == "old": OLD.append(i)
        if file == "": EMPTY.append(i)
DICTIONARY = {'new': NEW,  'old': OLD,  ' ': EMPTY}
print('"old":', OLD, '\n', '"new":', NEW, '\n', '"":', EMPTY)
