import os
import time
import timeit
from io import BytesIO

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import cudf

np.random.seed(0)
num_rows = 500_000
pdf = pd.DataFrame(
    {
        "numbers": np.random.randint(-1000, 1000, num_rows, dtype="int64"),
        "business": np.random.choice(
            ["McD", "Buckees", "Walmart", "Costco"], size=num_rows
        ),
    }
)

gdf = cudf.from_pandas(pdf)

def timeit_pandas_cudf(pd_obj, gd_obj, func, **kwargs):
    """
    A utility function to measure execution time of an
    API(`func`) in pandas & cudf.

    Parameters
    ----------
    pd_obj : Pandas object
    gd_obj : cuDF object
    func : callable
    """
    pandas_time = timeit.timeit(lambda: func(pd_obj), **kwargs)
    cudf_time = timeit.timeit(lambda: func(gd_obj), **kwargs)
    return pandas_time, cudf_time

pandas_value_counts, cudf_value_counts = timeit_pandas_cudf(
    pdf, gdf, lambda df: df.value_counts(), number=30
)

pdf = pdf.head(500_000)
gdf = gdf.head(500_000)

pandas_concat = timeit.timeit(lambda: pd.concat([pdf, pdf, pdf]), number=30)
cudf_concat = timeit.timeit(lambda: cudf.concat([gdf, gdf, gdf]), number=30)

pandas_groupby, cudf_groupby = timeit_pandas_cudf(
    pdf,
    gdf,
    lambda df: df.groupby("business").agg(["min", "max", "mean"]),
    number=30,
)

num_rows = 500_000
pdf = pd.DataFrame(
    {
        "numbers": np.random.randint(-1000, 1000, num_rows, dtype="int64"),
        "business": np.random.choice(
            ["McD", "Buckees", "Walmart", "Costco"], size=num_rows
        ),
    }
)
gdf = cudf.from_pandas(pdf)

pandas_merge, cudf_merge = timeit_pandas_cudf(
    pdf, gdf, lambda df: df.merge(df), number=30
)

performance_df = pd.DataFrame(
    {
        "cudf speedup vs. pandas": [
            pandas_value_counts / cudf_value_counts,
            pandas_concat / cudf_concat,
            pandas_groupby / cudf_groupby,
            pandas_merge / cudf_merge,
        ],
    },
    index=["value_counts", "concat", "groupby", "merge"],
)

ax = performance_df.plot.bar(
    color="#7400ff",
    ylim=(1, 400),
    rot=0,
    xlabel="Operation",
    ylabel="Speedup factor",
)
ax.bar_label(ax.containers[0], fmt="%.0f")
plt.show()

# limpa memoria
# Cleaning up used memory for later benchmarks
del pdf
del gdf
import gc

_ = gc.collect()

num_rows = 900_000
pd_series = pd.Series(
    np.random.choice(
        ["123", "56.234", "Walmart", "Costco", "rapids ai"], size=num_rows
    )
)

gd_series = cudf.from_pandas(pd_series)

pandas_upper, cudf_upper = timeit_pandas_cudf(
    pd_series, gd_series, lambda s: s.str.upper(), number=20
)
pandas_contains, cudf_contains = timeit_pandas_cudf(
    pd_series, gd_series, lambda s: s.str.contains(r"[0-9][a-z]"), number=20
)
pandas_isalpha, cudf_isalpha = timeit_pandas_cudf(
    pd_series, gd_series, lambda s: s.str.isalpha(), number=20
)
performance_df = pd.DataFrame(
    {
        "cudf speedup vs. pandas": [
            pandas_upper / cudf_upper,
            pandas_contains / cudf_contains,
            pandas_isalpha / cudf_isalpha,
        ],
    },
    index=["upper", "contains", "isalpha"],
)
ax = performance_df.plot.bar(
    color="#7400ff",
    ylim=(1, 7000),
    rot=0,
    xlabel="String method",
    ylabel="Speedup factor",
)
ax.bar_label(ax.containers[0], fmt="%.0f")
plt.show()