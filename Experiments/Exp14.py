import numpy as np

# PART A Creating and Manipulating Arrays
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(array_1d)
print("1D Array - First Element:", array_1d[0])
print("1D Array - Slice [1:4]:", array_1d[1:4])

array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:")
print(array_2d)
print("2D Array - Element at (0, 1):", array_2d[0, 1])
print("2D Array - First Row:", array_2d[0])
print("2D Array - Second Column:", array_2d[:, 1])

reshaped_2d = array_1d.reshape((1, 5))
print("\nReshaped 1D to 2D:")
print(reshaped_2d)

array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\n3D Array:")
print(array_3d)
print("3D Array - Element at (1, 0, 1):", array_3d[1, 0, 1])
print("3D Array - First matrix:\n", array_3d[0])

reshaped_3d = array_2d.reshape((1, 2, 3))
print("\nReshaped 2D to 3D:")
print(reshaped_3d)

# PART B Array Mathematics
array1 = np.array([2, 4, 6])
array2 = np.array([1, 3, 5])
print("\nArray 1:", array1)
print("Array 2:", array2)

add = array1 + array2
subtract = array1 - array2
multiply = array1 * array2
divide = array1 / array2
print("\nElement-wise Addition:", add)
print("Element-wise Subtraction:", subtract)
print("Element-wise Multiplication:", multiply)
print("Element-wise Division:", divide)

dot_product = np.dot(array1, array2)
print("\nDot Product:", dot_product)
cross_product = np.cross(array1, array2)
print("Cross Product:", cross_product)

# PART C Statistical Operations
data = np.array([10, 15, 20, 25, 30, 35, 40])
print("\nData:", data)

mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)
variance = np.var(data)
print("\nMean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
print("Variance:", variance)

data2 = np.array([5, 10, 15, 20, 25, 30, 35])
correlation_matrix = np.corrcoef(data, data2)
print("\nCorrelation Coefficient Matrix:\n", correlation_matrix)
print("Correlation Coefficient between data and data2:", correlation_matrix[0, 1])