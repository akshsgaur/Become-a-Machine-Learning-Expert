import numpy as np

# Sometimes we have data that contains values we dont want o use
# The key to filtering data is through basic relation operations, eg: ==, >
# In Numpy, we can apply basic relation operations element-wise on arrays.
arr = np.array([[0,2,3],
                [1,3,-6],
                [-3,-2,1]])

#A. Filtering Data
#~ operation represents a boolean negation, i.e, it flips each truth value in the array.

print(repr(arr == 3))
print(repr(arr>0))
print(repr(arr!= 1))
# negated from the previous step
print(repr(~(arr != 1)))

#np.nan cant be used with any relation operation. Instead, we use np.isnan to filter for the location of np.nan.
print("-----------------------------------------")
arr = np.array([[0,2,np.nan],
                [1,np.nan, -6],
                [np.nan, -2, 1]])
print(repr(np.isnan(arr)))

print("-----------------------------------------")

#B. Filtering in Numpy
#np.where function takes in a required first argument, which is a boolean
#array where Trrue represents the locations of the elemetns we want to filter.

print(repr(np.where([True, False, True])))
arr = np.array([0,3,5,3,1])
print(repr(np.where(arr==3)))
arr_2 = np.array([[0,2,3],
                 [1,0,0],
                 [-3, 0,0]])


x_ind, y_ind = np.where(arr_2 != 0)
print(repr(x_ind)) # x indices of non-zero elements
print(repr(y_ind)) # y indices of non zero elements
print(repr(arr_2[x_ind, y_ind]))

# np.where can either be 1 argument or 3 atguments. The first argument is the boolean array.
# When there are 3 arguments, the next two arguments represent the True replacement values and False replacement values,
#respectively.

print("-----------------------------------------")

np_filter = np.array([[True, False],[False, True]])
positives = np.array([[1,2],[3,4]])
negatives = np.array([[-2,-5],[-1,-8]])
print(repr(np.where(np_filter, positives, negatives)))

np_filter = positives >2
print(np_filter)
print(repr(np.where(np_filter, positives, negatives)))

print("-----------------------------------------")

#Broadcasing: If we want to use a contant replacement value, ie, -1, we could incorporate broadcasting.

np_filter = np.array([[True, False],[False, True]])
positives = np.array([[1,2],[3,4]])
print(repr(np.where(np_filter, positives, -1)))

print("-----------------------------------------")

#Axis-Wise Filtering

#If we want to filter baed on rows or columns of data, we could use the np.any and np.all functions.
#Both functions take in the same arguments, and return a single boolean or a boolean array.

arr = np.array([[-2,-1,-3],
                [4,5,-6],
                [3,9,1]])

print(repr(arr>0))
print(np.any(arr>0))
print(np.all(arr>0))

# np.all and np.any with axis argument

print("-----------------------------------------")

arr = np.array([[-2,-1,-3],
                [4,5,-6],
                [3,9,1]])
print(repr(arr>0))
print(repr(np.any(arr>0, axis=0)))
print(repr(np.any(arr>0, axis=1)))
print(repr(np.all(arr>0, axis=1)))

# We can use np.any and np.all in tandem with np.where to filter for entire rows or columns of data.
print("-----------------------------------------")

has_positives = np.any(arr>0, axis=1)
print(has_positives)
print(np.where(has_positives))
print(repr(arr[np.where(has_positives)]))

