# Loop Array

# Import array module
import array

# Use the array function within the array module to create an integer array
int_array = array.array('i', [1,2,3,4,5])

for element in int_array:
    print(element)