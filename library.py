#creation
# import numpy as np
# a=np.array([1,2,3,4,5])
# print(a)

#indexing
# import numpy as np
#
# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
#
# print('2nd element on 1st row: ', arr[0, 1])

#slicing
# import numpy as np
#
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
#
# print(arr[1:5])

#Data types
#
# import numpy as np
#
# arr = np.array([1, 2, 3, 4])
#
# print(arr.dtype)

#Copy vs view

# import numpy as np
#
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# arr[0] = 42
#
# print(arr)
# print(x)


#array shape
# import numpy as np
#
# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
#
# print(arr.shape)


#array reshape

# import numpy as np
#
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
#
# newarr = arr.reshape(4, 3)
#
# print(newarr)

#Array join
#
# import numpy as np
#
# arr1 = np.array([1, 2, 3])
#
# arr2 = np.array([4, 5, 6])
#
# arr = np.concatenate((arr1, arr2))
#
# print(arr)


#Array split


# import numpy as np
#
# arr = np.array([1, 2, 3, 4, 5, 6])
#
# newarr = np.array_split(arr, 3)
#
# print(newarr)


#Array search
#
# import numpy as np
#
# arr = np.array([1, 2, 3, 4, 5, 4, 4])
#
# x = np.where(arr == 4)
#
# print(x)


#Array sort
# import numpy as np
#
# arr = np.array([3, 2, 0, 1])
#
# print(np.sort(arr))


#Array filter

# import numpy as np
#
# arr = np.array([41, 42, 43, 44])
#
# x = [True, False, True, False]
#
# newarr = arr[x]
#
# print(newarr)


#pandas getting started
# import pandas
#
# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }
#
# myvar = pandas.DataFrame(mydataset)
#
# print(myvar)


#pandas series
# import pandas as pd
#
# a = [1, 7, 2]
#
# myvar = pd.Series(a)
#
# print(myvar)


#pandas dataframe
# import pandas as pd
#
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
#
# #load data into a DataFrame object:
# df = pd.DataFrame(data)
#
# print(df)


#panda csv
# import pandas as pd
#
# df = pd.read_csv('data.csv')
#
# print(df.to_string())


#panda json
# import pandas as pd
#
# df = pd.read_json('data.json')
#
# print(df.to_string())


#pandas analyzing data
# import pandas as pd
#
# df = pd.read_csv('data.csv')
#
# print(df.head(10))



























#pandas getting started
# import pandas
#
# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }
#
# myvar = pandas.DataFrame(mydataset)
#
# print(myvar)



#pandas series
# import pandas as pd
#
# a = [1, 7, 2]
#
# myvar = pd.Series(a)
#
# print(myvar)



#pandas dataframe
# import pandas as pd
#
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
#
# #load data into a DataFrame object:
# df = pd.DataFrame(data)
#
# print(df)

#pandas csv
# import pandas as pd
#
# df = pd.read_csv('data.csv')
#
# print(df.to_string())



