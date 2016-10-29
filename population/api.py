import requests
import pandas as pd


def get_rim_protection():
    url = 'http://stats.nba.com/stats/leaguedashptstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=' \
          '&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0' \
          '&Outcome=&PORound=0&PerMode=Totals&PlayerExperience=&PlayerOrTeam=Player&PlayerPosition=' \
          '&PtMeasureType=Defense&Season=2015-16&SeasonSegment=&SeasonType=Regular+Season&StarterBench=' \
          '&TeamID=0&VsConference=&VsDivision=&Weight='
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    while response.status_code != 200:
        response = requests.get(url)
    headers = response.json()['resultSets'][0]['headers']
    data = response.json()['resultSets'][0]['rowSet']
    frame = pd.DataFrame(data, columns=headers)
    return frame


def get_opponent_shooting_by_zone():
    url = 'http://stats.nba.com/stats/leaguedashplayershotlocations?College=&Conference=&Country=&DateFrom=&DateTo=' \
          '&DistanceRange=By+Zone&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0' \
          '&LeagueID=00&Location=&MeasureType=Opponent&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N' \
          '&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2015-16' \
          '&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=' \
          '&VsDivision=&Weight='
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
          '&PlayerPosition=&PlusMinus=N&Rank=N&Season=2015-16&SeasonSegment=&SeasonType=Regular+Season' \
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
          '&PtMeasureType=Defense&Season=2015-16&SeasonSegment=&SeasonType=Regular+Season&StarterBench=' \
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
          '&PtMeasureType=SpeedDistance&Season=2015-16&SeasonSegment=&SeasonType=Regular+Season&StarterBench=' \
          '&TeamID=0&VsConference=&VsDivision=&Weight='
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    while response.status_code != 200:
        response = requests.get(url)
    headers = response.json()['resultSets'][0]['headers']
    data = response.json()['resultSets'][0]['rowSet']
    frame = pd.DataFrame(data, columns=headers)
    return frame




