import numpy as np
import copy as cp



# Get column from attr_name
def get_col(matr, subjects, n, attr):
    mat = cp.copy(matr)
    index = subjects.index(attr)
    col = []
    for e in range(0, n):
        col.append(mat[e][index])
    return col

# Get attr_bar 'average'
def get_bar(vect):
    return np.average(vect)

# Get bars_vect
def get_bars(data, n, m):
    bars = []
    for i in range(0, m):
        bars.append(get_bar(get_col(data['matrix'], data['subjects'], n, data['subjects'][i]) ) )
    return bars

# Get equartype
def get_equartype(vect, bar):
    v = cp.copy(vect)
    for i in range(0, len(v)):
        v[i] = np.power(v[i]-bar, 2)
    return np.average(v) 

# Get equartype
def get_equartypes(data, bars, n, m):
    v = []
    for i in range(0, m):
        v.append(
            get_equartype(
                get_col(
                    data['matrix'], 
                    data['subjects'],
                    n, 
                    data['subjects'][i]
                ), 
                bars[i] 
            ) 
        )
    return v

# get Sigmas => Sigma = sqrt(equart)
def get_sigmas(equarts):
    s = []
    for e in equarts:
        s.append(np.sqrt(e))
    return s



# Center a matrix on ist own gravity point
def matrix_centre(dat, bars, n, m):
    mat = np.transpose(cp.copy(dat['matrix']))

    for i in range(0, m):
        for j in range(0, n):
            mat[i][j] -= bars[i] 

    return np.transpose(np.array(mat))

# Reduce a matrix on low echelle
def matrix_reduce(centered, sigmas, n, m):
    mat = np.transpose(cp.copy(centered))

    for i in range(0, m):
        for j in range(0, n):
            mat[i][j] = float(mat[i][j])/float(sigmas[i]) 

    return np.transpose(np.array(mat))

