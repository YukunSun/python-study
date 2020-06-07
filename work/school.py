# -*- coding: utf-8 -*-
import pandas as pd

work_dir = '~/Desktop/'
data = pd.read_csv(work_dir + 'ori.csv', sep="\t")
frame = pd.DataFrame(data, columns=['c1', 'c2'])

# add column:school_num
by_province = frame.groupby(['c1', 'c2']).agg(
    school_num=pd.NamedAgg(column='c2', aggfunc='count')
)

second_level_idx_series = by_province['school_num']
# convert float to int,fill zero for NaN
df = second_level_idx_series.unstack().fillna(0).astype(int)

# order:add column:factor
# dict_sort = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5}
# arr = pd.Series()
# for week in df.iterrows():
#     no = week[1:2]
#     # df.insert(0, 'factor', dict_sort.get(no))
#     # df['factor'] = dict_sort.get(week)
#     arr.append(week, dict_sort.get(week))
# df.insert(0, 'factor', arr)
# print(df)
# print(df.sort_values())

df.to_csv(index=True, path_or_buf=work_dir + 'by_province.csv', header=True)
print('generate success:statics by province')
