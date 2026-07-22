import pandas as pd


def youngest_fellah(df, year):
    if not isinstance(df, pd.DataFrame):
        return None
    data_filter = df[df['Year'] == year][['Sex', 'Age']]
    woman = data_filter[data_filter['Sex'] == 'F']
    man = data_filter[data_filter['Sex'] == 'M']
    woman = woman.sort_values(['Age'], ignore_index=True)
    man = man.sort_values(['Age'], ignore_index=True)
    return {'f': float(woman.loc[0]['Age']), 'm': float(man.loc[0]['Age'])}
