"""
Найти редакционное расстояние между строками
"""


def levenshtein_algorithm(A, B):
    F = [[(i + j) if i * j == 0 else 0 for j in range(len(B) + 1)]
         for i in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i-1] == B[j-1]:
                F[i][j] = F[i-1][j-1]
            else:
                F[i][j] = 1 + min(F[i-1][j], F[i][j-1], F[j-1][j-1])
    return F[-1][-1]


str1 = "колокол"
str2 = "молоко"
print(levenshtein_algorithm(str1, str2))
