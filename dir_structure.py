import os


abs_path = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(abs_path)
data_dir = os.path.join(BASE_DIR,"data")

input_dir = os.path.join(data_dir, "inputs")
output_dir = os.path.join(data_dir,"outputs")
