# разделить на 3-4 функции

def calculate_bonus(salary, perf_review, lvl):
  if validate_salary(salary) is None:
    return None
  bonus_lvl = calculate_bonus_lvl(lvl)
  if bonus_lvl == None:
    return None
  bonus_pr = calculate_bonus_pr(perf_review)
  if bonus_pr == None:
    return None
  return 3 * salary * bonus_lvl * bonus_pr


def validate_salary(salary):
  if isinstance(salary, int) and salary in range(70000, 750001):
    return True
  else:
    return None


def calculate_bonus_lvl(lvl):
  if not isinstance(lvl, int) or lvl not in range(7, 18):
    return None
  bonus_lvl = 0.05
  mark_lvl = (10, 13, 15)
  for mark in mark_lvl:
    if lvl >= mark:
      bonus_lvl = round(bonus_lvl + 0.05, 2)
    else:
      break
  return bonus_lvl


def calculate_bonus_pr(perf_review):
  if not isinstance(perf_review, (float, int)) or not 1 <= perf_review <= 5:
    return None
  bonus_pr = 0
  size_bonus_pr = (0.25, 0.5, 1, 1.5, 2)
  mark_pr = 2
  for size_bonus in size_bonus_pr:
    if perf_review >= mark_pr:
      bonus_pr = size_bonus
      mark_pr += 0.5
    else:
      break
  return bonus_pr

