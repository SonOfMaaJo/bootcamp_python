import matplotlib.pyplot as plt


class ImageProcessor(object):
    def load(self, path):
        try:
            image_array = plt.imread(path)
            print(f'Loading image of dimensions {image_array.shape[0]}'
                  f' x {image_array.shape[1]}')
            return image_array
        except Exception as e:
            print(f'Exception: {type(e).__name__} -- {e}')
            return None

    def display(self, array):
        try:
            plt.figure(figsize=(8, 6))
            plt.imshow(array)
            plt.title('Loaded Image')
            plt.axis('off')
            plt.show()
        except Exception as e:
            print(f'Exception: {type(e).__name__} -- {e}')
