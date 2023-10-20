import os

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

df = cudf.DataFrame(
    {
        "a": list(range(20)),
        "b": list(reversed(range(20))),
        "c": list(range(20)),
    }
)
# print(df)

ddf = dask_cudf.from_cudf(df, npartitions=2)
# print(ddf.head())

# convertendo para pandas
# pdf = pd.DataFrame({"a": [0, 1, 2, 3], "b": [0.1, 0.2, None, 0.3]})
# gdf = cudf.DataFrame.from_pandas(pdf)
# print(gdf)

# puxando por indexador
cudf_comparator = 3
c_comparator = df.query("b == @cudf_comparator")
print(c_comparator)

dask_cudf_comparator = 3
dd_comparator = ddf.query("b == @val", local_dict={"val": dask_cudf_comparator}).compute()
print(dd_comparator)