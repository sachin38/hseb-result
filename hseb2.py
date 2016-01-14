#!/usr/bin/env python2

from bs4 import BeautifulSoup
import sys
import requests

def mainFunctions():
    #taking input of symbol number
    print "Enter the symbol number:"
    number = raw_input()

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

    # returning the result 
    print result

mainFunctions()
