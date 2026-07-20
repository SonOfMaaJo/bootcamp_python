import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from modules import CsvReader
import sys


def distance_func(name):
    if name == 'L2':
        return lambda x, y: sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2 +
                                 (x[2] - y[2])**2)
    if name == 'L1':
        return lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1]) + abs(
            x[2] - y[2])
    return None


class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid
        self.max_iter = max_iter
        self.centroids = []
        self.predictions = None

    def fit(self, datas, dist_name='L2', cent='r'):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, ramdomly pick n centroids
        from the dataset.
        Args:
        _____
            datas: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        _____
            None.
        Raises:
        _____
            This function should not raise any Exception.
        """
        distance = distance_func(dist_name)
        if cent == 'r':
            centroids_idx = np.random.choice(datas.shape[0], self.ncentroid,
                                             replace=False)
            self.centroids = datas[centroids_idx]
        elif cent == 'rpp':
            choice = np.random.choice(datas.shape[0])
            self.centroids.append(datas[choice, :])
            for _ in range(self.ncentroid - 1):
                distances_s = [[distance(datas[x, -3:], centroid[-3:])**2 for
                                centroid in self.centroids]
                               for x in range(datas.shape[0])]
                distances_s = np.array(distances_s)
                weights = np.max(distances_s, axis=1)
                weights = np.mean(weights, axis=0)
                choice = np.random.choice(datas.shape[0], p=weights)
                self.centroids.append(datas[choice, :])
        self.predictions = self.predict(datas, distance)

    def predict(self, datas, distance):
        """
        Predict from which cluster each datapoint belongs to.
        Args:
        _____
            X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        _____
            the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        _____
            This function should not raise any Exception.
        """
        if not isinstance(datas, np.ndarray):
            return None
        i = 0
        nb_data, _ = datas.shape
        while i < self.max_iter:
            clusters = [[] for _ in range(self.ncentroid)]
            predicts = []
            for j in range(nb_data):
                point = datas[j, :]
                distances = [distance(point[-3:], x[-3:])
                             for x in self.centroids]
                closest_index = distances.index(min(distances))
                clusters[closest_index].append(point)
                predicts.append(closest_index)
            newcentroids = []
            for j in range(self.ncentroid):
                cluster = np.array(clusters[j])
                centroid = np.mean(cluster, axis=0)
                newcentroids.append(centroid)
            self.centroids = newcentroids
            i += 1
        return np.array(predicts).reshape(nb_data, -1)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('python Kmeans.py filepath=path_to_file ncentroid=int '
              'max_iter=int')
        sys.exit()
    try:
        filepath = sys.argv[1].split('=')[1]
        ncentroid = int(sys.argv[2].split('=')[1])
        max_iter = int(sys.argv[3].split('=')[1])
        with CsvReader(filename=filepath, header=True, skip_top=1,
                       skip_bottom=0) as file:
            datas = file.getdata()
            datas = [[float(data[i]) for i in range(len(data)) if i > 0]
                     for data in datas]
            datas = np.array(datas)
            header = file.getheader()[-3:]
            kmeans = KmeansClustering(max_iter=max_iter, ncentroid=ncentroid)
            kmeans.fit(datas, cent='r')
            homelands = {
                'Venus': [0, 'gold'],
                'Earth': [0, 'royalblue'],
                'Mars': [0, 'orangered'],
                'Asteroids': [0, 'teal'],
            }
            classement = [(i, cent) for i, cent in enumerate(kmeans.centroids)]
            classement = sorted(classement, key=lambda x: x[1][0])
            homelands['Asteroids'][0] = classement[-1][0]
            classement = classement[:-1]
            classement = sorted(classement, key=lambda x: x[1][1])
            venus = classement[0]
            classement = classement[1:]
            b_classement = classement
            classement = sorted(classement, key=lambda x: x[1][0])
            if classement[1][1][2] < venus[1][2]:
                homelands['Mars'][0] = classement[1][0]
                homelands['Earth'][0] = classement[0][0]
                homelands['Venus'][0] = venus[0]
            else:
                homelands['Mars'][0] = venus[0]
                homelands['Venus'][0] = b_classement[0][0]
                homelands['Earth'][0] = b_classement[1][0]
            for homeland, centroid in homelands.items():
                print(f'Details of centroids from {homeland}:\n',
                      f'{header[0]} = {kmeans.centroids[centroid[0]][0]}\n',
                      f'{header[1]} = {kmeans.centroids[centroid[0]][1]}\n',
                      f'{header[2]} = {kmeans.centroids[centroid[0]][2]}\n',
                      'numbers of individuals',
                      f' = {kmeans.predictions[kmeans.predictions
                                               == centroid[0]].shape[0]}',
                      '\n\n')
            fig = plt.figure(figsize=(8, 6))
            ax = fig.add_subplot(111, projection="3d")
            for homeland, tpl in homelands.items():
                points = datas[kmeans.predictions[:, 0] == tpl[0]]
                centroid = kmeans.centroids[tpl[0]]
                ax.scatter(
                    points[:, 0],
                    points[:, 1],
                    points[:, 2],
                    color=tpl[1],
                    s=20,
                    alpha=0.7,
                    label=homeland
                )
                ax.scatter(
                    centroid[0],
                    centroid[1],
                    centroid[2],
                    color=tpl[1],
                    marker="x",
                    s=250,
                    linewidths=3,
                )
            ax.set_xlabel(header[0])
            ax.set_ylabel(header[1])
            ax.set_zlabel(header[2])
            ax.set_title("solar system census")
            ax.legend()
            plt.show()

    except Exception as e:
        print(f'Exception: {type(e).__name__}: -- {e}')
