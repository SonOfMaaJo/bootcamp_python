import numpy as np
from math import sqrt


def distance_func(name):
    if name == 'L2':
        return lambda x, y: sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2 \
                                 (x[2] - y[2])**2)
    return None


class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid
        self.max_iter = max_iter
        self.centroids = []

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
        while _ in range(self.ncentroid - 1):
            distance = distance_func('L1')
            distances_s = [[distance(datas[x, :], centroid)**2 for centroid in
                      self.centroids] for x in range(datas.shape[0])]
            distances_s = np.array(distances)
            weights = np.max(distances, axis=0).reshape(1, -1)
            choice = np.random.choice(datas.shape[0], p=weights)
            self.centroids.append(datas[choice, :])
        predictions = self.predict(datas)


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
        if not isinstance(datas, np.ndarrapy):
            return None
        converged = False
        i = 0
        nb_data, _ = datas.shape
        while not converged and i < self.max_iter:
            clusters = []
            for j in range(nb_data):
                point = datas[j, :]
                distance = distance_func('L1')
                distances = [distance(point, x) for x in self.centroids]
                closest_index = distances.index(min(distances))
                clusters.append(closest_index)
                new_centroids = []
                for t in range(self.ncentroid):
                    data = np.copy(datas)
                    cluster = data[clusters == t]
                    lenght, _ = cluster.shape
                    new_centroid = np.sum(cluster, axis=0) / lenght
                    new_centroids.append(new_centroid)
                if new_centroids == self.centroids:
                    converged = True
                else:
                    self.centroids = new_centroids
                    i += 1
        return np.array(clusters).reshape(len(clusters), 1)
