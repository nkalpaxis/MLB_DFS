import pandas as pd

# read in player list, all batting splits/stats
# rename player list Nickname column to Name in order to merge on Name column
players = pd.read_csv("fdmlb.csv")
players.rename(columns={"Nickname": "Name"}, inplace=True)
vsleft = pd.read_csv("vsLHP.csv")
vsleft_bb = pd.read_csv("vsLHP bb.csv")
vsright = pd.read_csv("vsRHP.csv")
vsright_bb = pd.read_csv("vsRHP bb.csv")

# reindex vsleft/vsright columns so its Name/Plate Appearances/ISO/wOBA/K%
# reindex format makes reading the final spreadsheet easier
vsleft = vsleft.reindex(columns=["Name", "PA", "ISO", "wOBA", "K%"])
vsright = vsright.reindex(columns=["Name", "PA", "ISO", "wOBA", "K%"])

# merge vsLHP & vsLHP_bb into one dataframe for full lefty splits
# inner join on Name column
vsleft_df = pd.merge(vsleft, vsleft_bb, how="inner", on="Name")

# merge vsRHP & vsRHP_bb into one dataframe for full righty splits
vsright_df = pd.merge(vsright, vsleft_bb, how="inner", on="Name")

# merge vsleft_df with vsright_df for full splits dataframe
# inner join on Name column
splits_df = pd.merge(vsleft_df, vsright_df, how="inner", on="Name")

# merge player list with splits_df
# inner join on Name column
batter_df = pd.merge(players, splits_df, how="inner", on="Name")

# set batter dataframe index to Position
batter_df.set_index("Position")

# when merging the splits dataframes pandas will rename vsleft/vsright columns as
# PA_x PA_y / ISO_x ISO_y the following list with .columns method will rename columns to
# PA v L / PA v R etc ..
batter_df.columns = [
    "Position",
    "Name",
    "Salary",
    "Team",
    "Opp",
    "PA v L",
    "vL ISO",
    "vL wOBA",
    "vL K%",
    "vL FB%",
    "vL FB/HR%",
    "vL HC%",
    "PA v R",
    "vR ISO",
    "vR wOBA",
    "vR K%",
    "vR FB%",
    "vR FB/HR%",
    "vR HC%",
]


# write over original player list csv
batter_df.to_csv("fdmlb.csv", index=False)
