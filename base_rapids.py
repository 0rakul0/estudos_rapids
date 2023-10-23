import os
import numpy as np
import cupy as cp
import pandas as pd
import cudf
import dask_cudf
#
# cp.random.seed(12)
#
# s = cudf.Series([1, 2, 3, None, 4])
# print(s)
#
# ds = dask_cudf.from_cudf(s, npartitions=2)
# print(ds.head(n=3))

# df = cudf.DataFrame(
#     {
#         "a": list(range(20)),
#         "b": list(reversed(range(20))),
#         "c": list(range(20)),
#     }
# )
# print(df)
#
# ddf = dask_cudf.from_cudf(df, npartitions=2)
# print(ddf.head())

# convertendo para pandas
# pdf = pd.DataFrame({"a": [0, 1, 2, 3], "b": [0.1, 0.2, None, 0.3]})
# gdf = cudf.DataFrame.from_pandas(pdf)
# print(gdf)

# puxando por indexador
# cudf_comparator = 3
# c_comparator = df.query("b == @cudf_comparator")
# print(c_comparator)
#
# dask_cudf_comparator = 3
# dd_comparator = ddf.query("b == @val", local_dict={"val": dask_cudf_comparator}).compute()
# print(dd_comparator)

# gerador de datas
print(""" data frame com 72 linhas e valores aleatorios""")
data_df = cudf.DataFrame()
data_df['date'] = pd.date_range('01/31/2023', periods=72,freq='w')
data_df['value'] = np.random.sample(len(data_df))
print(data_df)

print(""" procura por dias abaixo de 2023-02-20""")

date_search = cudf.to_datetime('2023-02-20')
procura = data_df.loc[data_df.date <= date_search]
print(procura)

print(""" só os dias na coluna day""")
data_df['day'] = data_df.date.dt.day
print(data_df.head(5))

print(""" só os dias na coluna mes""")
data_df['month'] = data_df.date.dt.month
print(data_df.head(5))

print(""" só os dias na coluna ano""")
data_df['year'] = data_df.date.dt.year
print(data_df.head(5))