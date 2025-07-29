import math

def calculate_column_statistics(file_paths, column_index, start_row, output_file):
    column_averages = []

    def write_and_print(message, file_handle):
        print(message)
        file_handle.write(message + '\n')

    with open(output_file, 'w') as out:
        write_and_print(f"Statistics for files:", out)
        for file_path in file_paths:
            write_and_print(f"{file_path}", out)
        write_and_print("", out)

        for file_path in file_paths:
            column_values = []
            with open(file_path, 'r') as file:
                for _ in range(start_row):
                    next(file)
                for line in file:
                    columns = line.strip().split()
                    if len(columns) > column_index:
                        try:
                            value = float(columns[column_index])
                            column_values.append(value)
                        except ValueError:
                            print(f"Skipping non-numeric value in file {file_path}: {columns[column_index]}")
            if column_values:
                average = sum(column_values) / len(column_values)
                column_averages.append(average)
                write_and_print(f"Average of column {column_index} in {file_path}: {average}", out)
            else:
                write_and_print(f"No valid values found in column {column_index} in {file_path}", out)

        if column_averages:
            avg_of_averages = sum(column_averages) / len(column_averages)
            std_deviation = math.sqrt(sum((x - avg_of_averages) ** 2 for x in column_averages) / len(column_averages))
            std_error = std_deviation / math.sqrt(len(column_averages))

            write_and_print(f"\nAverage of the averages: {avg_of_averages}", out)
            write_and_print(f"Standard Deviation of averages: {std_deviation}", out)
            write_and_print(f"Standard Error of averages: {std_error}", out)
        else:
            write_and_print("No valid values found in any of the files.", out)


# === User inputs ===
prefix = input("Enter the prefix (e.g. 'virus_widom' or 'euk_alpha'): ")
middle = input("Enter the middle part (e.g. 'H4_A' or 'H2A_B'): ")

# Fixed values
num_files = 4
column_index = 1
start_row = 0

# === Generate file paths ===
file_paths = [f"{prefix}.rmsd.{middle}_{i+1}.dat" for i in range(num_files)]

# Output file name
output_file = f"avg_rmsd_{prefix}_{middle}.dat"

# === Run calculation ===
calculate_column_statistics(file_paths, column_index, start_row, output_file)

print(f"\nResults written to {output_file}")

