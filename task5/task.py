import json
import numpy as np


def get_matrix(filepath: str):
    with open(filepath, 'r') as file:
        clusters = json.load(file)

    clusters = [c if isinstance(c, list) else [c] for c in clusters]
    n = sum(len(cluster) for cluster in clusters)

    matrix = [[1] * n for _ in range(n)]

    worse = []
    for cluster in clusters:
        for worse_element in worse:
            for element in cluster:
                matrix[element - 1][worse_element - 1] = 0
        for element in cluster:
            worse.append(int(element))

    return np.array(matrix)


def find_clusters(matrix, est1, est2):
    conflict_core = []

    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            if matrix[i][j] == 0 and matrix[j][i] == 0:
                conflict_pair = sorted([i + 1, j + 1])
                if conflict_pair not in conflict_core:
                    conflict_core.append(conflict_pair)

    final_result = [pair[0] if len(pair) == 1 else pair for pair in conflict_core]
    return str(final_result)


def main(file_path1, file_path2):
    matrix1 = get_matrix(file_path1)
    matrix2 = get_matrix(file_path2)

    matrix_and = np.multiply(matrix1, matrix2)
    matrix_and_t = np.multiply(np.transpose(matrix1), np.transpose(matrix2))
    matrix_or = np.maximum(matrix_and, matrix_and_t)

    clusters = find_clusters(matrix_or, matrix1, matrix2)
    print(clusters)


#temp = main("C:/system_alalys/task5/ex_1.json", "C:/system_alalys/task5/ex_2.json")