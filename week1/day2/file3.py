import os
file = 'delay.txt'
# f = open(file, 'r')
# while True:
#     line = f.readline()
#     if len(line) ==0:
#         break
#     print(line)
# f.close()

with open(file, 'r') as f:
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line)