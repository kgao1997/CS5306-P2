#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 yqiu <yqiu@f24-suntzu>
#
# Distributed under terms of the MIT license.

"""
"""

import json
import random
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

DATAFILE = "reviews_10k.json"

def parse_reviews(filename):
    with open(DATAFILE, 'r') as fi:
        reviews = []
        for line in fi:
            try:
                reviews.append(json.loads(line))
            except:
                continue
        return reviews

"""
eventually plot the histogram using a single year's worth of reviews
- parse review objects into dicts
- plot histogram of reviews over date?

for plotting datetime objects
https://stackoverflow.com/questions/29672375/histogram-in-matplotlib-time-on-x-axis
"""
def main():
    sns.set_style('darkgrid')
    reviews = parse_reviews(DATAFILE) # :dict
    datetimes = [datetime.strptime(review['date'], "%Y-%m-%d")
                 for review in reviews]
    # just look at 2016 data
    epochs = [dt.timestamp() for dt in datetimes if dt.year == 2016]
    print(len(epochs))
    # convert the epoch format to matplotlib date format
    mpl_data = mdates.epoch2num(epochs)
    # plot it
    fig, ax = plt.subplots(1,1)
    ax.hist(mpl_data, color='lightblue')

    locator = mdates.AutoDateLocator()
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(mdates.AutoDateFormatter(locator))
    # ax.xaxis.set_major_locator(mdates.YearLocator())
    # ax.xaxis.set_major_formatter(mdates.DateFormatter('%m.%d.%y'))
    plt.show()

if __name__ == "__main__":
    main()

