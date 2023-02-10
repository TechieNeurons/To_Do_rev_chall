from z3 import *

def chunks(n, l):
    if n == 0:
        return []
    elif n == 1:
        return [[x] for x in l]
    elif len(l) <= n:
        return [l]
    else:
        return [l[:n]] + chunks(n, l[n:])

def takeLast(n, l):
    return list(reversed(l[-n:]))

a = [-43, 61, 58, 5, -4, -11, 64, -40, -43, 61, 62, -51, 46, 15, -49, -44, 47, 4, 6, -7, 47, 7, -59, 52, 17, 11, -56, 61, -74, 52, 63, -21, 53, -17, 66, -10, -58, 0]
b = [6, 106, 10, 0, 119, 52, 51, 101, 0, 0, 15, 48, 116, 22, 10, 58, 93, 59, 106, 43, 30, 47, 93, 62, 97, 63]
c = [304, 357, 303, 320, 304, 307, 349, 305, 257, 337, 340, 309, 396, 333, 320, 380, 362, 368, 286]
d = [52, 52, 95, 95, 110, 49, 51, 51, 95, 110, 110, 53, 116, 51, 98, 63]

flag = [BitVec(f"flag_{i}", 8) for i in range(78)]

s = Solver()

s.add(flag[76] == 0)
s.add(flag[77] == 0)

# Constraints for ord(extractFlag(flag))
for i in range(76):
    s.add(And(33 <= flag[i], flag[i] <= 126))
    
# Constraints for : four = map head (chunks 5 content)
four = [flag[5 * i] for i in range(16)]
for i in range(15):
    s.add(four[i] == d[i])
    
# Constraints for : three = map (foldr (+) 0) (chunks 4 content)
three = [sum([flag[4 * i + j] for j in range(4)]) for i in range(19)]
for i in range(19):
    s.add(three[i] == c[i])
    
# Constraints for :  two     = map (foldr xor 0) (chunks 3 content)
two = [flag[i] ^ flag[i+1] ^ flag[i+2] for i in range(0,78,3)]
for i in range(25):
    s.add(two[i] == b[i])

# Constraints for : one = map (\ [l, r] -> (l - r)) (chunks 2 content)
one = [(flag[2 * i] - flag[2 * i + 1]) for i in range(38)]
for i in range(38):
    s.add(one[i] == a[i])

print (s.check())
print (s.model())
