# Create a function named 'calculate' in mean_var_std.py
# that uses numpy to output the mean, columns, and elements in a 3x3 matrix.

#The input of the function should be a list containing 9 digite. The function should
# convert the list into a 3x3 numpy array, and then return a dictionary containing
#the mean, variance, standard deviation, max, min, and sum along both axes for the
#flattened matrix.

#If a list containing less than 9 elements is passed into the function, it should
# raise a ValueError exception with the message: "List must contain nine numbers.
# " The values in the returned dictionary should be lists and not Numpy arrays.



import numpy as np

def calculate(list):
    a = np.array(list)
    a = np.reshape(a, (3,3))
    print(a)
    # Mean
    mean1 = np.mean(a, axis=0)
    mean2 = np.mean(a, axis=1)
    meanF = np.mean(a, axis=None)
    output = { 'mean':[mean1, mean2, meanF]}
    # Variance
    var1 = np.var(a, axis=0)
    var2 = np.var(a, axis=1)
    varF = np.var(a, axis=None)
    output['variance']= [var1, var2, varF]
    # Standard Deviation
    std1 = np.std(a, axis=0)
    std2 = np.std(a, axis=1)
    stdF = np.std(a, axis=None)
    output['standard deviation'] = [std1, std2, stdF]
    # Max
    max1 = np.max(a, axis=0)
    max2 = np.max(a, axis=1)
    maxF = np.max(a, axis=None)
    output['max'] = [max1, max2, maxF]
    # Min
    min1 = np.min(a, axis=0)
    min2 = np.min(a, axis=1)
    minF = np.min(a, axis=None)
    output['min'] = [min1, min2, minF]
    sum1 = np.sum(a, axis=0)
    sum2 = np.sum(a, axis=1)
    sumF = np.sum(a, axis=None)
    output['sum'] = [sum1, sum2, sumF]

    calculations = output

    return calculations