#!/usr/bin/env python2

"""Python script to fetch HSEB result from www.hseb.ntc.net.np for given symbol
number.
Libraries required:
BeautifulSoup and Requests

Code written by : Sabin Parajulee
"""

from bs4 import BeautifulSoup
import sys
import requests

def sendRequest(number):
    """Method name: sendRequest()

    Arguments:
        number [integer] - symbol number to be checked

    Returns:
        string

    Action:
        1. Makes a POST request to the url with symbol number.
        2. Fetches the status code and response.
        3. If status code is not 200, returns error message, else calls
           another method 'parseResponse()' with the response and returns the
           result from the method
    """

    url = "http://www.hseb.ntc.net.np/result.php/"
    req = requests.post(
            url,
            data = {"symbol": number}
            )

    status_code = req.status_code
    response = req.text

    if status_code == 200:
        return parseResponse(response)

    return "Something went wrong"

def parseResponse(response):
    """Method name: parseResponse()

    Arguments:
        reponse [string] - HTML content to be parsed

    Returns:
        string

    Action:
        1. Initialize BeautifulSoup object with the response we got
        2. Navigate to right section and fetch the text.
        3. Return the text
    """

    soup = BeautifulSoup(response, "lxml")

    # Finding appropriate portion. Since the response text is always within
    # "div" with id "show-result", we select it.
    res_div = soup.find_all("div", id="show-result")

    # Loop through the result looking for another "div" and extract the text
    for div in res_div:
        result = div.find("div").text

    return result

def main():
    # Check if user has entered symbol number or not. If not, show usage
    # and exit.
    if len(sys.argv) != 2:
        print "Usage: ./hseb.py symbol_no"
        print "E.g. ./hseb.py 123456890",
        print "or python hseb.py 123456890"
        print "Exiting..."
        sys.exit(1)

    # Get the symbol number
    symbol = sys.argv[1]

    # Call our sendRequest() method and print the result
    print "For symbol number: ", symbol
    print sendRequest(symbol)

if __name__ == "__main__":
    main()
