import requests
import pandas as pd


def get_opponent_shooting_by_zone():
    url = 'http://stats.nba.com/stats/leaguedashplayershotlocations?College=&Conference=&Country=&DateFrom=&DateTo=' \
          '&DistanceRange=By+Zone&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0' \
          '&LeagueID=00&Location=&MeasureType=Opponent&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N' \
          '&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2016-17' \
          '&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    while response.status_code != 200:
        response = requests.get(url)
    headers = response.json()['resultSets']['headers'][1]['columnNames']

    # clean headers
    headers[5] = 'OPP_FGM_RA'
    headers[6] = 'OPP_FGA_RA'
    headers[7] = 'OPP_FG_PCT_RA'

    headers[8] = 'OPP_FGM_NRA'
    headers[9] = 'OPP_FGA_NRA'
    headers[10] = 'OPP_FG_PCT_NRA'

    headers[11] = 'OPP_FGM_MR'
    headers[12] = 'OPP_FGA_MR'
    headers[13] = 'OPP_FG_PCT_MR'

    headers[14] = 'OPP_FGM_LC3'
    headers[15] = 'OPP_FGA_LC3'
    headers[16] = 'OPP_FG_PCT_LC3'

    headers[17] = 'OPP_FGM_RC3'
    headers[18] = 'OPP_FGA_RC3'
    headers[19] = 'OPP_FG_PCT_RC3'

    headers[20] = 'OPP_FGM_AB3'
    headers[21] = 'OPP_FGA_AB3'
    headers[22] = 'OPP_FG_PCT_AB3'

    headers[5] = 'OPP_FGM_RA'
    headers[6] = 'OPP_FGA_RA'
    headers[7] = 'OPP_FG_PCT_RA'

    data = response.json()['resultSets']['rowSet']
    frame = pd.DataFrame(data, columns=headers)
    return frame


def get_hustle_stats():
    url = 'http://stats.nba.com/stats/leaguehustlestatsplayer?College=&Conference=&Country=&DateFrom=&DateTo=' \
          '&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=' \
          '&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=' \
          '&PlayerPosition=&PlusMinus=N&Rank=N&Season=2016-17&SeasonSegment=&SeasonType=Regular+Season' \
          '&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    while response.status_code != 200:
        response = requests.get(url)
    headers = response.json()['resultSets'][0]['headers']
    data = response.json()['resultSets'][0]['rowSet']
    frame = pd.DataFrame(data, columns=headers)
    return frame

def get_overall_defense():
    url = 'http://stats.nba.com/stats/leaguedashptstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=' \
          '&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0' \
          '&Outcome=&PORound=0&PerMode=PerGame&PlayerExperience=&PlayerOrTeam=Player&PlayerPosition=' \
          '&PtMeasureType=Defense&Season=2016-17&SeasonSegment=&SeasonType=Regular+Season&StarterBench=' \
          '&TeamID=0&VsConference=&VsDivision=&Weight='
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    while response.status_code != 200:
        response = requests.get(url)
    headers = response.json()['resultSets'][0]['headers']
    data = response.json()['resultSets'][0]['rowSet']
    frame = pd.DataFrame(data, columns=headers)
    return frame

def get_speed_and_distance():
    url = 'http://stats.nba.com/stats/leaguedashptstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=' \
          '&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0' \
          '&Outcome=&PORound=0&PerMode=PerGame&PlayerExperience=&PlayerOrTeam=Player&PlayerPosition=' \
          '&PtMeasureType=SpeedDistance&Season=2016-17&SeasonSegment=&SeasonType=Regular+Season&StarterBench=' \
          '&TeamID=0&VsConference=&VsDivision=&Weight='
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    while response.status_code != 200:
        response = requests.get(url)
    headers = response.json()['resultSets'][0]['headers']
    data = response.json()['resultSets'][0]['rowSet']
    frame = pd.DataFrame(data, columns=headers)
    return frame

def get_player_info(player_id):
    url = 'http://stats.nba.com/stats/commonplayerinfo?LeagueID=00' \
          '&PlayerID=' + str(player_id) + '&SeasonType=Regular+Season'
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    while response.status_code != 200:
        response = requests.get(url)
    headers = response.json()['resultSets'][0]['headers']
    data = response.json()['resultSets'][0]['rowSet']
    frame1 = pd.DataFrame(data, columns=headers)

    url = 'http://stats.nba.com/stats/playerdashboardbyyearoveryear?DateFrom=&DateTo=&GameSegment=&LastNGames=0' \
          '&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N' \
          '&PerMode=PerGame&Period=0&PlayerID=' + str(player_id) + '&PlusMinus=N&Rank=N&Season=2016-17&SeasonSegment=&' \
          'SeasonType=Regular+Season&ShotClockRange=&Split=yoy&VsConference=&VsDivision='
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    while response.status_code != 200:
        response = requests.get(url)
    headers = response.json()['resultSets'][0]['headers']
    data = response.json()['resultSets'][0]['rowSet']
    frame2 = pd.DataFrame(data, columns=headers)

    # get rid of crap I don't want
    frame = frame1[['PERSON_ID', 'FIRST_NAME', 'LAST_NAME',
    'DISPLAY_FIRST_LAST', 'HEIGHT', 'WEIGHT', 'POSITION', 'TEAM_ID', 'TEAM_NAME',
    'TEAM_ABBREVIATION']]
    frame['GP'] = frame2['GP']
    frame['PLAYER_ID'] = frame['PERSON_ID']
    frame['PLAYER_NAME'] = frame['DISPLAY_FIRST_LAST']

    return frame

def get_team_info(team_id):
    url = 'http://stats.nba.com/stats/teaminfocommon?LeagueID=00&Season=2016-17&SeasonType=Regular+Season' \
          '&TeamID=' + str(team_id)
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    while response.status_code != 200:
        response = requests.get(url)
    headers = response.json()['resultSets'][0]['headers']
    data = response.json()['resultSets'][0]['rowSet']
    frame = pd.DataFrame(data, columns=headers)
    # get rid of crap I don't want
    frame = frame[['TEAM_ID', 'TEAM_ABBREVIATION', 'W', 'L']]
    return frame

def get_players():
    data = pd.read_csv('./data/hustle.csv')
    players = data['PLAYER_ID'].values

    player_df = pd.DataFrame(columns=['PLAYER_ID', 'PLAYER_NAME', 'HEIGHT', 'WEIGHT', 'POSITION', 'TEAM_ID',
                                      'TEAM_NAME', 'TEAM_ABBREVIATION', 'GP'])

    for player in players:
        player_data = get_player_info(player)

        height = str(player_data['HEIGHT'].values[0])
        if len(height) < 1:
            continue
        height = str(player_data['HEIGHT'].values[0]).split('-')
        height = int(height[0]) * 12 + int(height[1])
        player_data['HEIGHT'] = height

        player_df = pd.concat([player_df, player_data])

    return player_df

def get_teams():
    data = pd.read_csv('./data/team_records.csv')
    teams = data['TEAM_ID'].values

    team_df = pd.DataFrame(columns=data.columns.values)

    for team in teams:
        team_data = get_team_info(team)
        team_data['WIN_PCT'] = team_data['W'].values[0] / (team_data['W'].values[0] + team_data['L'].values[0] * 1.0)
        team_df = pd.concat([team_df, team_data[['TEAM_ID', 'TEAM_ABBREVIATION', 'WIN_PCT']]])

    return team_df
