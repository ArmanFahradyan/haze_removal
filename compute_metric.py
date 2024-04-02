from metrics import entropy_for_dir

source_dir = "datasets/small_data"
destination_file = ""

def main():
    avg_entropy = entropy_for_dir(source_dir, destination_file)
    print(f"avg entropy:\t{avg_entropy}")


if __name__ == "__main__":
    main()
