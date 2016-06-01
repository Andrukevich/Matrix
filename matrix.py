def lst():
    """Reads out content from an external file."""
    list = []
    for i in open('Matrix.txt'):
        list.append([])
        for j in i.rstrip().split():
            list[-1].append(int(j))
    return list

def horizontals(n):
    """Calculates the maximal product of N numbers on horizontals."""
    list = lst()
    max = 0
    for i in range(len(list)):
        for j in range(len(list[i])-n+1):
            res = list[i][j]
            for k in range(1, n):
                res *= list[i][j+k]
            if max < res:
                max = res
    return max

def verticals(n):
    """Calculates the maximal product of N numbers on verticals."""
    list = lst()
    max = 0
    for i in range(len(list)-n+1):
        for j in range(len(list[i])):
            res = list[i][j]
            for k in range(1, n):
                res *= list[i+k][j]
            if max < res:
                max = res
    return max

def diagonals(n):
    """Calculates the maximal product of N numbers on diagonals."""
    list = lst()
    max = 0
    for i in range(len(list)):
        for j in range(len(list[i])):
            if i == j and len(list[i])-n-i > -1:
                res = list[i][j]
                for k in range(1, n):
                    res *= list[i+k][j+k]
                    if max < res:
                        max = res
            elif i < j and len(list[i])-n-j > -1:
                res = list[i][j]
                for k in range(1, n):
                    res *= list[i+k][j+k]
                    if max < res:
                        max =res
            elif i > j and len(list[i])-n-i > -1:
                res = list[i][j]
                for k in range(1, n):
                    res *= list[i+k][j+k]
                    if max < res:
                        max =res
    return max

def reverse_diagonals(n):
    """Calculates the maximal product of N numbers on reverse diagonals."""
    list = lst()
    max = 0
    for i in range(-1, -len(list)-1, -1):
        for j in range(-len(list[i]), 0, 1):
            if i + j == -len(list[i])-1 and len(list[i])-n+i+1 > -1:
                res = list[i][j]
                for k in range(1, n):
                    res *= list[i-k][j+k]
                    if max <res:
                        max = res
            elif i + j <  -len(list[i])-1 and len(list[i])-n+i+1 > -1:
                res = list[i][j]
                for k in range(1, n):
                    res *= list[i-k][j+k]
                    if max < res:
                        max =res
            elif i + j >  -len(list[i])-1 and j-1 < -n:
                res = list[i][j]
                for k in range(1, n):
                    res *= list[i-k][j+k]
                    if max < res:
                        max = res
    return max

def max_product(n):
    """Calculates the maximal product of N numbers horizontals or verticals or diagonals or reverse diagonals."""
    if n <= len(lst()):
        return ('Maximum product of {0} numbers is {1}'.format(n, max(horizontals(n), verticals(n), diagonals(n), reverse_diagonals(n))))
    else:
        return 'Sorry\nError product of N numbers is more than a matrix'


print (max_product(3))