import os 
import shutil

def is_exact_frame(file_, all_frames, pool_):
    for frame, is_poss in zip(all_frames, pool_):
        if is_poss:
            start = file_.find(frame)
            end = start + len(frame) - 1
            if start<1 or (end+1)>=len(file_):
                continue
            # Check full match
            if not(file_[start-1].isdigit() or file_[end+1].isdigit()):
                return True
    return False

output_path = os.path.abspath(os.path.join(os.path.realpath(__file__), os.path.pardir, 'data', 'output'))
input_path = os.path.abspath(os.path.join(os.path.realpath(__file__), os.path.pardir, 'data', 'input'))
# redefine and uncomment below, for other paths
input_path = "/home/karthikd/Workspace/MachineLearning/Projects/SIH'22/Frames-Preprocessing/Deduplication/data/shrimp_dec20_para"

"""
# Chengalpattu Tank
reqd_frame_nos = list(map(str, [
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
]))
"""

# """
# Shrimp - Dec 20
reqd_frame_nos = list(map(str, [
    297,
    313,
    390,
    401,
    439,
    521,
    649,
    688,
    695
]))
# """


frame_file_l = os.listdir(input_path)
for frame_file in frame_file_l:
    poss_pool = [(reqd_frame in frame_file) for reqd_frame in reqd_frame_nos]
    if any(poss_pool) and is_exact_frame(frame_file, reqd_frame_nos, poss_pool):
        shutil.copy(
            os.path.join(input_path, frame_file),
            os.path.join(output_path, frame_file)
        )