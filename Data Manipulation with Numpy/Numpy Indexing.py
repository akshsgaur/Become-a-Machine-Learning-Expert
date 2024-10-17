import numpy as np
#A. Array accessing
arr = np.array([1,2,3,4,5])

#First Element of the array
print(arr[0])

#Last element of the array
print(arr[4])

arr = np.array([[6,3],[0,2]])
#Subarray
print(repr(arr[0]))

#B.a Slicing of 1-D array
arr = np.array([1,2,3,4,5])
print(repr(arr[:]))
print(repr(arr[1:]))
print(repr(arr[2:4]))
print(repr(arr[:-1]))
print(repr(arr[-2:]))


print("#B.b Slicing of 2-D array")
#B.b Slicing of 2-D array
arr_2 = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])


print(repr(arr_2[:]))
print(repr(arr_2[1:]))
print(repr(arr_2[:,-1]))
print(repr(arr_2[:,1:]))
print(repr(arr_2[0:1,1:]))
print(repr(arr_2[0,1:]))


#Argmin and Argmax - Indexes of minimum and maximum of a list.
print("Argmin and Argmax")
arr_3 = np.array([[-2,-1,-3],
                  [4,5,-6],
                  [-3,9,1]])
print(np.argmin(arr_3[0]))
print(np.argmax(arr_3[2]))
print(np.argmin(arr_3)) #<- index of element -6 is index 5 in the flattened version of arr.

# Axis Keyword -> Argument specifies which dimension to apply the operation on.
print("argmin and argmax with axis")
print(repr(np.argmin(arr_3,axis=0)))
print(repr(np.argmin(arr_3, axis=1)))
print(repr(np.argmax(arr_3, axis=-1)))

## Test1:

data = [[[-10, 12,  13,  15,   8,   9],
 [  9,   0,  -5,   6,   1,   7],
 [ 99,   1,   7,  -9,  -3,   0],
 [ 10,  12,  -1,   0,   1,   2],
 [  0,   0,   4,   5,  17,  18]]]#

#Set elem equal to the third element of the second row in data (remember that the first row is index 0). Then return elem.
def direct_index(data):
  data = np.array(data)
  print(data)
  elem =data[1,2]
  return elem

#The first slice will contain all the rows, but will skip the first element in each row. The second slice will contain all the elements of the first three rows except the last two elements.
#Set slice1 equal to the specified first slice. Remember that NumPy uses a comma to separate slices along different dimensions.
#Set slice2 equal to the specified second slice.

def slice_data(data):
  data = np.array(data)
  slice1 = data[:,1:]
  slice2 = data[:3,0:-2]
  return slice1, slice2

#We can use np.argmin to find minimum points in the data array. First, we'll find the index of the overall minimum element.
#We can also return the indexes of each row's minimum element. This is equivalent to finding the minimum column for each row, which means our operation is done along axis 1
#Set argmin_all equal to np.argmin with data as the only argument.
#Set argmin1 equal to np.argmin with data as the first argument and the specified axis keyword argument.

def argmin_data(data):
  argmin_all = np.argmin(data)
  argmin1 = np.argmin(data, axis=1)
  return argmin_all, argmin1

#The function argmax_data, will find the index of each row's maximum element in data. Since there are only 2 dimensions in data, we can apply the operation along either axis 1 or -1.
def argmax_data(data):
  argmax_neg1 = np.argmax(data, axis=-1)
  return argmax_neg1