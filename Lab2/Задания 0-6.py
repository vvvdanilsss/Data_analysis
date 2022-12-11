import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('penguins_size.csv')
# Выведите общую статистику по всем числовым и нечисловым столбцам с помощью метода describe().
print(df.describe())
# Узнайте размеры датасета с помощью свойство shape.
print(df.shape)
# Выведите 4 первые строки датасета.
print(df.head(4))
# Узнайте, сколько видов пингвинов представлено в таблице.
print(df.species.nunique())
# Посчитайте долю пингвинов каждого вида.
print(df.groupby('species').size() / len(df))
# Выведите количество пингвинов, обитающих на каждом из островов.
print(df.groupby('island').size())
# Найдите id пингвина с самым длинным клювом и с самым коротким. Выведите всю информацию о каждом из этих пингвинов в виде одной таблицы.
print(df.iloc[[df.culmen_length_mm.idxmax(), df.culmen_length_mm.idxmin()]])
# Посчитайте, насколько самый длинный клюв длиннее самого короткого.
print(df.culmen_length_mm.max() - df.culmen_length_mm.min())
print(df[['culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g']].corr())
# Результат покажите на тепловой карте (heatmap). Требуется построить график, а не раскрасить получившуюся в первом пункте таблицу
sns.heatmap(df[['culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g']].corr())
plt.show()
# О пингвинах какого вида в таблице больше всего недостающих данных? (Строк с NaN)
d = {x: df[df.species == x].isnull().sum().sum() for x in df.species.unique()}
print(f'{max(d, key=d.get)}: {max(d.values())}')
# Какой информации о пингвинах чаще всего не хватает?
d_inf = dict(df.isnull().sum().items())
print(f'{max(d_inf, key=d_inf.get)}: {max(d_inf.values())}')
d_dag = {x: round(abs((len(df[(df.island == x) & (df.sex == "MALE")]) - len(df[(df.island == x) & (df.sex == "FEMALE")])) * 100 / len(df[(df.island == x) & ((df.sex == "MALE") | (df.sex == "FEMALE"))])), 2) for x in df.island.unique()}
print('Равномерно') if max(d_dag.values()) <= 3 else print('Неравномерно')
# Результат покажите на столбиковой диаграмме.
plt.bar(d_dag.keys(), d_dag.values())
plt.title('Демография')
plt.xlabel('Названия островов')
plt.ylabel('Проценты разницы')
plt.show()
# Считая, что длина плавника пингвина составляет треть его роста, рассчитайте индекс массы тела каждого пингвина. Определите самый крупный вид.
d_ind = {x: round(df[df.species == x].body_mass_g.mean() / 1000 / (df[df.species == x].flipper_length_mm.mean() / 1000 * 3) ** 2, 2) for x in df.species.unique()}
big_ping = max(d_ind, key=d_ind.get)
print(f'Самый крупный вид: {big_ping} (индекс массы рассчитан по формуле: масса (кг) / рост ** 2 (м ** 2)')
# В каком количестве популяция этого вида представлена на каждом из островов? Результат покажите на круговой диаграмме.
d_count = {x: len(df[(df.island == x) & (df.species == big_ping)]) for x in df.island.unique()}
d_count_copy = dict()

for _ in d_count:
    if d_count[_] != 0:
        d_count_copy[_] = d_count[_]

plt.pie(d_count_copy.values(), labels=d_count_copy.keys())
plt.title('Количество самого крупного вида на каждом их островов')
plt.show()