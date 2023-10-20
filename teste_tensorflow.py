import tensorflow as tf
print(tf.__version__)
print(tf.config.list_physical_devices('GPU'))

import cudf
print(cudf.__version__)

import cuml
print(cuml.__version__)

import cugraph
print(cugraph.__version__)