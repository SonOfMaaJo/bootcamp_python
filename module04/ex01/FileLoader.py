import pandas as pd


class WrongParameters(Exception):
    pass

class FileLoader(object):
    def load(self, path):
        try:
            datas = pd.read_csv(path)
            print(f"Loading dataset of dimensions {datas.shape[0]}"
                  f" x {datas.shape[1]}")
            return datas
        except Exception as e:
            print(f"Exception: {type(e).__name__} -- {e}")

    def display(self, df, n):
        try:
            if not isinstance(df, pd.DataFrame) or not isinstance(n, int):
                raise WrongParameters("The parameters should be an dataFame"
                                      "and integers")
            if n < 0:
                print(df.tail(n))
            else:
                print(df.head(n))
        except Exception as e:
            print(f"Exception: {type(e).__name__} -- {e}")
