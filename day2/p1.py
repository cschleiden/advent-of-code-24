def read_input(path):
    reports = []
    with open(path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            levels = line.split()
            reports.append(levels)
    return reports

reports = read_input('day2/input.txt')

safe_reports = 0

for report in reports:
    prev = int(-1)
    increasing = False
    safe = True
    for i in range(len(report)):
      level = int(report[i])
      if i == 1:
        if prev < level:
          increasing = True
        else:
          increasing = False
      if i >= 1:
         if (increasing and prev > level) or (increasing == False and prev < level):
            safe = False
            break

         if abs(prev - level) < 1 or abs(prev - level) > 3:
            safe = False
            break
      prev = level
    if safe:
        safe_reports += 1


print(safe_reports)