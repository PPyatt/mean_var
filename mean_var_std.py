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
from xlwings.constants import calculations


def calculate(list):
    if len(list) != 9:
         raise ValueError("List must contain nine numbers.")
    else:
        a = np.array(list)
        a = np.reshape(a, (3,3))

        # Mean
        mean1 = np.mean(a, axis=0, dtype=float).tolist()
        mean2 = np.mean(a, axis=1, dtype=float).tolist()
        meanF = np.mean(a, axis=None, dtype=float).tolist()
        output = { 'mean':[mean1, mean2, meanF]}
        # Variance
        var1 = np.var(a, axis=0).tolist()
        var2 = np.var(a, axis=1).tolist()
        varF = np.var(a, axis=None).tolist()
        output['variance']= [var1, var2, varF]
        # Standard Deviation
        std1 = np.std(a, axis=0).tolist()
        std2 = np.std(a, axis=1).tolist()
        stdF = np.std(a, axis=None).tolist()
        output['standard deviation'] = [std1, std2, stdF]
        # Max
        max1 = np.max(a, axis=0).tolist()
        max2 = np.max(a, axis=1).tolist()
        maxF = np.max(a, axis=None).tolist()
        output['max'] = [max1, max2, maxF]
        # Min
        min1 = np.min(a, axis=0).tolist()
        min2 = np.min(a, axis=1).tolist()
        minF = np.min(a, axis=None).tolist()
        output['min'] = [min1, min2, minF]
        sum1 = np.sum(a, axis=0).tolist()
        sum2 = np.sum(a, axis=1).tolist()
        sumF = np.sum(a, axis=None).tolist()
        output['sum'] = [sum1, sum2, sumF]

        calculations = output

        return calculations
