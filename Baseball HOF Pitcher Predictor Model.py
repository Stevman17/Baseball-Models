# Import data to DataFrames
import pandas as pd
# Read in the CSV files
master_df = pd.read_csv('People.csv',usecols=['playerID','nameFirst','nameLast','bats','throws','debut','finalGame'])
batting_df = pd.read_csv('Batting.csv')
fielding_df = pd.read_csv('Fielding.csv',usecols=['playerID','yearID','stint','teamID','lgID','POS','G','GS','InnOuts','PO','A','E','DP'])
pitching_df = pd.read_csv('Pitching.csv')
awards_df = pd.read_csv('AwardsPlayers.csv', usecols=['playerID','awardID','yearID'])
allstar_df = pd.read_csv('AllstarFull.csv', usecols=['playerID','yearID'])
hof_df = pd.read_csv('HallOfFame.csv',usecols=['playerID','yearid','votedBy','needed_note','inducted','category'])
appearances_df = pd.read_csv('Appearances.csv')
post_df = pd.read_csv('PitchingPost.csv')

#Tidy Data: all of the players stats are seperated in rows for each year.
#Here, I will aggregate a player's career stats under their 'playerID'
# Initialize dictionaries for player stats and years played
player_stats = {}
years_played = {}
# Create dictionaries for player stats and years played from `pitching_df`
for i, row in pitching_df.iterrows():
    playerID = row['playerID']
    if playerID in player_stats:
        player_stats[playerID]['W'] = player_stats[playerID]['W'] + row['W']
        player_stats[playerID]['L'] = player_stats[playerID]['L'] + row['L']
        player_stats[playerID]['G'] = player_stats[playerID]['G'] + row['G']
        player_stats[playerID]['GS'] = player_stats[playerID]['GS'] + row['GS']
        player_stats[playerID]['CG'] = player_stats[playerID]['CG'] + row['CG']
        player_stats[playerID]['SHO'] = player_stats[playerID]['SHO'] + row['SHO']
        player_stats[playerID]['SV'] = player_stats[playerID]['SV'] + row['SV']
        player_stats[playerID]['IPouts'] = player_stats[playerID]['IPouts'] + row['IPouts']
        player_stats[playerID]['H'] = player_stats[playerID]['H'] + row['H']
        player_stats[playerID]['ER'] = player_stats[playerID]['ER'] + row['ER']
        player_stats[playerID]['HR'] = player_stats[playerID]['HR'] + row['HR']
        player_stats[playerID]['BB'] = player_stats[playerID]['BB'] + row['BB']
        player_stats[playerID]['SO'] = player_stats[playerID]['SO'] + row['SO']
        player_stats[playerID]['BAOpp'] = player_stats[playerID]['BAOpp'] + row['BAOpp']
        player_stats[playerID]['ERA'] = player_stats[playerID]['ERA'] + row['ERA']
        player_stats[playerID]['IBB'] = player_stats[playerID]['IBB'] + row['IBB']
        player_stats[playerID]['WP'] = player_stats[playerID]['WP'] + row['WP']
        player_stats[playerID]['HBP'] = player_stats[playerID]['HBP'] + row['HBP']
        player_stats[playerID]['BK'] = player_stats[playerID]['BK'] + row['BK']
        player_stats[playerID]['BFP'] = player_stats[playerID]['BFP'] + row['BFP']
        player_stats[playerID]['GF'] = player_stats[playerID]['GF'] + row['GF']
        player_stats[playerID]['R'] = player_stats[playerID]['R'] + row['R']
        player_stats[playerID]['SH'] = player_stats[playerID]['SH'] + row['SH']
        player_stats[playerID]['SF'] = player_stats[playerID]['SF'] + row['SF']
        player_stats[playerID]['GIDP'] = player_stats[playerID]['GIDP'] + row['GIDP']
        years_played[playerID].append(row['yearID'])
    else:
        player_stats[playerID] = {}
        player_stats[playerID]['W'] = row['W']
        player_stats[playerID]['L'] = row['L']
        player_stats[playerID]['G'] = row['G']
        player_stats[playerID]['GS'] = row['GS']
        player_stats[playerID]['CG'] = row['CG']
        player_stats[playerID]['SHO'] = row['SHO']
        player_stats[playerID]['SV'] = row['SV']
        player_stats[playerID]['IPouts'] = row['IPouts']
        player_stats[playerID]['H'] = row['H']
        player_stats[playerID]['ER'] = row['ER']
        player_stats[playerID]['HR'] = row['HR']
        player_stats[playerID]['BB'] = row['BB']
        player_stats[playerID]['SO'] = row['SO']
        player_stats[playerID]['BAOpp'] = row['BAOpp']
        player_stats[playerID]['ERA'] = row['ERA']
        player_stats[playerID]['IBB'] = row['IBB']
        player_stats[playerID]['WP'] = row['WP']
        player_stats[playerID]['HBP'] = row['HBP']
        player_stats[playerID]['BK'] = row['BK']
        player_stats[playerID]['BFP'] = row['BFP']
        player_stats[playerID]['GF'] = row['GF']
        player_stats[playerID]['R'] = row['R']
        player_stats[playerID]['SH'] = row['SH']
        player_stats[playerID]['SF'] = row['SF']
        player_stats[playerID]['GIDP'] = row['GIDP']
        years_played[playerID] = []
        years_played[playerID].append(row['yearID'])

# Iterate through `years_played` and add the number of years played to `player_stats`
for k, v in years_played.items():
    player_stats[k]['Years_Played'] = len(list(set(v)))

# Initialize `fielder_list`
fielder_list = []
# Add fielding stats to `player_stats` from `fielding_df`

for i, row in fielding_df.iterrows():
    playerID = row['playerID']
    Gf = row['G']
    GSf = row['GS']
    POf = row['PO']
    Af = row['A']
    Ef = row['E']
    DPf = row['DP']
    if playerID in player_stats and playerID in fielder_list:
        player_stats[playerID]['Gf'] = player_stats[playerID]['Gf'] + Gf
        player_stats[playerID]['GSf'] = player_stats[playerID]['GSf'] + GSf
        player_stats[playerID]['POf'] = player_stats[playerID]['POf'] + POf
        player_stats[playerID]['Af'] = player_stats[playerID]['Af'] + Af
        player_stats[playerID]['Ef'] = player_stats[playerID]['Ef'] + Ef
        player_stats[playerID]['DPf'] = player_stats[playerID]['DPf'] + DPf
    #Change the else statement from Pt 2 to an elif to avoid ValueError's for hitters that never pitched, which
    #is common
    elif playerID in player_stats:
        fielder_list.append(playerID)
        player_stats[playerID]['Gf'] = Gf
        player_stats[playerID]['GSf'] = GSf
        player_stats[playerID]['POf'] = POf
        player_stats[playerID]['Af'] = Af
        player_stats[playerID]['Ef'] = Ef
        player_stats[playerID]['DPf'] = DPf

# Initialize `allstar_list`
allstar_list = []
# Add a count for each Allstar game appearance for each player in `player_stats`
for i, row in allstar_df.iterrows():
    playerID = row['playerID']
    if playerID in player_stats and playerID in allstar_list:
        player_stats[playerID]['AS_games'] += 1
    elif playerID in player_stats:
        allstar_list.append(playerID)
        player_stats[playerID]['AS_games'] = 1


#Aggregate awards data, choosing only the pitcher awards
#print(awards_df['awardID'].unique())
# Create DataFrames for each award
ptc = awards_df[awards_df['awardID'] == 'Pitching Triple Crown']
mvp = awards_df[awards_df['awardID'] == 'Most Valuable Player']
gg = awards_df[awards_df['awardID'] == 'Gold Glove']
roy = awards_df[awards_df['awardID'] == 'Rookie of the Year']
cy = awards_df[awards_df['awardID'] == 'Cy Young Award']
as_mvp = awards_df[awards_df['awardID'] == 'All-Star Game MVP']
rr = awards_df[awards_df['awardID'] == 'Rolaids Relief Man Award']
nlcs_mvp = awards_df[awards_df['awardID'] == 'NLCS MVP']
alcs_mvp = awards_df[awards_df['awardID'] == 'ALCS MVP']
ry = awards_df[awards_df['awardID'] == 'Reliever of the Year Award']
ws_mvp = awards_df[awards_df['awardID'] == 'World Series MVP']
# Include each DataFrame in `awards_list`
awards_list = [ptc, mvp, gg, roy, cy, as_mvp, rr, nlcs_mvp, alcs_mvp, ry, ws_mvp]
# Initialize lists for each of the above DataFrames
ptc_list = []
mvp_list = []
gg_list = []
roy_list = []
cy_list = []
as_mvp_list = []
rr_list = []
nlcs_mvp_list = []
alcs_mvp_list = []
ry_list = []
ws_mvp_list = []
# Include each of the above lists in `lists`
lists = [ptc_list, mvp_list, gg_list, roy_list, cy_list, as_mvp_list, rr_list, nlcs_mvp_list, alcs_mvp_list, ry_list, ws_mvp_list]
# Add a count for each award for each player in `player_stats`
for index, v in enumerate(awards_list):
    for i, row in v.iterrows():
        playerID = row['playerID']
        award = row['awardID']
        if playerID in player_stats and playerID in lists[index]:
            player_stats[playerID][award] += 1
        elif playerID in player_stats:
            lists[index].append(playerID)
            player_stats[playerID][award] = 1

#Add some playoff stats, since Hall of Fame voters might implicitly weight playoff performance more heavily.
#Initialize `playoff_list`
playoff_list = []
# Add playoff stats to `player_stats` from `post_df`
for i, row in post_df.iterrows():
    playerID = row['playerID']
    Pg = row['G']
    Pw = row['W']
    Pgs = row['GS']
    Psho = row['SHO']
    Psv = row['SV']
    Pipouts = row['IPouts']
    Pso = row['SO']
    Pera = row['ERA']
    if playerID in player_stats and playerID in playoff_list:
        player_stats[playerID]['Pg'] = player_stats[playerID]['Pg'] + Pg
        player_stats[playerID]['Pw'] = player_stats[playerID]['Pw'] + Pw
        player_stats[playerID]['Pgs'] = player_stats[playerID]['Pgs'] + Pgs
        player_stats[playerID]['Psho'] = player_stats[playerID]['Psho'] + Psho
        player_stats[playerID]['Psv'] = player_stats[playerID]['Psv'] + Psv
        player_stats[playerID]['Pso'] = player_stats[playerID]['Pso'] + Pso
        player_stats[playerID]['Pera'] = player_stats[playerID]['Pera'] + Pera
    elif playerID in player_stats:
        playoff_list.append(playerID)
        player_stats[playerID]['Pg'] = Pg
        player_stats[playerID]['Pw'] = Pw
        player_stats[playerID]['Pgs'] = Pgs
        player_stats[playerID]['Psho'] = Psho
        player_stats[playerID]['Psv'] = Psv
        player_stats[playerID]['Pso'] = Pso
        player_stats[playerID]['Pera'] = Pera


#HOF
#filter hof_df first to include only players who were inducted into the Hall of Fame.
# Then iterate through hof_df indicating which players in player_stats have been inducted into the
#  Hall of Fame as well as how they were inducted:
# filter `hof_df` to include only instances where a player was inducted into the Hall of Fame
hof_df = hof_df[(hof_df['inducted'] == 'Y') & (hof_df['category'] == 'Player')]
# Indicate which players in `player_stats` were inducted into the Hall of Fame
for i, row in hof_df.iterrows():
    playerID = row['playerID']
    if playerID in player_stats:
        player_stats[playerID]['HoF'] = 1
        player_stats[playerID]['votedBy'] = row['votedBy']
#print(hof_df.head())

#I've now compiled data from batting_df, fielding_df, awards_df, allstar_df, and hof_df into the player_stats
# dictionary.
#So, now is a good time to convert the player_stats dictionary into a DataFrame.
#Use the pandas from_dict() method to convert the dictionary to a DataFrame called stats_df:
# Convert `player_stats` into a DataFrame
stats_df = pd.DataFrame.from_dict(player_stats, orient='index')
#stats_df.to_csv('new-csv-file-stats.csv')
#print(list(stats_df))

#Add a column to stats_df called playerID derived from the index.
# Then join stats_df with master_df using an inner join.
#Remember that an inner join selects all rows from both tables as long as there is a match between the columns.
# In this case, you use an inner join because you want to match the information of stats_df with the master_df data:
# you want to keep on working with the rows that are common to both DataFrames.
# Add a column for playerID from the `stats_df` index
stats_df['playerID'] = stats_df.index
# Join `stats_df` and `master_df`
master_df = master_df.join(stats_df,on='playerID',how='inner', rsuffix='mstr')
# Inspect first rows of `master_df`
#print(master_df.loc[master_df['nameLast'] == 'Martinez'])
#print(appearances_df.head())

#as MLB progressed, different eras emerged where the amount of runs per game increased or decreased significantly.
# This means that when a player played has a large influence on that player’s career statistics.
# The Hall of Fame (HoF) voters take this into account when voting players in, so your model needs that information too.
# Initialize a dictionary
pos_dict = {}
# Iterate through `appearances_df`
# Add a count for the number of appearances for each player at each position
# Also add a count for the number of games played for each player in each era.
for i, row in appearances_df.iterrows():
    ID = row['playerID']
    year = row['yearID']
    if ID in pos_dict:
        pos_dict[ID]['G_all'] = pos_dict[ID]['G_all'] + row['G_all']
        pos_dict[ID]['G_p'] = pos_dict[ID]['G_p'] + row['G_p']
        pos_dict[ID]['G_c'] = pos_dict[ID]['G_c'] + row['G_c']
        pos_dict[ID]['G_1b'] = pos_dict[ID]['G_1b'] + row['G_1b']
        pos_dict[ID]['G_2b'] = pos_dict[ID]['G_2b'] + row['G_2b']
        pos_dict[ID]['G_3b'] = pos_dict[ID]['G_3b'] + row['G_3b']
        pos_dict[ID]['G_ss'] = pos_dict[ID]['G_ss'] + row['G_ss']
        pos_dict[ID]['G_lf'] = pos_dict[ID]['G_lf'] + row['G_lf']
        pos_dict[ID]['G_cf'] = pos_dict[ID]['G_cf'] + row['G_cf']
        pos_dict[ID]['G_rf'] = pos_dict[ID]['G_rf'] + row['G_rf']
        pos_dict[ID]['G_of'] = pos_dict[ID]['G_of'] + row['G_of']
        pos_dict[ID]['G_dh'] = pos_dict[ID]['G_dh'] + row['G_dh']
        if year < 1920:
            pos_dict[ID]['pre1920'] = pos_dict[ID]['pre1920'] + row['G_all']
        elif year >= 1920 and year <= 1941:
            pos_dict[ID]['1920-41'] = pos_dict[ID]['1920-41'] + row['G_all']
        elif year >= 1942 and year <= 1945:
            pos_dict[ID]['1942-45'] = pos_dict[ID]['1942-45'] + row['G_all']
        elif year >= 1946 and year <= 1962:
            pos_dict[ID]['1946-62'] = pos_dict[ID]['1946-62'] + row['G_all']
        elif year >= 1963 and year <= 1976:
            pos_dict[ID]['1963-76'] = pos_dict[ID]['1963-76'] + row['G_all']
        elif year >= 1977 and year <= 1992:
            pos_dict[ID]['1977-92'] = pos_dict[ID]['1977-92'] + row['G_all']
        elif year >= 1993 and year <= 2009:
            pos_dict[ID]['1993-2009'] = pos_dict[ID]['1993-2009'] + row['G_all']
        elif year > 2009:
            pos_dict[ID]['post2009'] = pos_dict[ID]['post2009'] + row['G_all']
    else:
        pos_dict[ID] = {}
        pos_dict[ID]['G_all'] = row['G_all']
        pos_dict[ID]['G_p'] = row['G_p']
        pos_dict[ID]['G_c'] = row['G_c']
        pos_dict[ID]['G_1b'] = row['G_1b']
        pos_dict[ID]['G_2b'] = row['G_2b']
        pos_dict[ID]['G_3b'] = row['G_3b']
        pos_dict[ID]['G_ss'] = row['G_ss']
        pos_dict[ID]['G_lf'] = row['G_lf']
        pos_dict[ID]['G_cf'] = row['G_cf']
        pos_dict[ID]['G_rf'] = row['G_rf']
        pos_dict[ID]['G_of'] = row['G_of']
        pos_dict[ID]['G_dh'] = row['G_dh']
        pos_dict[ID]['pre1920'] = 0
        pos_dict[ID]['1920-41'] = 0
        pos_dict[ID]['1942-45'] = 0
        pos_dict[ID]['1946-62'] = 0
        pos_dict[ID]['1963-76'] = 0
        pos_dict[ID]['1977-92'] = 0
        pos_dict[ID]['1993-2009'] = 0
        pos_dict[ID]['post2009'] = 0
        if year < 1920:
            pos_dict[ID]['pre1920'] = row['G_all']
        elif year >= 1920 and year <= 1941:
            pos_dict[ID]['1920-41'] = row['G_all']
        elif year >= 1942 and year <= 1945:
            pos_dict[ID]['1942-45'] = row['G_all']
        elif year >= 1946 and year <= 1962:
            pos_dict[ID]['1946-62'] = row['G_all']
        elif year >= 1963 and year <= 1976:
            pos_dict[ID]['1963-76'] = row['G_all']
        elif year >= 1977 and year <= 1992:
            pos_dict[ID]['1977-92'] = row['G_all']
        elif year >= 1993 and year <= 2009:
            pos_dict[ID]['1993-2009'] = row['G_all']
        elif year > 2009:
            pos_dict[ID]['post2009'] = row['G_all']

# Convert the `pos_dict` to a DataFrame
pos_df = pd.DataFrame.from_dict(pos_dict, orient='index')
#Next you want to determine the percentage of times each player played
# at each position and within each era.
#First, create a list called pos_col_list from the columns of pos_df and
# remove the string ‘G_all’. Then create new columns in pos_df for the percentage
# each player played at each position and within each era by looping through
# pos_col_list and dividing the games played at each position or era by the
# total games played by that player. Finally, print out the first few rows of
# pos_df:
# Create a list from the columns of `pos_df`
pos_col_list = pos_df.columns.tolist()
# Remove the string 'G_all'
pos_col_list.remove('G_all')
# Loop through the list and divide each column by the players total games played
for col in pos_col_list:
    column = col + '_percent'
    pos_df[column] = pos_df[col] / pos_df['G_all']
# Print out the first rows of `pos_df`
#print(pos_df.head())
#Since we are focused on pitchers, filter out players who have played more than 10%
#of their games as a position player
# Filter `pos_df` to eliminate players who played 10% or more of their games as Fielders or Catchers
pos_df = pos_df[(pos_df['G_p_percent'] > 0.1)]
# Get info on `pos_df`
#print(pos_df.info())
# Join `pos_df` and `master_df`
master_df = master_df.join(pos_df,on='playerID',how='right')
# Print out the first rows of `master_df`
#print(master_df.head())

#Now filter master_df to only include players who were voted into the Hall of Fame
#  or didn’t make it at all.
#Some players make it into the Hall by selection from the Veterans Committee,
# or by a specially appointed committee. These players are typically selected for
# reasons other than purely their statistics which your model may find difficult
#  to quantify, so it’s best to leave them out of the data set.
# Replace NA values with `None`
master_df['votedBy'] = master_df['votedBy'].fillna('None')
# Filter `master_df` to include only players who were voted into the Hall of Fame or Players who did not make it at all
master_df = master_df[(master_df['votedBy'] == 'None') | (master_df['votedBy'] == 'BBWAA') | (master_df['votedBy'] == 'Run Off')]
# Inspect `master_df`
#master_df.info()

#The bats and throws columns need to be converted to numeric: you can easily do
#  this by creating a function to convert each R to a 1 and each L to a 0.
# Use the apply() method to create numeric columns called bats_R and throws_R:
# Create a function to convert the bats and throws colums to numeric
def bats_throws(col):
    if col == "R":
        return 1
    else:
        return 0
# Use the `apply()` method to create numeric columns from the bats and throws columns
master_df['bats_R'] = master_df['bats'].apply(bats_throws)
master_df['throws_R'] = master_df['throws'].apply(bats_throws)
# Print out the first rows of `master_df`
#print(master_df.head())

#The debut and finalGame columns are currently strings. You’ll need to parse out
#  the years from these columns. First, import datetime. Next, convert the debut
#  and finalGame columns to a datetime object using pd.to_datetime(). Then parse
# out the year using dt.strftime(‘%Y’) and convert to numeric with pd.to_numeric().
# Import datetime
from datetime import datetime
# Convert the `debut` column to datetime
master_df['debut'] =  pd.to_datetime(master_df['debut'])
# Convert the `finalGame` column to datetime
master_df['finalGame'] = pd.to_datetime(master_df['finalGame'])
# Create new columns for debutYear and finalYear
master_df['debutYear'] = pd.to_numeric(master_df['debut'].dt.strftime('%Y'), errors='coerce')
master_df['finalYear'] = pd.to_numeric(master_df['finalGame'].dt.strftime('%Y'), errors='coerce')
# Return the first rows of `master_df`
#print(master_df.head())
#print(list(master_df))

# Eliminating unnecessary columns
df = master_df.drop(['votedBy', 'IBB', 'bats', 'throws', 'GSf', 'POf','Gf', 'playerIDmstr', 'bats_R', 'throws_R'], axis=1)
# Print `df` columns
#print(df.columns)
# Print a list of null values
#print(df.isnull().sum(axis=0).tolist())

# Fill null values in numeric columns with 0
fill_cols = ['BAOpp', 'SH', 'SF', 'GIDP', 'Pitching Triple Crown', 'Cy Young Award','All-Star Game MVP','Rolaids Relief Man Award', 'NLCS MVP', 'ALCS MVP', 'Reliever of the Year Award', 'AS_games', 'Rookie of the Year', 'Gold Glove', 'Most Valuable Player', 'HoF', '1977-92', 'pre1920', '1942-45', '1946-62', '1963-76', '1920-41', '1993-2009', 'World Series MVP', 'G_dh_percent', 'G_dh', 'Af', 'DPf', 'Ef', 'Pg', 'Pw', 'Pgs', 'Psho', 'Psv', 'Pso', 'Pera']
for col in fill_cols:
    df[col] = df[col].fillna(0)
# Drop any additional rows with null. Also, replace infinite values with Nan, and drop them too.
import numpy as np
df = df.replace([np.inf, -np.inf], np.nan).dropna()
df.isnull().any()
# Check to make sure null values have been removed
#print(df.isnull().sum(axis=0).tolist())

#Feature Engineering: Creating New Features
#print(df.columns)
#Let's add WHIP!
#WHIP is a usefull statistic to judge pitchers. Add up all of the hits and walks
#the pitcher has allowed, and divide that number by the number of innings pitched!
# Create WHIP (`WHIP`) column
df['WHIP'] = (df['BB'] + df['H']) / (df['IPouts']/3)
#  Create Strikeout's (SO) per 9 innings column
df['SO/9'] = (df['SO']*9) / (df['IPouts']/3)
#Creat Strikeout's per BB column
#where a pitcher has zero walks, we need to avoid dividing by 0
#using "np.where" we can  make the value in the 'SO/BB' column a zero when walks are 0.
df['SO/BB'] = np.where(df['BB']>0, (df['SO'])/(df['BB']), 0)
# Double check the `df` columns
#print(df.columns)
#df.to_csv('new-csv-file.csv')


#Filter df to only include Hall of Fame players and print the length.
# Filter the `df` for the remaining Hall of Fame members in the data
df_hof = df[df['HoF'] == 1]
# Print the length of the new DataFrame
#print(len(df_hof))

#Visualize the Data
#You have 36 Hall of Fame pitvchers left in the data set. Plot out distributions for Strikeouts, ERA, Total Outs,
#and the WHIP data column we created.
# Import the `pyplot` module from `matplotlib`
# import matplotlib.pyplot as plt
# # Initialize the figure and add subplots
# fig = plt.figure(figsize=(15, 12))
# ax1 = fig.add_subplot(2,2,1)
# ax2 = fig.add_subplot(2,2,2)
# ax3 = fig.add_subplot(2,2,3)
# ax4 = fig.add_subplot(2,2,4)
# # Create distribution plots for Strikeouts, ERA, Outs,
# ax1.hist(df_hof['SO'])
# ax1.set_title('Distribution of Strikeouts')
# ax1.set_ylabel('HoF Careers')
# ax2.hist(df_hof['ERA'])
# ax2.set_title('Distribution of ERA')
# ax3.hist(df_hof['IPouts'])
# ax3.set_title('Distribution of Total Outs')
# ax3.set_ylabel('HoF Careers')
# ax4.hist(df_hof['AS_games'])
# ax4.set_title('Distribution of All Star Game Appearances')
# #Make a Scatterplot
# #Filter `df` for players with 10 or more years of experience
# df_10 = df[(df['Years_Played'] >= 10) & (df['HoF'] == 0)]
# # Initialize the figure and add subplots
# fig = plt.figure(figsize=(14, 7))
# ax1 = fig.add_subplot(1,2,1)
# ax2 = fig.add_subplot(1,2,2)
# # Create Scatter plots for SO vs. ERA and WHIP vs. Total Outs
# # Use an aplha of .5 on the non hall-of-famers to make the less numerous hall of famers more visible.
# ax1.scatter(df_hof['SO'], df_hof['BFP'], c='r', label='HoF Player')
# ax1.scatter(df_10['SO'], df_10['BFP'], c='b', label='Non HoF Player', alpha=0.5)
# ax1.set_title('Career SO vs. Career Batters Faced')
# ax1.set_xlabel('Career SO')
# ax1.set_ylabel('Career ERA')
# ax2.scatter(df_hof['WHIP'], df_hof['IPouts'], c='r', label='HoF Player')
# ax2.scatter(df_10['WHIP'], df_10['IPouts'], c='b', label='Non HoF Player', alpha=0.5)
# ax2.set_title('Career WHIP vs. Career IPouts')
# ax2.set_xlabel('Career WHIP')
# ax2.legend(loc='lower right', scatterpoints=1)
# # Show the plot
# plt.show()
#Check for null values
#print(df.isnull().sum(axis=0).tolist())

#Make sure to separate out the pitchers who played their most recent
# season in the last 15 years so you can use this as “new” data once you
#  have a model that’s trained and tested.
#Add a column to df for years since last season (YSLS) by subtracting
# the finalYear column from 2017. Next, create a new DataFrame called
#  df_pitchers by filtering df for pitchers whose last season was more
# than 15 years ago and create one called df_eligible for players whose
#  last season was 15 or less years ago.
# Create column for years since retirement
df['YSLS'] = 2017 - df['finalYear']
# Filter `df` for players who retired more than 15 years ago
df_pitchers = df[df['YSLS'] > 15]
#print(df_pitchers.head())
# Filter `df` for players who retired less than 15 years ago and for currently active players
df_eligible = df[df['YSLS']<= 15]
#print(df_eligible.head())

#Now you need to select the columns to include in the model. First, print out the columns.
#print(df.columns)
# Select columns to use for models, and identification columns
num_cols_pitchers = ['playerID', 'nameFirst', 'nameLast','W', 'L',
       'G', 'GS', 'CG', 'SHO', 'SV', 'IPouts', 'H', 'ER', 'HR', 'BB', 'SO',
       'BAOpp', 'ERA', 'WP', 'HBP', 'BK', 'BFP', 'GF', 'R', 'SH', 'SF', 'GIDP',
       'Years_Played','Pitching Triple Crown', 'HoF',
       'Most Valuable Player', 'AS_games', 'Cy Young Award',
       'Rookie of the Year', 'Gold Glove', 'World Series MVP',
       'All-Star Game MVP', 'Rolaids Relief Man Award', 'NLCS MVP', 'ALCS MVP',
       'Reliever of the Year Award', 'G_all', 'G_p', 'pre1920',
       '1920-41', '1942-45', '1946-62', '1963-76', '1977-92', '1993-2009',
       'post2009', 'G_p_percent', 'pre1920_percent', '1920-41_percent', '1942-45_percent',
       '1946-62_percent', '1963-76_percent', '1977-92_percent',
       '1993-2009_percent', 'post2009_percent',
       'WHIP', 'SO/9', 'YSLS', 'SO/BB', 'Pg', 'Pw', 'Pgs', 'Psho', 'Psv', 'Pso', 'Pera']
#'Pg', 'Pw', 'Pgs', 'Psho', 'Psv', 'Pso', 'Pera'
# Create a new DataFrame (`data`) from the `df_hitters` using the columns above
data = df_pitchers[num_cols_pitchers]
# Return the first rows of `data`
#print(data.head())
#Print out how many rows are in data and how many of those rows are Hall of Famers.
#Print length of `data`
print(len(data))
# Print how many Hall of Fame members are in data
print(len(data[data['HoF'] == 1]))
#Inspect this data in a .CSV that will be saved to the directory of your file.
#data.to_csv('new-csv-file-data.csv')
#df.to_csv('new-csv-file-df.csv')
#There are 5922 rows and 36 of those are Hall of Famers for your model to identify.
# Create your target Series from the HoF column of data and your features DataFrame
#  by dropping the identification columns and the target column with the help of drop().
# Create `target` Series
target = data['HoF']
# Create `features` DataFrame
features = data.drop(['playerID', 'nameFirst', 'nameLast', 'HoF'], axis=1)

#Build Model
#Model #1: Logistic Regression model
# Import cross_val_predict, KFold and LogisticRegression from 'sklearn'
from sklearn.model_selection import cross_val_predict, KFold
from sklearn.linear_model import LogisticRegression
# Create Logistic Regression model
lr = LogisticRegression(class_weight='balanced')
# Create an instance of the KFold class
kf = KFold(n_splits=100, random_state=1)
# Create predictions using cross validation
predictions_lr = cross_val_predict(lr, features, target, cv=kf)

# Import NumPy as np
import numpy as np
# Convert predictions and target to NumPy arrays
np_predictions_lr = np.asarray(predictions_lr)
np_target = target.as_matrix()
# Determine True Positive count
tp_filter_lr = (np_predictions_lr == 1) & (np_target == 1)
tp_lr = len(np_predictions_lr[tp_filter_lr])
# Determine False Negative count
fn_filter_lr = (np_predictions_lr == 0) & (np_target == 1)
fn_lr = len(np_predictions_lr[fn_filter_lr])
# Determine False Positive count
fp_filter_lr = (np_predictions_lr == 1) & (np_target == 0)
fp_lr = len(np_predictions_lr[fp_filter_lr])
# Determine True Negative count
tn_filter_lr = (np_predictions_lr == 0) & (np_target == 0)
tn_lr = len(np_predictions_lr[tn_filter_lr])
# Determine True Positive rate
tpr_lr = tp_lr / (tp_lr + fn_lr)
# Determine False Negative rate
fnr_lr = fn_lr / (fn_lr + tp_lr)
# Determine False Positive rate
fpr_lr = fp_lr / (fp_lr + tn_lr)
# Print each count
print('LR True Positive: ' + str(tp_lr))
print('LR Flase Negative: ' + str(fn_lr))
print('LR False Positive: ' + str(fp_lr))
# Print each rate
print('LR True Positive Rate: ' + str(tpr_lr))
print('LR Flase Negative Rate: ' + str(fnr_lr))
print('LR False Positive Rate: ' + str(fpr_lr))


#Model #2 RandomForestClassifier

# Import RandomForestClassifier from sklearn
from sklearn.ensemble import RandomForestClassifier
# Create penalty dictionary
penalty = {
    0: 100,
    1: 1
}
# Create Random Forest model
rf = RandomForestClassifier(random_state=1,n_estimators=100, max_depth=11, min_samples_leaf=1, class_weight=penalty)
# Create predictions using cross validation
predictions_rf = cross_val_predict(rf, features, target, cv=kf)
# Convert predictions to NumPy array
np_predictions_rf = np.asarray(predictions_rf)
# Determine True Positive count
tp_filter_rf = (np_predictions_rf == 1) & (np_target == 1)
tp_rf = len(np_predictions_rf[tp_filter_rf])
# Determine False Negative count
fn_filter_rf = (np_predictions_rf == 0) & (np_target == 1)
fn_rf = len(np_predictions_rf[fn_filter_rf])
# Determine False Positive count
fp_filter_rf = (np_predictions_rf == 1) & (np_target == 0)
fp_rf = len(np_predictions_rf[fp_filter_rf])
0# Determine True Negative count
tn_filter_rf = (np_predictions_rf == 0) & (np_target == 0)
tn_rf = len(np_predictions_rf[tn_filter_rf])
# Determine True Positive rate
tpr_rf = tp_rf / (tp_rf + fn_rf)
# Determine False Negative rate
fnr_rf = fn_rf / (fn_rf + tp_rf)
# Determine False Positive rate
fpr_rf = fp_rf / (fp_rf + tn_rf)
# Print each count
print('RF True Positive: ' + str(tp_rf))
print('RF Flase Negative: ' + str(fn_rf))
print('RF False Positive: ' + str(fp_rf))
# Print each rate
print('RF True Positive Rate: ' + str(tpr_rf))
print('RF Flase Negative Rate: ' + str(fnr_rf))
print('RF False Positive Rate: ' + str(fpr_rf))

#The Random Forest and Logistic Regression Models are equally succesfull when it came to
#true positives and false negatives, but the Random Forest gives 11 less false positives.
#I'm an optimist, but the Logistic Regression model seems to be including a lot a releivers and I'm not that
#optimistic, so let's go with the Random Forest.

#Model to fit my data
new_data = df_eligible[num_cols_pitchers]
# Create a new features DataFrame
new_features = new_data.drop(['playerID', 'nameFirst', 'nameLast', 'HoF'], axis=1)
# Fit the Random Forest model
rf.fit(features, target)
# Estimate probabilities of Hall of Fame induction
probabilities = rf.predict_proba(new_features)
# Convert predictions to a DataFrame
hof_predictions = pd.DataFrame(probabilities[:,1])
# Sort the DataFrame (descending)
hof_predictions = hof_predictions.sort_values(0, ascending=False)
hof_predictions['Probability'] = round(hof_predictions[0], 2)
#Print 50 highest probability HoF inductees from still eligible players
for i, row in hof_predictions.head(50).iterrows():
     prob = ' '.join(('HoF Probability =', str(row['Probability'])))
     print('')
     print(prob)
     print(new_data.iloc[i,1:27])