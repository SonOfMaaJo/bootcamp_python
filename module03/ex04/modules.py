import sys
import os


base_dir = os.path.dirname(__file__)
module_dir = os.path.join(base_dir, "..", "../module02/ex03")
sys.path.append(os.path.abspath(module_dir))

from csvreader import CsvReader
