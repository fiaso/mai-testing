## Практики тест-дизайна. Расчет квартального бонуса
Нам необходимо создать механизм расчета премии по результатам Performance Review программиста,
какие у нас есть входные данные:
1. ЗП инженера – [70 000... 750 000]
2. Результат квартального Performance Review [1...5]
3. Уровень инженера – [7..17]
4. Размер премии от квартальной ЗП:
- 5% если lvl < 10,
- 10% если 10 =< lvl < 13,
- 15% если 13 =< lvl < 15,
- 20% если lvl >= 15
5. Модификатор премии:
- 0% – если результат perf-review < 2
- 25% – если результат 2 =< perf-review < 2.5
- 50% – если результат 2.5 =< perf-review < 3
- 100% – если результат 3 =< perf-review < 3.5
- 150% – если результат 3.5 =< perf-review < 4
- 200% – если результат perf-review >= 4
Программа находится в `bonus.py`, тесты в `test.py`.

## Атрибутно-компонентный анализ. Пересечения
https://docs.google.com/spreadsheets/d/1fbiv6DRMqCMqo8DX_QbWxsPXlikqrXgq1bI_wZsQYxY/edit?usp=sharing

## Атрибутно-компонентный анализ. Сравнения и тепловая карта
https://docs.google.com/spreadsheets/d/1Ja4Njo_zNotRq715M61CLmF8GHNZ9ehxUECjLKvjqx0/edit?usp=sharing
