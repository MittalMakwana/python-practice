# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 03:40:59 2017

@author: mmakwana
"""
# Converts the following format to epoch time.
# 2009-10-16T07:00:39.000Z
# Dates seem to be stored at GMT in SF.  However, they are displayed based on localtime in the SF UI.
import re
def ConvertSalesForceTime2Epoch(SFTime):
    REGEX = '(\d{4})-(\d{1,2})-(\d{1,2})T(\d{1,2}):(\d{1,2}):(\d{1,2})'
    if re.search(REGEX, SFTime):
      time = re.compile(REGEX).split(SFTime)
      
      return time