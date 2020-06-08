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
arr = []
dict_sort = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5}
for week, _ in df.iterrows():
    no = week[1:2]
    arr.append(dict_sort[no])
df.insert(loc=0, column='factor', value=arr)
df.sort_values(by='factor')
# write to csv
df.drop(columns=['factor']).to_csv(index=True, path_or_buf=work_dir + 'by_province.csv', header=True)
print('generate success:statics by province')
