# MLB DFS Spreadsheet

![mlbdfs_datatable](https://user-images.githubusercontent.com/58003892/135893989-cd028c49-43a4-413e-8163-4fe268d2ccc1.png)

The scripts in this repository are used to build a MLB DFS spreadsheet tailored for the Fanduel website. The data used to create this sheet come from the following sources:

- Fanduel: player list csv which includes; player names, salaries, players team, & players opponent
- Numberfire: we scrape numberfire projections for the days slate but are only scraping the pitchers names, the reason is because the fanduel player list contains a lot of pitchers that are in the bullpen which can definitely help down the road to add a bullpen aspect to the sheet which I have plans for, but for the time being the numberfire list contains a lot less relief pitchers
- Fangraphs: most of the data in the sheet comes from fangraphs; lefty/righty splits, lefty/righty batted balls splits, & pitcher stats

# Collecting Fangraphs Data

To get our vs Left Handed Pitchers & vs Right Handed Pitchers splits data we'll use fangraphs splits leaderboards, the link is:

https://www.fangraphs.com/leaders/splits-leaderboards?splitArr=&splitArrPitch=&position=B&autoPt=true&splitTeams=false&statType=player&statgroup=1&startDate=2021-03-01&endDate=2021-11-01&players=&filter=&groupBy=season&sort=-1,1

Here are the following steps to set the correct filters and export the data we want;

- Click the 'Splits' tab on the leaderboards landing page
- Select the 'Handedness' tab and filter 'vsLHP'
- Select the 'Filters' tab next to the 'Splits' tab
- Set PA (plate appearances) to greater than or equal to 10
- Click the red update button to update the data table with our filter settings
- Select the 'Advanced' tab above the data table and export the data which will download to a CSV (you'll see export data on right of the table above the # of results)
- Select the 'Batted Balls' tab above the data table and export the data to a second CSV
- Follow the steps above to download the 'Advanced' & 'Batted Balls' data for 'vsRHP'

Now that we have these four csv files (2 for vsLHP and 2 for vsRHP) dump them into your code editor and rename them 'vsLHP.csv'/'vsLHP bb.csv'/'vsRHP.csv'/'vsRHP bb.csv'

Next collect the pitcher stats data from fangraphs, the link is:

https://www.fangraphs.com/leaders.aspx?pos=all&stats=pit&lg=all&qual=y&type=8&season=2021&month=0&season1=2021&ind=0

On this page simply set the 'MIN IP:' filter from 'Qualified' to 10, then export the data to a csv (export the data of the table as it is, you do not need to export the 'Advanced' or 'Batted Balls' tabs, the 'Dashboard' tab has all the data we want). Dump the csv into your code editor and rename the file 'pitcher_stats.csv'

# Quick notes on numberfire_scrape

The numberfire_scrape.py script is used to scrape all the starting pitchers for each days slate, in order to use this script you need selenium. The script has comments that describe all the lines of code. Basically you just need to set the driver variable to the path location of your geckodriver.exe, replace the email & password field strings with your fanduel login information and your all set. There is options on scraping different slates for example; Early only, Main, after hours etc .. lines 51-53 explain the options.

# Basic Workflow

After the fangraphs data is collected, the following steps will outline the basic workflow on how to set up the spreadsheet from start to finish:

- Download players list csv from Fanduel contest you wish to enter, dump csv into code editor and rename it 'fdmlb.csv'
- Run numberfire_scrape.py to get the slates pitchers
- Run fanduel_clean.py script to clean the Fanduel players list csv
- Run fangraphs_clean.py script to clean all 5 fangraph csv files
- Run batter_merge.py script
- Run pitcher_merge.py script
- Import 'fdmlb.csv' into google sheets/excel 
- Import 'pitchers.csv' into a seperate tab in the same google sheets/excel workbook


# Google Sheets / Excel Setup

After we import our fdmlb.csv file into google sheets or excel there is a few things we need to do. There were lines of code in the merging scripts that used pandas map method to map specific formats for 3 decimal percision as well as format percentages, unfortunately when we import into google sheets any float value that ends in a zero (example .270/.330) would format to .27/.33 as well as percentages not carrying over. Those lines of code that format percentage and decimal percision have been taken out, instead we can use google sheets/excel 'format as percentage' & 'decrease/increase decimal places' tools located on the tool bar menu. For any column that has a percentage (vL K%/vL FB% etc..) just select them and use the format as percentage tool, for the other two columns (ISO & wOBA) use the increase/decrease decimal places tool to format them to 3 decimal places. The colors in the image above come from the conditional formatting tool which is located in the format drop down menu. Below I will link fangraphs resources that explain these sabermetrics, the articles also have tables that show what is a good 
