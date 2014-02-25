import numpy
import thinkplot
import thinkstats2
import random
import matplotlib
import matplotlib.pyplot as pyplot	
import math

def main():
	mean, var = 163, 52.8
	sigma = math.sqrt(var)
	pdf = thinkstats2.GaussianPdf(mean, sigma)

	xs = numpy.linspace(mean-3*sigma, mean + 3*sigma, 10)
	pmf = pdf.MakePmf(xs)
	thinkplot.Pmf(pmf, label='Gaussian')
	thinkplot.Show()

if __name__ == '__main__':
    main()