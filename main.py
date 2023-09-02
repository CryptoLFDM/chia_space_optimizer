import shutil

from config import config

CHIA_CONST = {
    "1": {
        "k32": 87.5,
        "k33": 179.6,
        "k34": 368.2,
        "k35": 754.3,
    },
    "2": {
        "k32": 86.0,
        "k33": 176.6,
        "k34": 362.1,
        "k35": 742.2,
    },
    "3": {
        "k32": 84.5,
        "k33": 173.4,
        "k34": 355.9,
        "k35": 729.7,
    },
    "4": {
        "k32": 82.9,
        "k33": 170.2,
        "k34": 349.4,
        "k35": 716.8,
    },
    "5": {
        "k32": 81.3,
        "k33": 167.0,
        "k34": 343.0,
        "k35": 704.0,
    },
    "6": {
        "k32": 79.6,
        "k33": 163.8,
        "k34": 336.6,
        "k35": 691.1,
    },
    "7": {
        "k32": 78.0,
        "k33": 160.6,
        "k34": 330.2,
        "k35": 678.3,
    },
    "9": {
        "k32": 75.2,
        "k33": 154.1,
        "k34": 315.5,
        "k35": 645.8,
    }
}

compression_level = config['compression_level']

directories_to_calculate = config['directories_to_calculate']


# Function to get total space in GiB using shutil
def get_total_space(dir_path: str) -> float:
    total, used, free = shutil.disk_usage(dir_path)
    return total / (2 ** 30)  # Convert bytes to GiB


def display(total_gib_used: float, dir_path: str, disk_sizes: dict, best_combinations: dict):
    total_gib_percentage = (total_gib_used / disk_sizes[dir_path]) * 100
    k32_nbr = int(get_total_space(dir_path) / CHIA_CONST[str(compression_level)]["k32"])
    total_K32gib = k32_nbr * CHIA_CONST[str(compression_level)]["k32"]
    total_K32gib_percentage = (total_K32gib / disk_sizes[dir_path]) * 100

    print(f"Disk: {dir_path}")
    print(f"Disk Size (GiB): {disk_sizes[dir_path]:.2f} GiB")
    print(f"Total GiB Used: {total_gib_used:.2f} GiB ({total_gib_percentage:.2f}%)")
    print(f"Best Combination: {best_combinations[dir_path]}")
    print("K32 comparaison")
    print(f"Total K32 GiB Used: {total_K32gib:.2f} GiB ({total_K32gib_percentage:.2f}%) with {k32_nbr} K32 plots")
    print()


def main():
    best_combinations = {}
    disk_sizes = {}
    plots_possible = {}

    for dir_path in directories_to_calculate:
        total_space = get_total_space(dir_path)
        sorted_files = sorted(CHIA_CONST[str(compression_level)].items(), key=lambda x: x[1], reverse=True)

        best_combination = []
        total_gib_used = 0

        for file_type, file_size in sorted_files:
            if total_space >= file_size:
                num_files = int(total_space // file_size)
                best_combination.append((file_type, num_files))
                total_gib_used += num_files * file_size
                total_space -= num_files * file_size

        best_combinations[dir_path] = best_combination
        disk_sizes[dir_path] = get_total_space(dir_path)
        plots_possible[dir_path] = len(best_combination)

    for dir_path in directories_to_calculate:
        total_gib_used = sum(num_files * CHIA_CONST[str(compression_level)][file_type] for file_type, num_files in
                             best_combinations[dir_path])
        display(total_gib_used, dir_path, disk_sizes, best_combinations)


if __name__ == '__main__':
    main()