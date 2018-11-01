#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 yqiu <yqiu@f24-suntzu>
#
# Distributed under terms of the MIT license.

"""
filter reviews by year
"""

import json

def filter_reviews(infn, outfn, year):
    with open(infn, 'r') as fi:
        with open(outfn, 'w+') as fo:
            for line in fi:
                try:
                    review = json.loads(line)
                    if review['date'].startswith(year):
                        fo.write(json.dumps(review))
                        fo.write('\n')
                except:
                    continue

def main():
    filter_reviews("yelp_academic_dataset_review.json", "2016_reviews.json", "2016")

if __name__ == "__main__":
    main()
