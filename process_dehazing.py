import os
import cv2

from single_image_dehazing import image_dehazer
from haze_removal import run_file


source_dir = "datasets/Distributed_haze1k/test_thick/input"
destination_dir = "results/Distributed_haze1k/test_thick/single_Image_Dehazing" # haze_removal
# destination_dir = "results/small_data/Single_Image_Dehazing"


def main():
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir, exist_ok=True)
    image_names = sorted([file for file in os.listdir(source_dir) if not file.startswith('.')])
    for name in image_names:
        image = cv2.imread(os.path.join(source_dir, name))
        processed_image, haze_map = image_dehazer.remove_haze(image, showHazeTransmissionMap=False)
        # processed_image = run_file(os.path.join(source_dir, name))
        cv2.imwrite(os.path.join(destination_dir, name), processed_image)


if __name__ == "__main__":
    main()