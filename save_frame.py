import os
import cv2


def create_dir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print(f"Error path")


def save_frame(video_path, save_dir, gap=10):
    name = video_path.split("/")[-1].split(".")[0]
    save_path = os.path.join(save_dir, name)
    create_dir(save_path)

    cap = cv2.VideoCapture(video_path)
    idx = 0

    while True:
        ret, frame = cap.read()
        if ret == False:
            cap.release()
            break
        if idx == 0:
            cv2.imwrite(f"{save_path}/{idx}.png", frame)
        else:
            if idx % gap == 0:
                cv2.imwrite(f"{save_path}/{idx}.png", frame)

        idx += 1
