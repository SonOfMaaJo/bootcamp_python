import numpy as np


class ScrapBooker(object):
    def crop(self, array, dim, position=(0, 0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width of the image) from the coordinates given by position
        arguments.

        Args:
        _____
            array:      numpy.ndarray
            dim:        tuple of 2 integers.
            position:   tuple of 2 integers.

        Returns:
        _____
            new_arr:    the cropped numpy.ndarray.
            None:       (if the combination of parameters is not possible.)
        """
        if not isinstance(array, np.ndarray) or not isinstance(dim, tuple):
            return None
        try:
            return array[position[0]:dim[0] + position[0],
                         position[1]:dim[1] + position[1]]
        except Exception:
            return None

    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis (0: vertical,
        1: horizontal)

        Args:
        _____
            array:  numpy.ndarray.
            n:      non null positive integer lower than the number of
                    row/column of the array (depending of axis value)
            axis:   positive non null integer.

        Returns:
        _____
            new_array:  thined numpy.ndarray.
            None:       (if the combination of parameters is not possible).

        Raises:
        _____
            This function should not raise any Exception
        """
        if not isinstance(array, np.ndarray) or not isinstance(n, int):
            return None
        if axis != 0 and axis != 1:
            return None
        return np.delete(array, n, axis)

    def juxtapose(self, array, n, axis):
        """
        Juxtapose n copies of the image along the specified axis.

        Args:
        _____
            array:  numpy.ndarray.
            n:      positive non null integer.
            axis:   integer of value 0 or 1.

        Returns:
        _____
            new_arr:    juxtaposed numpy.ndarray.
            None:       (if the combination of parameters is not possible).

        Raises:
        _____
            This function should not raise any Exception.
        """
        if axis != 0 and axis != 1 or n < 0:
            return None
        if not isinstance(n, int) and not isinstance(array, np.ndarray):
            return None
        if n == 0:
            return np.array([])
        if n == 1:
            return array
        new_arr = np.concat((array, array), axis=axis)
        for _ in range(n - 2):
            new_arr = np.concat((new_arr, array), axis=axis)
        return new_arr

    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array. The dim argument
        specifies the number of repetition along each dimensions.

        Args:
        _____
            array:  numpy.ndarray.
            dim:    tuple of 2 integers.

        Return:
        _____
            new_arr:    mosaic numpy.ndarray.
            None:       (combinaison of parameters not compatible).

        Raises:
        _____
            This function should not raise any Exception.
        """
        new_array = self.juxtapose(array, dim[0], 0)
        new_array = self.juxtapose(new_array, dim[1], 1)
        return new_array
