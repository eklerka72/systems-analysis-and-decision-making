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
            # arr[t-1][i-1] = 1
        i += 1
    return (arr)


