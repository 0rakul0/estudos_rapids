import os
import numpy as np
import cupy as cp
import pandas as pd
import cudf
import dask_cudf


df = cudf.DataFrame({'a':list(range(10)),
                     'b':list(reversed(range(10))),
                     'c':list(range(10))})

# print(df)

# verificando se é par ou impa

df['ag_col1'] = [1 if x % 2 == 0 else 0 for x in range(len(df))]
df['ag_col2'] = [1 if x % 3 == 0 else 0 for x in range(len(df))]

# print(df)

# estatistica
agg_1 = df.groupby(['ag_col1']).agg({'a':'max','b':'mean','c':'sum'})
print(agg_1)

agg_2 = df.groupby(['ag_col1','ag_col2']).agg({'a':'max','b':'min'})
print(agg_2)

# trabalhando com datas
date_df = cudf.DataFrame()
date_df['date'] = pd.date_range('01/31/2023', periods=72,freq='w')
date_df['value'] = np.random.sample(len(date_df))
print(date_df)