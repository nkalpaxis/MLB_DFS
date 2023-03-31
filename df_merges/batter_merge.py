import pandas as pd

players = pd.read_csv("fd.csv")
players.rename(columns={"Nickname": "Name"}, inplace=True)
vsleft = pd.read_csv("vsLHP.csv")
vsright = pd.read_csv("vsRHP.csv")
barrels = pd.read_csv("barrels.csv")


vsleft["Name"] = vsleft["Name"].str.replace("'", "")
vsleft["Name"] = vsleft["Name"].str.replace(".", "")
vsright["Name"] = vsright["Name"].str.replace("'", "")
vsright["Name"] = vsright["Name"].str.replace(".", "")
barrels["Name"] = barrels["Name"].str.replace("'", "")
barrels["Name"] = barrels["Name"].str.replace(".", "")


vsleft = vsleft.reindex(columns=["Name", "PA", "ISO", "wOBA", "K%"])
vsright = vsright.reindex(columns=["Name", "PA", "ISO", "wOBA", "K%"])

splits_df = pd.merge(vsleft, vsright, how="inner", on="Name")

splits_barrel = pd.merge(splits_df, barrels, how="inner", on="Name")

df = pd.merge(players, splits_barrel, how="inner", on="Name")

df.columns = [
    "Position",
    "Name",
    "Salary",
    "Team",
    "Opp",
    "PA v L",
    "vL ISO",
    "vL wOBA",
    "vL K%",
    "PA v R",
    "vR ISO",
    "vR wOBA",
    "vR K%",
    "Barrels",
    "Barrel%",
    "HardHit",
    "HardHit%",
]

# to make things easier before an excel/google sheets dump
# the following maps format columns with percentages
df["vL K%"] = df["vL K%"].map("{:,.2%}".format)
df["vR K%"] = df["vR K%"].map("{:,.2%}".format)


# the following maps format columns with floats to 3 decimal precision
df["vL ISO"] = df["vL ISO"].map("{:.3f}".format)
df["vL wOBA"] = df["vL wOBA"].map("{:.3f}".format)
df["vR ISO"] = df["vR ISO"].map("{:.3f}".format)
df["vR wOBA"] = df["vR wOBA"].map("{:.3f}".format)

# write over original player list csv
df.to_csv("fd.csv", index=False)
