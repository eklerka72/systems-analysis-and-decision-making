import json
import numpy as np


def main(road):
    with open(road, "r") as read_file:
        data = json.load(read_file)
    nodes = data["nodes"]
    i = 1
    arr = np.zeros((len(nodes), len(nodes)))
    while i <= len(nodes):
        temp = nodes[f'{i}']
        for j in temp:
            t = int(j)
            arr[i - 1][t - 1] = 1
        i += 1

    global res
    res = arr

    def search(i, j):
        global arr
        global res
        for t in range(0, len(nodes)):
            if res[j, t] != 0:
                if res[i, t] == 0:
                    res[i, t] += 2
                else:
                    res[i, t] += 1
                search(i, t)

    temp = 0
    for i in range(0, len(nodes)):
        for j in range(0, len(nodes)):
            if res[i][j] != 0:
                search(i, j)
            if arr[i][j] == 1:
                temp += 1

    sum = 0
    for j in range(0, len(nodes)):
        for i in range(0, temp):
            if res[j][i] != 0:
                sum += res[j][i] / (len(nodes) - 1) * np.log2(res[j][i] / (len(nodes) - 1))
    sum = round(-sum, 1)

    return (sum)
