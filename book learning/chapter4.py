import thinkplot
import thinkstats2
import random
import matplotlib
import matplotlib.pyplot as pyplot
import thinkstats2

def exercise41():
	dicti = [];
	for i in range(0,1000):
		dicti += random.expovariate(1/32.6)
	cdf = thinkstats2.MakeCdfFromList(dicti)
	thinkplot.Cdf(cdf)
	pyplot.yscale('log');
	thinkplot.Show()


def main():
	exercise41();	

if __name__ == '__main__':
    main()
