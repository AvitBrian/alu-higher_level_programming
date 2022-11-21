#!/usr/bin/python3
""" define a pascal's function """

def pascal_triangle(n):
    """ with size (n) represent the triangle """

    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i +1])
        tmp.append(1)
        triangle.append(tmp)
    return triangles
