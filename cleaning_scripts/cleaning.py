import pandas as pd

# cleaning function to remove periods and apostrophes
def clean_names(df, col):
    df[col] = df[col].str.replace(".","")
    df[col] = df[col].str.replace("'","")
    return df

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
players = clean_names(players, 'Nickname')

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
vsleft = clean_names(vsleft, 'Name')

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

# remove periods and apostrophes from players names
vsleft_bb = clean_names(vsleft_bb, 'Name')

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

# remove periods and apostrophes from players names
vsright = clean_names(vsright, 'vsright')

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

# remove periods and apostrophes from players names
vsright_bb = clean_names(vsright_bb, 'Name')

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

# remove periods and apostrophes from players names
pitcher_stats = clean_names(pitcher_stats, 'Name')

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

# remove periods and apostrophes from players names
barrels = clean_names(barrels, 'Name')

barrels.to_csv("barrels.csv", index=False)
