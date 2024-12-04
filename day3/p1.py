def extract_number(line, i):
  number = []
  while line[i].isdigit():
    number.append(line[i])
    i += 1
  return number, i

ops = []

with open('day3/input.txt', 'r') as file:
  lines = file.readlines()
  for line in lines:
    for i in range(len(line)):
      if line[i:i+4] == 'mul(':
        i += 4

        n1, i = extract_number(line, i)
        if line[i] == ',':
          i += 1
        else:
          continue
        n2, i = extract_number(line, i)
        if line[i] == ')':
          i += 1
        else:
          continue
        ops.append([n1, n2])
      else:
        i += 3

s = 0

for op in ops:
  n1 = int(''.join(op[0]))
  n2 = int(''.join(op[1]))
  print(n1 * n2)
  s += n1 * n2

print(s)