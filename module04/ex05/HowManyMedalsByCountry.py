team_sports = ['BasketBall', 'Football', 'Tug-Of-War',
               'Badminton', 'Sailing', 'Handball', 'Water Polo', 'Hockey',
               'Rowing', 'Bobsleigh', 'Softball', 'Volleyball',
               'Synchronized Swimming', 'Baseball', 'Ruby Sevens', 'Rugby',
               'Lacrosse', 'Polo']

def how_many_medals_by_country(data, country):
    team_records = data[data['Sport'].isin(team_sports)]
    team_records = team_records[team_records['Team'] == country]
    results = team_records.groupby(by=['Year', 'Medal'])['Medal'].count()
    output = {}
    for year, _ in results.keys():
        output.update({int(year): {'G': 0, 'S': 0, 'B': 0}})
    for (year, medal), val in results.items():
        output[int(year)][medal[0]] = val
    return output
