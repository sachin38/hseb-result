"""
This script is written by Sachin Adhikari. This script will 
ask for symbol number and give you the result of hseb exam either
you have passed or failed

Libraries required
    BeautifulSoup and requests

"""
#!/usr/bin/env python2

from bs4 import BeautifulSoup
import sys
import requests

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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
    print bcolors.WARNING + result + bcolors.ENDC

mainFunctions()
