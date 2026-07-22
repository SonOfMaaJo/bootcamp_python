import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


class Komparator:
    def __init__(self, datas):
        self.datas = datas

    def numeric_features(self, features):
        return [feature for feature in features if feature in
                self.datas.columns and
                pd.api.types.is_numeric_dtype(self.datas[feature])]

    def compare_box_plots(self, categorical_var, numerical_vars):
        num_features = self.numeric_features(numerical_vars)
        datas = self.datas[num_features + [categorical_var]].dropna()
        categorical_values = datas[categorical_var].unique()
        fig, axes = plt.subplots(nrows=len(num_features), ncols=1,
                                 figsize=(8, 8))
        axes = axes.flatten()
        for j, num_var in enumerate(numerical_vars):
            types_data = pd.DataFrame(columns=categorical_values)
            for type_c in categorical_values:
                types_data[type_c] = datas[datas[categorical_var] ==
                                           type_c][num_var] \
                    .reset_index(drop=True)
            types_data[categorical_values].boxplot(ax=axes[j])
            axes[j].set_title(num_var)
        plt.show()

    def density(self, categorical_var, numerical_vars):
        num_features = self.numeric_features(numerical_vars)
        datas = self.datas[num_features + [categorical_var]].dropna()
        categorical_values = datas[categorical_var].unique()
        fig, axes = plt.subplots(nrows=len(num_features), ncols=1,
                                 figsize=(8, 8))
        axes = axes.flatten()
        for j, num_var in enumerate(numerical_vars):
            types_data = pd.DataFrame(columns=categorical_values)
            for type_c in categorical_values:
                types_data[type_c] = datas[datas[categorical_var] ==
                                           type_c][num_var] \
                    .reset_index(drop=True)
            types_data[categorical_values].plot.density(ax=axes[j],
                                                        bw_method='silverman')
            axes[j].set_title(num_var)
        plt.show()

    def compare_histograms(self, categorical_var, numerical_vars):
        num_features = self.numeric_features(numerical_vars)
        datas = self.datas[num_features + [categorical_var]].dropna()
        categorical_values = datas[categorical_var].unique()
        fig, axes = plt.subplots(nrows=len(num_features), ncols=1,
                                 figsize=(8, 8))
        axes = axes.flatten()
        for j, num_var in enumerate(numerical_vars):
            types_data = pd.DataFrame(columns=categorical_values)
            for type_c in categorical_values:
                types_data[type_c] = datas[datas[categorical_var] ==
                                           type_c][num_var] \
                    .reset_index(drop=True)
            types_data[categorical_values].plot.hist(ax=axes[j],
                                                     bins=10,
                                                     alpha=0.5)
            axes[j].set_title(num_var)
        plt.show()
