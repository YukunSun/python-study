# -*- coding: utf-8 -*-
import pandas as pd
from pandas import DataFrame


# school num
def school_statistics(frame):
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
    for week, _ in df[0:5].iterrows():
        no = week[1:2]
        arr.append(no)
    df.insert(loc=0, column='factor', value=arr)
    list_sorted = ["一", "二", "三", "四", "五"]
    df['factor'] = df['factor'].astype('category').cat.set_categories(list_sorted)
    df_sorted = df.sort_values(by=['factor'], ascending=True)
    df = df_sorted.drop(columns=['factor'])

    # calculate sum
    df.loc['total_per_province', :] = df.sum(axis=0)
    df.loc[:, 'total_per_week'] = df.sum(axis=1)

    # write to csv
    df.to_csv(index=True, path_or_buf=work_dir + 'school_num.csv', header=True)
    print('generate success:school statics')


def student_statistics(frame):
    # add column
    by_province = frame.groupby(['c1', 'c2']).agg(
        student_num=pd.NamedAgg(column='c8', aggfunc='sum')
    )
    second_level_idx_series = by_province['student_num']
    # convert float to int,fill zero for NaN
    df = second_level_idx_series.unstack().fillna(0).astype(int)

    # order:add column:factor
    arr = []
    dict_sort = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5}
    for week, _ in df[0:5].iterrows():
        no = week[1:2]
        arr.append(no)
    df.insert(loc=0, column='factor', value=arr)
    list_sorted = ["一", "二", "三", "四", "五"]
    df['factor'] = df['factor'].astype('category').cat.set_categories(list_sorted)
    df_sorted = df.sort_values(by=['factor'], ascending=True)
    df = df_sorted.drop(columns=['factor'])

    # calculate sum
    df.loc['total_per_province', :] = df.sum(axis=0)
    df.loc[:, 'total_per_week'] = df.sum(axis=1)

    # write to csv
    df.to_csv(index=True, path_or_buf=work_dir + 'student_num.csv', header=True)
    print('generate success:student statics')


if __name__ == '__main__':
    work_dir = './'
    data = pd.read_csv(work_dir + 'ori.csv', sep="\t")
    frame = DataFrame(data, columns=['c1', 'c2', 'c8'])
    school_statistics(frame)

    student_statistics(frame)
