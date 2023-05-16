def dot_product(N, vector_1, vector_2):
    answer = 0
    for i in range(N):
        answer += vector_1[i] * vector_2[i]

    return answer
