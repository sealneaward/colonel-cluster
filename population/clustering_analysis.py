import pandas as pd

clustering_data = pd.read_csv('./data/overall_cluster.csv')
regular_season_data = pd.read_csv('./data/team_records.csv')

teams = regular_season_data['TEAM_ABBREVIATION'].values

regular_season_data['Type_1'] = None
regular_season_data['Type_2'] = None
regular_season_data['Type_3'] = None
regular_season_data['Type_4'] = None
regular_season_data['Type_5'] = None

# get assignments for each team
for team in teams:
    clustering_assignments = clustering_data[clustering_data['TEAM_ABBREVIATION'] == team]
    # find the totals of each cluster type in data
    number_1 = len(clustering_assignments[clustering_assignments['CLUSTER'] == 1])
    number_2 = len(clustering_assignments[clustering_assignments['CLUSTER'] == 2])
    number_3 = len(clustering_assignments[clustering_assignments['CLUSTER'] == 3])
    number_4 = len(clustering_assignments[clustering_assignments['CLUSTER'] == 4])
    number_5 = len(clustering_assignments[clustering_assignments['CLUSTER'] == 5])

    regular_season_data['Type_1'][regular_season_data['TEAM_ABBREVIATION'] == team] = number_1
    regular_season_data['Type_2'][regular_season_data['TEAM_ABBREVIATION'] == team] = number_2
    regular_season_data['Type_3'][regular_season_data['TEAM_ABBREVIATION'] == team] = number_3
    regular_season_data['Type_4'][regular_season_data['TEAM_ABBREVIATION'] == team] = number_4
    regular_season_data['Type_5'][regular_season_data['TEAM_ABBREVIATION'] == team] = number_5

regular_season_data.to_csv('./data/team_records.csv', index=False)
