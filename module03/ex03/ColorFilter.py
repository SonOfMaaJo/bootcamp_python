import numpy as np


class ColorFilter(object):
    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        Args
        _____
            array:  numpy.ndarray corresponding to the image.
        Retrun:
        _____
            array:  numpy.ndarray corresponding to the transformed image.
            None:   otherwise.
        Raises:
        _____
            This function should not raise any Exception.
        """
        try:
            if not isinstance(array, np.ndarray):
                return None
            new_array = np.copy(array)
            new_array[:, :, :3] = 1 - array[:, :, :3]
            return new_array
        except Exception:
            return None

    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        _____
            array:  numpy.ndarray corresponding to the image.
        Return:
        _____
            array:  numpy.ndarray corresponding to the transformed image.
            None:   otherwise.
        Raises:
        _____
            This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None
        try:
            new_array = np.copy(array)
            x_dim, y_dim, _ = new_array.shape
            red = np.zeros((x_dim, y_dim))
            green = np.zeros((x_dim, y_dim))
            blue = new_array[:, :, 2]
            alpha = new_array[:, :, 3]
            new_array = np.dstack((red, green, blue, alpha))
            return new_array
        except Exception:
            return None

    def to_green(self, array):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        _____
            array:  numpy.ndarray corresponding to the image.
        Return:
        _____
            array:  numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        _____
            This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None
        try:
            new_array = np.copy(array)
            new_array[:, :, 2] = 0 * new_array[:, :, 2]
            new_array[:, :, 0] = 0 * new_array[:, :, 0]
            return new_array
        except Exception:
            return None

    def to_red(self, array):
        """
        Applies a red filter to the image received as numpy array.
        Args:
        _____
            array:  numpy.ndarray corresponding to the image.
        Return:
        _____
            array:  numpy.ndarray corresponding to the transformed image.
            None:   otherwise.
        Raises:
        _____
            This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None
        try:
            new_array = np.copy(array)
            green_array = self.to_green(array)
            blue_array = self.to_blue(array)
            new_array[:, :, :3] = new_array[:, :, :3] - green_array[:, :, :3] \
                - blue_array[:, :, :3]
            return new_array
        except Exception:
            return None

    def to_celluloid(self, array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
            celluloid filter is also known as cel-shading or toon-shading.
        Args:
        _____
            array:  numpy.ndarray corresponding to the image.
        Return:
        _____
            array:  mumpy.ndarray corresponding to the transformed image.
            None:   otherwise.
        Raises:
        _____
            This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None
        try:
            new_array = np.copy(array)
            new_array[array <= 0.2] = 0.0
            new_array[(array > 0.2) & (array <= 0.5)] = 0.33
            new_array[(array > 0.5) & (array <= 0.8)] = 0.66
            new_array[array > 0.8] = 1
            return new_array
        except Exception:
            return None

    def to_grayscale(self, array, v_filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = 'mean'/'m': performs the mean of RBG channels.
        For filter = 'weight'/'w': performs a weighted mean of RBF channels.
        Args:
        _____
            array:  numpy.ndarray corresponding to the image.
            filter: string with accepted values in ['m', 'mean', 'w', 'weight']
            weights:   [kwargs] 3 floats where the sum equals to 1,
                        corresponding to the weights of each RBG channels.
                        Excepting keys: 'r_weight', 'g_weight' and 'b_weight'.
        Return:
        _____
            array:  numpy.ndarray corresponding to the transformed image.
            None:   othewise.
        Raises:
        _____
            This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None
        try:
            new_array = np.copy(array)
            new_array = new_array[:, :, :3]
            x_dim, y_dim, _ = new_array.shape
            new_array = new_array.reshape(x_dim * y_dim, 3)
            if v_filter == 'm' or v_filter == 'mean':
                sum_arr = np.sum(new_array, axis=1)
                return sum_arr.reshape(x_dim, y_dim) / 3.0
            elif v_filter == 'weight' or v_filter == 'w':
                new_array[:, 0] = kwargs['r_weight'] * new_array[:, 0]
                new_array[:, 1] = kwargs['g_weight'] * new_array[:, 1]
                new_array[:, 2] = kwargs['b_weight'] * new_array[:, 2]
                sum_arr = np.sum(new_array, axis=1)
                return sum_arr.reshape(x_dim, y_dim)
            else:
                return None
        except Exception:
            return None
