#!/usr/bin/env python2

from bs4 import BeautifulSoup
import sys
import requests

def resultFetch(number):

       #url of the site
    url = "http://www.hseb.ntc.net.np/result.php/"

    #making post request with symbol number
    req = requests.post(
            url,
            data = {"symbol": number}
            )

    #putting the response to req.text
    response = req.text

    #passing it through BeautifulSoup function
    soup = BeautifulSoup(response, "lxml")

    #finding appropriate portion since the text is within div id show-result
    res_div = soup.find_all("div", id="show-result")

    # Looping through the result for looking another text
    for div in res_div:
        result = div.find("div").text

    if "Congratulation" in result:
        return True
    else:
        return False


print "Enter the starting symbol number"
symbol_start = int(raw_input())
print "Enter the ending symbol number"
symbol_end = int(raw_input())

count_passed = 0
count_failed = 0
symbol_list = range(symbol_start, symbol_end + 1)
e = symbol_start
print "The number of students in college are", len(symbol_list)

for e in symbol_list:
    if(resultFetch(e) == True):
        count_passed = count_passed + 1
    else:
        count_failed = count_failed + 1
    e = e + 1

print "The number of students passed are", count_passed
print "The number of students failed are", count_failed
