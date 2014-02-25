import numpy
import thinkplot
import thinkstats2
import random
import matplotlib
import matplotlib.pyplot as pyplot	
import math

def Cov(xs, ys, mux=None, muy=None):
    """Computes Cov(X, Y).

    Args:
        xs: sequence of values
        ys: sequence of values
        mux: optional float mean of xs
        muy: optional float mean of ys

    Returns:
        Cov(X, Y)
    """
    if mux is None:
        mux = thinkstats.Mean(xs)
    if muy is None:
        muy = thinkstats.Mean(ys)

    total = 0.0
    for x, y in zip(xs, ys):
        total += (x-mux) * (y-muy)

    return total / len(xs)


def main():
	listHi = [2,3,3,4,5,1,7,8,9,10]
	print Cov(listHi, listHi)


if __name__ == '__main__':
    main()