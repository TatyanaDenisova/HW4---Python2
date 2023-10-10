# Напишите функцию для транспонирования матрицы. Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

def my_def(matr: list[list[int]]) -> list[list[int]]:
    res = [[matr[i][j] for i in range(len(matr))] for j in range(len(matr[0]))]
    return res

matr = [[1, 2, 3], [4, 5, 6]]
print(my_def(matr))
