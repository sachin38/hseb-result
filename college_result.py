#!/usr/bin/env python2

"""
Copyright 2017 Puskar Adhikari (sachin.adhikari38@gmail.com)

This program is free software: you can redistribute it and/or modify it under 
the terms of the GNU General Public License as published by the Free Software 
Foundation, either version 3 of the License, or (at your option) any later 
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY 
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A 
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with 
this program. If not, see <http://www.gnu.org/licenses/>.
"""
                         ########################
                         ###  INFORMATION     ###
#########################################################################
# This program will ask for starting and ending symbol number and       #
# find the passed and failed students in hseb examination. It will      #
# write the symbol number of passed student to passed.txt and failed    #
# to failed.txt. Result will be fetched from http://neb.ntc.net.np      #
#########################################################################

from bs4 import BeautifulSoup
import sys
import requests

def resultFetch(number):

       #url of the site
    url = "http://neb.ntc.net.np/result.php/"

    #making post request with symbol number
    req = requests.post(
            url,
            data = {"symbol": number}
            )

    #putting the response to req.text
    response = req.text

    #passing it through BeautifulSoup function
    soup = BeautifulSoup(response, "html.parser")

    #finding appropriate portion since the text is within div id show-result
    res_div = soup.find_all("div", id="show-result")

    # Looping through the result for looking another text
    for div in res_div:
        result = div.find("div").text

    if "Congratulation" in result:
        return "passed"
    else:
        return "failed"

def main():
    print "Enter the starting symbol number"
    symbol_start = int(raw_input())
    print "Enter the ending symbol number"
    symbol_end = int(raw_input())

    # Variables to store number of passed and failed students
    count_passed = 0
    count_failed = 0
    
    # This will create a list of symbol numbers
    symbol_list = range(symbol_start, symbol_end + 1)
    
    #transfering value of symbol_start in e
    e = symbol_start

    #Looping through the list of symbol numbers to gather result
    for e in symbol_list:
        if(resultFetch(e) == "passed"):
            print "\n\nSymbol number:", e
            print resultFetch(e)
            text_file = open('passed.txt', 'a')
            text_file.write(str(e))
            text_file.write("\n")
            text_file.close()
            count_passed = count_passed + 1
        else:
            print "\n\nSymbol number:", e
            print resultFetch(e)
            text_file = open('failed.txt', 'a')
            text_file.write(str(e))
            text_file.write("\n")
            text_file.close()
            count_failed = count_failed + 1
        e = e + 1

    #Printing the results 
    print "\nThe students from symbol number",symbol_start,"to symbol number",symbol_end
    print "The number of students college are", len(symbol_list)
    print "The number of students passed are", count_passed
    print "The number of students failed are", count_failed

main()
