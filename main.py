from save_frame import *
from glob import glob


if __name__ == "__main__":
    video_paths = glob("videos/*")
    save_dir = "save"
    for path in video_paths:
        save_frame(path, save_dir, gap=10)
