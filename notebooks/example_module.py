def sum_function(values):
    result = 0
    for i in values:
        result += i
    return result


if __name__ == "__main__":
    new_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(sum_function(new_values))