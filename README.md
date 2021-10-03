# MLB DFS Spreadsheet

The scripts in this repository are used to build a MLB DFS spreadsheet tailored for the Fanduel website. The data used to create this sheet come from the following sources:

- Fanduel: player list csv which includes; player names, salaries, players team, & players opponent
- Numberfire: we scrape numberfire projections for the days slate but are only scraping the pitchers names, the reason is because the fanduel player list contains a lot of pitchers that are in the bullpen which can definitely help down the road to add a bullpen aspect to the sheet but for the time being the numberfire list contains a lot less relief pitchers
- Fangraphs: most of the data in the sheet comes from fangraphs; lefty/righty splits, lefty/righty batted balls splits, & pitcher stats

# Collecting Fangraphs Data

To get our vs Left Handed Pitchers & vs Right Handed Pitchers splits data we'll use fangraphs splits leaderboards, the link is:

https://www.fangraphs.com/leaders/splits-leaderboards?splitArr=&splitArrPitch=&position=B&autoPt=true&splitTeams=false&statType=player&statgroup=1&startDate=2021-03-01&endDate=2021-11-01&players=&filter=&groupBy=season&sort=-1,1

