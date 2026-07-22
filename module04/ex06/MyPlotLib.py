import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from math import ceil


class MyPlotLib:
    def numeric_features(self, data, features):
        return [feature for feature in features if feature in data.columns and
                pd.api.types.is_numeric_dtype(data[feature])]

    def histogram(self, data, features):
        num_features = self.numeric_features(data, features)
        nb = len(num_features)
        fig, axes = plt.subplots(nrows=ceil(nb / 3), ncols=nb % 3 if nb > 0
                                 else 1, figsize=(8, 8))
        axes = axes.flatten()
        for i, column in enumerate(num_features):
            data[column].hist(ax=axes[i],
                              color='#69b3a2'
                              )
            axes[i].set_title(f'{column}')
            axes[i].set_xlabel(column)
            axes[i].set_ylabel('Frequency')
        plt.tight_layout()
        plt.show()

    def density(self, data, features):
        num_features = self.numeric_features(data, features)
        data[num_features].plot.density(bw_method='silverman', figsize=(10, 6))
        plt.show()

    def pair_plot(self, data, features):
        num_features= self.numeric_features(data, features)
        num_datas = data[num_features]
        g = sns.PairGrid(num_datas)
        g.map_diag(sns.histplot, bins=10)
        g.map_offdiag(sns.scatterplot, s=1, alpha=0.5)
        plt.show()

    def box_plot(self, data, features):
        num_features = self.numeric_features(data, features)
        data.boxplot(column=num_features)
        plt.show()
