# ЗП инженера – [70 000... 750 000]
# Результат квартального Performance Review [1...5]
# Уровень инженера – [7..17]
# Размер премии от квартальной ЗП:
# 0.05 если lvl < 10,
# 0.1 если 10 =< lvl < 13,
# 0.15 если 13 =< lvl < 15,
# 0.2 если lvl >= 15
# Модификатор премии:
# 0 – если результат perf-review < 2
# 0.25 – если результат 2 =< perf-review < 2.5
# 0.5 – если результат 2.5 =< perf-review < 3
# 1 – если результат 3 =< perf-review < 3.5
# 1.5 – если результат 3.5 =< perf-review < 4
# 2 – если результат perf-review >= 4

import pytest

from bonus import validate_salary, calculate_bonus, calculate_bonus_lvl, calculate_bonus_pr

# Equivalence Partitioning
@pytest.mark.parametrize('salary, perf_review, lvl, bonus', [
    (100000, 3, 11, 30000),
    (0, 0, 0, None)
])
def test_eq_bonus(salary, perf_review, lvl, bonus):
    assert calculate_bonus(salary, perf_review, lvl) == bonus


# invalid types
@pytest.mark.parametrize('input, expected', [
    ('a', None),
    (None, None),
    ((0, 1), None),
    ([0, 1], None),
    ({0: 1}, None),
    ((x for x in range(3)), None),
])
def test_type_invalid(input, expected):
    assert validate_salary(input) == expected
    assert calculate_bonus_pr(input) == expected
    assert calculate_bonus_lvl(input) == expected


# unexpected type float
@pytest.mark.parametrize('input, expected', [
    (2.7, None)
])
def test_type_unexpected_float(input, expected):
    assert validate_salary(input) == expected
    assert calculate_bonus_lvl(input) == expected


# Boundary Value Analysis
@pytest.mark.parametrize('salary, expected', [
    # positive
    (70000, True),
    (750000, True),
    # negative
    (69999, None),
    (750001, None),
])
def test_boundary_salary(salary, expected):
    assert validate_salary(salary) == expected


@pytest.mark.parametrize('lvl, expected', [
    # positive
    (7, 0.05),  # boundary
    (8, 0.05),
    (9, 0.05),
    (10, 0.1),  # boundary
    (11, 0.1),
    (12, 0.1),
    (13, 0.15), # boundary
    (14, 0.15),
    (15, 0.2),  # boundary
    (16, 0.2),
    (17, 0.2),  # boundary
    # negative
    (6, None),
    (18, None)
])
def test_boundary_lvl(lvl, expected):
    assert calculate_bonus_lvl(lvl) == expected


@pytest.mark.parametrize('pr, expected', [
    # positive
    (1, 0),     # boundary
    (1.1, 0),
    (1.9, 0),
    (2, 0.25),  # boundary
    (2.1, 0.25),
    (2.4, 0.25),
    (2.5, 0.5), # boundary
    (2.6, 0.5),
    (2.9, 0.5),
    (3, 1),     # boundary
    (3.1, 1),
    (3.4, 1),
    (3.5, 1.5), # boundary
    (3.6, 1.5),
    (3.9, 1.5),
    (4, 2),     # boundary
    (4.1, 2),
    (4.9, 2),
    (5, 2),     # boundary
    # negative
    (0.9, None),
    (5.1, None)
])
def test_boundary_perf_review(pr, expected):
    assert calculate_bonus_pr(pr) == expected
