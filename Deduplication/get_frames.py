import os 
import shutil

input_path = os.path.abspath(os.path.join(os.path.realpath(__file__), os.path.pardir, 'data', 'input'))
# redefine and uncomment below, for other paths
# input_path = ""

reqd_frame_nos = list(map(str([
    16528,
    25317,
    25511,
    25939,
    25972,
    25681,
    25718,
    27366,
    27440,
    27552,
    27972,
    27939,
    27724,
    30219,
    30400,
    30454,
    30689,
    34069,
])))

for frame_file in os.listdir(input_path):
    if frame_file in reqd_frame_nos:
        shutil.copy(
            os.path.join(input_path, frame_file),
            os.path.join(output_path, frame_file
        )