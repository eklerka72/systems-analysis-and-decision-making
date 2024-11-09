import numpy as np
import math

def sum_column(matrix, column_index):
  column_sum = 0
  for row in matrix:
      column_sum += row[column_index]
  return column_sum

def main():

    types = 4
    age_groups = 5
    arr = np.array([[20, 15, 10, 5],
           [30, 20, 15, 10],
           [25, 25, 20, 15],
            [20, 20, 25, 20],
           [15, 15, 30, 25]])
    result = np.zeros(5)

    probabilitys = np.zeros((age_groups, types))
    all_sum = 0

    for i in range(age_groups):
        all_sum+=sum(arr[i])


    for i in range(age_groups):
        for j in range(types):
            probabilitys[i][j] = arr[i][j]/all_sum


    res_ent_sov = 0
    for i in range(age_groups):
        for j in range(types):
            res_ent_sov += probabilitys[i][j]*math.log(probabilitys[i][j], 2)

    res_ent_ages = 0
    for k in range(age_groups):
        temp = sum(probabilitys[k])
        res_ent_ages += temp*math.log(temp, 2)

    res_ent_types =0
    for k in range(types):
        temp = sum_column(probabilitys, k)
        res_ent_types += temp*math.log(temp, 2)

    res_ent_usl = 0
    probabilitys_usl = np.zeros((age_groups, types))
    for i in range(age_groups):
        temp = sum(probabilitys[i])
        for j in range(types):
            temp_1 = probabilitys[i][j]/temp
            probabilitys_usl[i][j] = round(-temp_1*math.log(temp_1, 2), 2)

    for i in range(age_groups):
        temp = 0
        for j in range(types): #ответ по книге получается, если не умножать на log
            temp += probabilitys_usl[i][j]*math.log(probabilitys_usl[i][j], 2)
        res_ent_usl += temp*sum(probabilitys[i])


    result[0] = round(-res_ent_sov,2)
    result[1] = round(-res_ent_ages, 2)
    result[2] = round(-res_ent_types, 2)
    result[3] = round(-res_ent_usl, 2)
    result[4] = result[1] - result[3]

    return result

#print(main())