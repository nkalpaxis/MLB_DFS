import pandas as pd

# download splits data from fangraphs
# rename vs left handed pitchers stats as vsLHP.csv
# rename vs right handed pitchers stats as vsRHP.csv

# read in both csv files - p1 short for players1
p1 = pd.read_csv("vsLHP.csv")
p2 = pd.read_csv("vsRHP.csv")

# drop columns not being used
p1 = p1.drop(
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
p1["Name"] = p1["Name"].str.replace("'", "")
p1["Name"] = p1["Name"].str.replace(".", "")

# write over original csv file
p1.to_csv("vsLHP.csv", index=False)

p2 = p2.drop(
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

p2["Name"] = p2["Name"].str.replace("'", "")
p2["Name"] = p2["Name"].str.replace(".", "")


p2.to_csv("vsRHP.csv", index=False)