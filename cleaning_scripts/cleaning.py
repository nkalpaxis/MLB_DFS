import pandas as pd

# download player list from fanduel contest & rename it fdmlb.csv

# read in fanduel player list csv
players = pd.read_csv("fd.csv")

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
players.to_csv("fd.csv", index=False)


# read in csv files
vsleft = pd.read_csv("vsLHP.csv")
vsleft_bb = pd.read_csv("vsLHP bb.csv")
vsright = pd.read_csv("vsRHP.csv")
vsright_bb = pd.read_csv("vsRHP bb.csv")
pitcher_stats = pd.read_csv("pitcher_stats.csv")
barrels = pd.read_csv("barrels.csv")

# drop columns not being used
vsleft = vsleft.drop(
    [
        "OPS",
        "Season",
        "BB%",
        "BB/K",
        "AVG",
        "OBP",
        "SLG",
        "BABIP",
        "wRC",
        "wRAA",
        "wRC+",
        "playerId",
        "Tm",
    ],
    axis=1,
)

# remove periods and apostrophes from players names
vsleft["Name"] = vsleft["Name"].str.replace("'", "")
vsleft["Name"] = vsleft["Name"].str.replace(".", "")

# write over original csv file
vsleft.to_csv("vsLHP.csv", index=False)

# drop plate appearances in batted ball stats
# when batting stats dataframes are merged PA will be included from vsleft/vsright datasets
vsleft_bb = vsleft_bb.drop(
    [
        "Season",
        "PA",
        "Tm",
        "GB/FB",
        "GB%",
        "LD%",
        "IFFB%",
        "IFH%",
        "BUH%",
        "Pull%",
        "Cent%",
        "Oppo%",
        "Soft%",
        "Med%",
        "playerId",
    ],
    axis=1,
)

vsleft_bb["Name"] = vsleft_bb["Name"].str.replace("'", "")
vsleft_bb["Name"] = vsleft_bb["Name"].str.replace(".", "")


vsleft_bb.to_csv("vsLHP bb.csv", index=False)

vsright = vsright.drop(
    [
        "OPS",
        "Season",
        "BB%",
        "BB/K",
        "AVG",
        "OBP",
        "SLG",
        "BABIP",
        "wRC",
        "wRAA",
        "wRC+",
        "playerId",
        "Tm",
    ],
    axis=1,
)

vsright["Name"] = vsright["Name"].str.replace("'", "")
vsright["Name"] = vsright["Name"].str.replace(".", "")


vsright.to_csv("vsRHP.csv", index=False)

vsright_bb = vsright_bb.drop(
    [
        "Season",
        "PA",
        "Tm",
        "GB/FB",
        "GB%",
        "LD%",
        "IFFB%",
        "IFH%",
        "BUH%",
        "Pull%",
        "Cent%",
        "Oppo%",
        "Soft%",
        "Med%",
        "playerId",
    ],
    axis=1,
)

vsright_bb["Name"] = vsright_bb["Name"].str.replace("'", "")
vsright_bb["Name"] = vsright_bb["Name"].str.replace(".", "")


vsright_bb.to_csv("vsRHP bb.csv", index=False)

# drop columns not being used
pitcher_stats = pitcher_stats.drop(
    [
        "W",
        "L",
        "SV",
        "G",
        "GS",
        "LOB%",
        "GB%",
        "vFA (pi)",
        "WAR",
        "playerid",
        "BABIP",
        "HR/FB",
    ],
    axis=1,
)

pitcher_stats["Name"] = pitcher_stats["Name"].str.replace("'", "")
pitcher_stats["Name"] = pitcher_stats["Name"].str.replace(".", "")

pitcher_stats.to_csv("pitcher_stats.csv", index=False)

barrels = barrels.drop(
    [
        "Team",
        "PA",
        "Events",
        "EV",
        "maxEV",
        "LA",
        "AVG",
        "xBA",
        "SLG",
        "xSLG",
        "wOBA",
        "xwOBA",
        "playerid",
    ],
    axis=1,
)

barrels.to_csv("barrels.csv", index=False)