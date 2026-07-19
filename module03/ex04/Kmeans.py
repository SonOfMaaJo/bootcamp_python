import numpy as np
from math import sqrt
from modules import CsvReader
import sys


def distance_func(name):
    if name == 'L2':
        return lambda x, y: sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2 +
                                 (x[2] - y[2])**2)
    return None


class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid
        self.max_iter = max_iter
        self.centroids = []
        self.clusters = []
        self.predictions = None

    def fit(self, datas):
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
        choice = np.random.choice(datas.shape[0])
        self.centroids.append(datas[choice, :])
        for _ in range(self.ncentroid - 1):
            distance = distance_func('L2')
            distances_s = [[distance(datas[x, -3:], centroid[-3:])**2 for
                            centroid in self.centroids]
                           for x in range(datas.shape[0])]
            distances_s = np.array(distances_s)
            weights = np.max(distances_s, axis=1)
            weights = weights / np.sum(weights)
            choice = np.random.choice(datas.shape[0], p=weights)
            self.centroids.append(datas[choice, :])
        self.predictions = self.predict(datas)

    def predict(self, datas):
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
                distance = distance_func('L2')
                distances = [distance(point[-3:], x[-3:])
                             for x in self.centroids]
                closest_index = distances.index(min(distances))
                clusters[closest_index].append(point)
                predicts.append(closest_index)
            self.clusters = clusters
            newcentroids = []
            for j in range(self.ncentroid):
                cluster = np.array(clusters[j])
                centroid = np.sum(cluster, axis=0) / cluster.shape[0]
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
            datas = [[float(data[i]) if i > 0 else int(data[i])
                      for i in range(len(data))] for data in datas]
            datas = np.array(datas)
            header = file.getheader()[-3:]
            kmeans = KmeansClustering(max_iter=max_iter, ncentroid=ncentroid)
            kmeans.fit(datas)
            homelands = {
                'Venus': [0, 'gold'],
                'Earth': [0, 'royalblue'],
                'Mars': [0, 'orangered'],
                'Asteroids': [0, 'teal'],
            }
            classement = sorted(kmeans.centroids, key=lambda x: x[1])
            homelands['Asteroids'][0] = classement[-1]
            classement = classement[:-1]
            classement = sorted(classement, key=lambda x: x[2])
            venus = classement[0]
            classement = classement[1:]
            b_classement = classement
            classement = sorted(classement, key=lambda x: x[1])
            if classement[1][3] < venus[3]:
                homelands['Mars'][0] = classement[1]
                homelands['Earth'][0] = classement[0]
                homelands['Venus'][0] = venus
            else:
                homelands['Mars'][0] = venus
                homelands['Venus'][0] = b_classement[0]
                homelands['Earth'][0] = b_classement[1]
            for homeland, centroid in homelands.items():
                for i in range(kmeans.ncentroid):
                    cent = kmeans.centroids[i]
                    if (cent[1] == centroid[0][1] and cent[2]
                            == centroid[0][2]) \
                            and cent[3] == centroid[0][3]:
                        index = i
                        break
                print(f'Details of centroids from {homeland}:\n',
                      f'{header[0]} = {centroid[0][1]}\n',
                      f'{header[1]} = {centroid[0][2]}\n',
                      f'{header[2]} = {centroid[0][3]}\n',
                      'numbers of individuals',
                      f' = {len(kmeans.clusters[i])}',
                      '\n\n')
    except Exception as e:
        print(f'Exception: {type(e).__name__} -- {e}')
