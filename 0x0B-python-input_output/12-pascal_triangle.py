#!/usr/bin/python3
"""Implement the pascal triangle function"""


def pascal_triangle(n):
    """Return a representation of the pascal triangle"""
    if n <= 0:
        return []

    triangles = [[1]]
    while (len(triangles) != n):
        j = triangles[-1]
        k = [1]
        for i in range(len(j) - 1):
            k.append(j[i] + j[i + 1])
        k.append(1)
        triangles.append(k)
    return triangles
