from typing import List

def read_input(path: str) -> List[List[int]]:
  reports = []
  with open(path, 'r') as file:
    lines = file.readlines()
    for line in lines:
      levels = line.split()
      levels = list(map(int, levels))
      reports.append(levels)
  return reports

def safe_report(report):
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
    return safe


reports = read_input('day2/input.txt')

safe_reports = 0

for report in reports:
    safe = safe_report(report)
    if safe:
        safe_reports += 1
    else:
        for i in range(len(report)):
          # new report without i
          new_report = report[:i] + report[i+1:]
          safe = safe_report(new_report)
          if safe:
            safe_reports += 1
            break


print(safe_reports)