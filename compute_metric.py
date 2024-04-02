from metrics import entropy_for_dir

# source_dir = "datasets/small_data"
source_dir = "results/small_data/haze_removal"
# destination_file = "metric_scores/small_data/original_images.txt"
destination_file = "metric_scores/small_data/haze_removal.txt"

def main():
    avg_entropy = entropy_for_dir(source_dir, destination_file)
    print(f"avg entropy:\t{avg_entropy}")


if __name__ == "__main__":
    main()
