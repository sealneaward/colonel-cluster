import api

frame = api.get_hustle_stats()
frame.to_csv('data/hustle.csv', index=False)

frame = api.get_opponent_shooting_by_zone()
frame.to_csv('data/zone_shooting.csv', index=False)

frame = api.get_overall_defense()
frame.to_csv('data/overall_defense.csv', index=False)

frame = api.get_speed_and_distance()
frame.to_csv('data/speed.csv', index=False)

frame = api.get_teams()
frame.to_csv('./data/team_records.csv', index=False)

# frame = api.get_players()
# frame.to_csv('./data/players.csv', index=False)
