from metrics import entropy_for_dir
import os

# source_dir = "datasets/small_data"
source_dir = "results/Distributed_haze1k/test_thick/single_Image_Dehazing/"
# destination_file = "metric_scores/small_data/original_images.txt"
destination_file = "metric_scores/Distributed_haze1k/test_thick/single_Image_Dehazing.txt"

def main():
    destination_path = destination_file[:destination_file.rfind('/')]
    os.makedirs(destination_path, exist_ok=True)
    avg_entropy = entropy_for_dir(source_dir, destination_file)
    print(f"avg entropy:\t{avg_entropy}")


if __name__ == "__main__":
    main()
