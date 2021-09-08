# Uses python3
def edit_distance(string_x,string_y):
    string_x = ' ' + string_x
    string_y = ' ' + string_y

    # Obtain the length of the padded string
    len_x = len(string_x)
    len_y = len(string_y)

    # Initializing the distance matrix
    dist_mat = [[0] * len_y for i in range(len_x)]
    for i in range(len_x):
        dist_mat[i][0] = i
    for j in range(len_y):
        dist_mat[0][j] = j

    # Calculating the distance matrix row by row.
    for j in range(1, len_y):
        for i in range(1, len_x):
            # YOUR CODE HERE
            if (string_x[i] == string_y[j]):
                dist_mat[i][j] = dist_mat[i - 1][j - 1]
            else:
                dist_mat[i][j] = min(dist_mat[i][j - 1], dist_mat[i - 1][j], dist_mat[i - 1][j - 1]) + 1
            # raise NotImplementedError()
    return dist_mat[-1][-1]


if __name__ == "__main__":
    a = input()
    b = input()
    print(edit_distance(a,b))
