import pandas as pd
import numpy as np

# T	return the transpose, which is by definition self
s1=pd.Series([1,2,3,4,5])
s1.T
# asobject	return object Series which contains boxed values
# array([1, 2, 3, 4, 5], dtype=object)
s1.asobject


# at	Fast label-based scalar accessor
s1.at[3]

# axes	Return a list of the row axis labels
s1.axes[0]

# base	return the base object if the memory of the underlying data is


# blocks	Internal property, property synonym for as_blocks()


# data	return the data pointer of the underlying data
# dtype	return the dtype object of the underlying data
# dtypes	return the dtype object of the underlying data
# empty
# flags
# ftype	return if the data is sparse|dense
# ftypes	return if the data is sparse|dense
# hasnans
# iat	Fast integer location scalar accessor.
# iloc	Purely integer-location based indexing for selection by position.
# imag
# is_copy
# is_monotonic	Return boolean if values in the object are
# is_monotonic_decreasing	Return boolean if values in the object are
# is_monotonic_increasing	Return boolean if values in the object are
# is_unique	Return boolean if values in the object are unique
# itemsize	return the size of the dtype of the item of the underlying data
# ix	A primarily label-location based indexer, with integer position fallback.
# loc	Purely label-location based indexer for selection by label.
# name
# nbytes	return the number of bytes in the underlying data
# ndim	return the number of dimensions of the underlying data,
# real
# shape	return a tuple of the shape of the underlying data
# size	return the number of elements in the underlying data
# strides	return the strides of the underlying data
# values	Return Series as ndarray or ndarray-like
