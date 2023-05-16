data_1 = list(map(int, input().split()))
data_2 = list(map(int, input().split()))

if ((data_1[0]  - data_2[0])** 2 + (data_1[1] - data_2[1]) ** 2) ** 0.5 <= data_1[2] + data_2[2]:
    if ((data_1[0]  - data_2[0])** 2 + (data_1[1] - data_2[1]) ** 2) ** 0.5 < data_1[2] - data_2[2] or \
    ((data_1[0]  - data_2[0])** 2 + (data_1[1] - data_2[1]) ** 2) ** 0.5 < data_2[2] - data_1[2]:
        print("NO")
    else:
        print("YES")
else:
    print("NO")
