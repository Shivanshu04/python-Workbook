# in regular list we  can  not perform mathmatical operaton
a=[1,2,3]
b= [1,2,3]
c=a+b
print(c)

#in numpy array we can perform mathematical operation
import numpy as np
a=[1,2,3]
num_1 = np.array([1,2,3])
num_2 =np.array([1,2,3])
num_3 = num_1+num_2


print(num_3)

# bmi method
weight =np.array([40,60,70,80])
height =np.array([5,7,8,9])
bmi = weight/height**2
print(bmi)

# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np

import numpy as np
# Create a numpy array from baseball: np_baseball
np_baseball  =  np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))

# height_in is available as a regular list

# Import numpy
import numpy as np
height_in = [180, 215, 210, 210, 188, 176, 209, 200]
# Create a numpy array from height_in: np_height_in

np_height_in = np.array(height_in)
# Print out np_height_in

print (np_height_in)
# Convert np_height_in to m: np_height_m
# Convert np_height_in to m: np_height_m

np_height_m = np_height_in *0.0254
# Print np_height_m
print(np_height_m)

# Print np_height_m

# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Import numpy
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)
print(np_baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)