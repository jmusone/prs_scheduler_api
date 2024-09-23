from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime
import re

#one thing to note is that getGameDates() and getGameTimes() only works for the PSL website, assuming they don't change any class names for the html
#because of this, I'm fairly confident this program won't work for sports monster
def getGameDates(url):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    gameDates = soup.find_all("td", class_ ="gameDate")
    stringGameDates = []
    for htmlDate in gameDates:
        dateMatches = re.search("<h4.*?>.*?</h4.*?>", str(htmlDate))
        stringDate = dateMatches.group()
        stringDate = re.sub("<.*?>", "", stringDate)
        stringDate = stringDate.strip()     
        stringGameDates.append(stringDate)  
    return stringGameDates

def getGameTimes(url):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    gameTimes = soup.find_all("td", class_ = "gameTime")
    stringGameTimes = []
    for htmlTime in gameTimes:
        stringTime = re.sub("<.*?>", "", str(htmlTime))
        stringTime = stringTime.strip()
        stringGameTimes.append(stringTime)
    return stringGameTimes

def getAllGameTimesAndDates(url):
    gameDates = getGameDates(url)
    gameTimes = getGameTimes(url)

    for stringDate, stringTime in zip(gameDates, gameTimes):
        combinedDateTime.append(stringDate + ": " + stringTime)
    return combinedDateTime

def getNextGameTimeAndDate(url):
    gameDates = getGameDates(url)
    currDate = datetime.today().strftime("%A, %B %d")
    for date in gameDates:
        strpDate = datetime.strptime(date, "%A, %B %d").strftime("%A, %B %d")
        if strpDate > currDate:
            print(date)
            return date
    #this is just an assumption where if no next date is found, the season will start next year. Therefore we can assume the first game is the next one
    #this assumption *doesn't* work if the url isn't updated and we're looking at a past season. 
    #I think the way around this would be somehow scraping the year from the website and comparing it to the current year from currDate
    #ALSO this does not account for cancelled games!
    print(gameDates[0])
    return gameDates[0]

getNextGameTimeAndDate()