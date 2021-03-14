import os


def read_files(path):
    """Read all files in a folder and its subfolders.

    Args:
        path (str): path to the folder

    Returns:
        dict: dictionary of filename (key) and content as string (value)
    """

    file2content = dict()

    for root, dirs, files in os.walk(path):
        for f in files:

            file_path = os.path.join(root, f)
            with open(file_path, encoding='utf-8') as infile:
                text = infile.read()

                file2content[f] = text

    return file2content


def sum_function(values):
    """Sum the values in a list. 

    Args:
        values (list): List of numbers

    Returns:
        int: Sum of values
    """
    result = 0

    for i in values:
        result += i
    return result


if __name__ == "__main__":

    # First example
    my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    summed = sum_function(my_numbers)
    print(summed)

    # Second example
    data = read_files('data')
    print(f"Read {len(data)} files")
