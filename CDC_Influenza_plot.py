import csv
from pandas import Series
import matplotlib.pyplot as plt
import seaborn as sns

DATAFILE = "CDC_2016_Influenza-Like_Illness_data.csv"

def main():
	sns.set_style('darkgrid')
	series = Series.from_csv(DATAFILE, header=0)
	series.plot()
	plt.xlabel('Week of Year')
	plt.ylabel('Weighted Influenza-Like Illness Frequency (%)')
	plt.title('2016 Influenza-Like Illness Frequency')
	plt.show()

if __name__ == "__main__":
	main()
