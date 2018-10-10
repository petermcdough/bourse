#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 18:51:26 2018

@author: hugofayolle
"""

import quandl                              # handles api calls
import sys
import datetime

sys.path.insert(0, "/Users/hugofayolle/Desktop/Bourse/Bourse_test/")

from Model.codes import Codes
from Model.constants import API_KEY        
from Model.stock import Stock              

def main():
    quandl.ApiConfig.api_key = API_KEY # mandatory to make api calls on quandl
    if len(sys.argv) > 1:
        to_date = sys.argv[1]
    else:
        to_date = str(datetime.datetime.now().date())
    codes = Codes()
    stocks = []
    for index, row in codes.data[codes.data.INCLUDE_FOR_ANALYSIS].iterrows():
        stocks.append(Stock(index))
    for stock in stocks:
        stock.refresh(to_date = to_date, verbose = True)    
    
if __name__ == "__main__":
    main()