# -*- coding: utf-8 -*-
"""
Created on Fri Oct 06 18:45:10 2017

@author: mmakwana
"""
from datetime import datetime
def is_valid(date):
    date = map(int, date.split("-"))
    return datetime(date[0],date[1],date[2]) >= datetime.today()