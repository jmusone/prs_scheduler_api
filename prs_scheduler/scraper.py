from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime
import re

#one thing to note is that getGameDates() and getGameTimes() only works for the PSL website, assuming they don't change any class names for the html
#because of this, I'm fairly confident this program won't work for sports monster
def getGameDates(soup):

    gameDates = soup.find_all("td", class_ ="gameDate")
    currYear = datetime.now().year
    stringGameDates = []
    for htmlDate in gameDates:
        dateMatches = re.search("<h4.*?>.*?</h4.*?>", str(htmlDate))
        stringDate = dateMatches.group()
        stringDate = re.sub("<.*?>", "", stringDate)
        stringDate = stringDate.strip() + " " + str(currYear)
        stringGameDates.append(stringDate)  
    return stringGameDates

def getGameTimes(soup):

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

    combinedDateTime = []
    for stringDate, stringTime in zip(gameDates, gameTimes):
        dateTimeString = stringDate + ": " + stringTime
        combinedDateTime.append(datetime.strptime(dateTimeString, "%A, %B %d %Y: %I:%M %p"))
    return combinedDateTime

def getLeagueInformation():
    leagueInfo={}

    #get team name
    teamName = re.sub("<.*?>", "", str(soup.select_one("div h1")))
    leagueInfo["teamName"] = teamName

    #parse PSL tite
    #format example: Late Fall '24 Volleyball - Thursdays at the Carnegie Library of Homestead - Recreational
    strLeagueInfo = str(soup.find_all("div", class_ ="value leagueName"))
    strLeagueInfo = re.sub("\[", "", strLeagueInfo)
    strLeagueInfo = re.sub("\]", "", strLeagueInfo)
    strLeagueInfo = re.sub("<.*?>", "", strLeagueInfo).strip().split("-")

    #get league name
    leagueInfo["league"] = strLeagueInfo[0]

    #get sport name
    sport = re.sub("^.*'[0-9][0-9]", "", strLeagueInfo[0]).strip()
    leagueInfo["sport"] = sport

    #get location
    location = re.sub("^.* at ", "", strLeagueInfo[1]).strip()
    leagueInfo["location"] = location
    return leagueInfo
