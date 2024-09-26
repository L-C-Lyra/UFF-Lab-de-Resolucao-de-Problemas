def read_matrices(num_rows, num_columns):
    matrix = list()
    for _ in range(num_rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix


def integral_image(matrix_n, num_rows, num_columns):
    int_image_n = list()
    for _ in range(num_rows):
        row = [None] * num_columns
        int_image_n.append(row)

    for row in range(num_rows):
        for col in range(num_columns):
            if row == 0 and col == 0:
                int_image_n[row][col] = matrix_n[row][col]
            elif row == 0:
                int_image_n[row][col] = matrix_n[row][col] + int_image_n[row][col - 1]
            elif col == 0:
                int_image_n[row][col] = matrix_n[row][col] + int_image_n[row - 1][col]
            else:
                int_image_n[row][col] = matrix_n[row][col] + int_image_n[row][col - 1] + int_image_n[row - 1][col] - int_image_n[row - 1][col - 1]
    return int_image_n


def sum_interval():
    pass


def main():
    num_rows, num_columns = map(int, input().split())
    matrix_a = read_matrices(num_rows, num_columns)
    int_image_a = integral_image(matrix_a, num_rows, num_columns)
    print(matrix_a)
    print(int_image_a)


if __name__ == "__main__":
    main()
