import pandas as pd

# download player list from fanduel contest & rename it fdmlb.csv

# read in fanduel player list csv
players = pd.read_csv("fdmlb.csv")

# drop columns not being used
players = players.drop(
    [
        "Id",
        "First Name",
        "Last Name",
        "FPPG",
        "Played",
        "Game",
        "Injury Indicator",
        "Injury Details",
        "Tier",
        "Probable Pitcher",
        "Batting Order",
        "Roster Position",
    ],
    axis=1,
)

# remove pitchers from players list
players = players[players.Position != "P"]

# remove periods and apostrophes from players names
players["Nickname"] = players["Nickname"].str.replace("'", "")
players["Nickname"] = players["Nickname"].str.replace(".", "")

# write over original csv
players.to_csv("fdmlb.csv", index=False)
