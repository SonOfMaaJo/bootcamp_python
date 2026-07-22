import sys
import os

base_dir = os.path.dirname(__file__)
module_dir = os.path.join(base_dir, "..")
sys.path.append(os.path.abspath(module_dir))
from ex01.ImageProcessor import ImageProcessor
imp = ImageProcessor()
arr = imp.load('/home/vnaoussi/Downloads/bootcamp_python-version-3.3.0/module03/attachments/elon_canaGAN.png')
from ex03.ColorFilter import ColorFilter
cf = ColorFilter()
imp.display(cf.invert(arr))
imp.display(cf.to_green(arr))
imp.display(cf.to_red(arr))
imp.display(cf.to_blue)
imp.display(cf.to_celluloid(arr))
imp.display(cf.to_grayscale(arr, 'm'))
imp.display(cf.to_grayscale(arr, 'w', r_weight=0.2, g_weight=0.3,
                            b_weight=0.5))
