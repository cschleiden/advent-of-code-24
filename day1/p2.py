list1 = []
list2 = []
with open('day1/input.txt', 'r') as file:
  lines = file.readlines()
  for line in lines:
    parts = line.split()
    # Add the first part to list1, second part to list2
    list1.append(int(parts[0]))
    list2.append(int(parts[1]))


l2counts = {}

for l2 in list2:
  if l2 in l2counts:
    l2counts[l2] += 1
  else:
    l2counts[l2] = 1

sum = 0

# Iterate through the lists
for i in range(len(list1)):
  l1 = list1[i]
  if l1 in l2counts:
    sum += l1 * l2counts[l1]

print(sum)