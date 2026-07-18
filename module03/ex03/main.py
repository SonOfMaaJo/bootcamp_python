from ex01.ImageProcessor import ImageProcessor
imp = ImageProcessor()
arr = imp.load('/home/vnaoussi/Downloads/bootcamp_python-version-3.3.0/module03/attachments/elon_canaGAN.png')
from ex03.ColorFilter import ColorFilter
cf = ColorFilter()
imp.display(cf.to_grayscale(arr, 'w', r_weight=0.2, g_weight=0.3,
                            b_weight=0.5))
