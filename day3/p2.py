ops = []

do = True

with open('day3/input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        for i in range(len(line)):
            if line[i:i+4] == 'mul(':
                i += 4
                n1 = []
                while line[i].isdigit():
                    n1.append(line[i])
                    i += 1
                if line[i] == ',':
                    i += 1
                else:
                    continue
                n2 = []
                while line[i].isdigit():
                    n2.append(line[i])
                    i += 1
                if line[i] == ')':
                    i += 1
                else:
                    continue
                if do:
                    ops.append([n1, n2])
            elif line[i:i+4] == 'do()':
                i += 4
                do = True
            elif line[i:i+7] == "don't()":
                i += 7
                do = False
            else:
                i += 3

s = 0

for ops in ops:
    n1 = int(''.join(ops[0]))
    n2 = int(''.join(ops[1]))
    print(n1 * n2)
    s += n1 * n2

print(s)