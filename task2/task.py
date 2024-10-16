import json
import numpy as np

def main(road):
    with open(road, "r") as read_file:
        data = json.load(read_file)
    nodes = data["nodes"]
    i = 1
    global arr
    global res
    arr = np.zeros((len(nodes), len(nodes)))
    while i <= len(nodes):
        temp = nodes[f'{i}']
        for j in temp:
            t = int(j)
            arr[i - 1][t - 1] = 1
            arr[t - 1][i - 1] = -1
        i += 1
    print(arr)
    res = np.zeros((5, len(nodes)))
    print(res)

    def serch_3(strok, stolb):
        global res
        global arr
        for u in range(0, len(nodes)):
            if arr[stolb, u] == 1:
                res[2, strok] += 1
                serch_3(strok, u)

    def serch_4(strok, stolb):
        global res
        global arr
        for u in range(0, len(nodes)):
            if arr[stolb, u] == -1:
                res[3, strok] += 1
                serch_4(strok, u)

    def serch_5(strok, stolb):
        global res
        global arr
        for u in range(0, len(nodes)):
            if arr[stolb, u] == 1 and u != strok:
                res[4, strok] += 1

    for i in range(0, len(nodes)):
        for t in range(0, 5):
            if t == 0:
                for j in range(0, len(nodes)):
                    if arr[i][j] == 1:
                        res[0][i] += 1
            elif t == 1:
                for j in range(0, len(nodes)):
                    if arr[i][j] == -1:
                        res[1][i] += 1
            elif t == 2:
                for j in range(0, len(nodes)):
                    if arr[i][j] == 1:
                        # res[2][i] += 1
                        serch_3(i, j)
            elif t == 3:
                for j in range(0, len(nodes)):
                    if arr[i][j] == -1:
                        serch_4(i, j)
            elif t == 4:
                for j in range(0, len(nodes)):
                    if arr[i][j] == -1:
                        serch_5(i, j)
    return res




