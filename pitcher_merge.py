import pandas as pd

# read in pitchers list from numberfire and pitcher_stats from fangraphs
pitchers = pd.read_csv("pitchers.csv")
pitcher_stats = pd.read_csv("pitcher_stats.csv")

# merge pitchers & pitcher_stats into one dataframe
# inner join on Name column
pitcher_df = pd.merge(pitchers, pitcher_stats, how="inner", on="Name")

# write over original pitchers csv file
pitcher_df.to_csv("pitchers.csv", index=False)
