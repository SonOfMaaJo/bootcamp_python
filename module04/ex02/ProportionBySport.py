import pandas as pd


def proportion_by_sport(df, year, sport, gender):

    data = df[(df['Year'] == year) & (df['Sex'] == gender)].drop_duplicates(
        subset=["ID", "Sport"]
    )
    return data[data['Sport'] == sport].shape[0] / data.shape[0]

