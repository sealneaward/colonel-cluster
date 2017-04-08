import api


if __name__ == '__main__':
    frame = api.get_hustle_stats()
    frame.to_csv('data/defense/hustle.csv', index=False)

    frame = api.get_opponent_shooting_by_zone()
    frame.to_csv('data/defense/zone_shooting.csv', index=False)

    frame = api.get_shooting_by_zone()
    frame.to_csv('data/offense/zone_shooting.csv', index=False)

    frame = api.get_overall_defense()
    frame.to_csv('data/defense/overall_defense.csv', index=False)

    frame = api.get_speed_and_distance()
    frame.to_csv('data/speed.csv', index=False)

    frame = api.get_players()
    frame.to_csv('./data/players.csv', index=False)
