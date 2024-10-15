# prs_scheduler_api
 
This code provides a web scraper that grabs game datetimes from the [PSL](https://pittsburghsportsleague.leaguelab.com/) website. It also provides an API to add new leagues as well as get gametimes.

## API Calls:
### League API Calls:
- GET /prs_scheduler/leagues/
- POST /prs_scheduler/leagues/
 ```
 {
     "league": "<league_name>",
     "location": "<location>",
     "sport": "<sport>",
     "teamName": "<team_name>",
     "scheduleLink": "https://pittsburghsportsleague.leaguelab.com/team/<team_code>/<team_name>"
 }
 ```
- GET /prs_scheduler/leagues/<id>
- PUT /prs_scheduler/leagues/<id>
 ```
 {
     "league": "<league_name>",
     "location": "<location>",
     "sport": "<sport>",
     "teamName": "<team_name>",
     "scheduleLink": "https://pittsburghsportsleague.leaguelab.com/team/<team_code>/<team_name>"
 }
 ```
- DELETE /prs_scheduler/leagues/<id>

### Game DateTime API Calls:
- GET /prs_scheduler/schedule/
- GET /prs_scheduler/schedule/<league_id>
