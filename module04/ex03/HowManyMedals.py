def how_many_medals(df, name):
    try:
        group_year = df[df['Name'] == name].groupby(by=['Year', 'Medal'])
        result = group_year['Medal'].count()
        output = {}
        for year, _ in result.keys():
            output.update({int(year): {'G': 0, 'S': 0, 'B': 0}})
        for (year, medal), res in result.items():
            output[int(year)][medal[0]] = res
        return output
    except Exception as e:
        print(f'Exception: {type(e).__name__} -- {e}')
