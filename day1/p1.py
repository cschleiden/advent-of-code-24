list1 = []
list2 = []
with open('day1/input1.txt', 'r') as file:
  lines = file.readlines()
  for line in lines:
    parts = line.split()
    # Add the first part to list1, second part to list2
    list1.append(int(parts[0]))
    list2.append(int(parts[1]))

# Sort lists
list1.sort()
list2.sort()

sum = 0

# Iterate through the lists
for i in range(len(list1)):
  l1 = list1[i]
  l2 = list2[i]
  sum += abs(l1 - l2)

print(sum)