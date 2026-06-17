# for i in range(10):
#     print(i)
#     if i == 5 :
#         print(exit)
#         exit()


num = [1,2,3,4,5]

square_num = [num*num for num in num]
print(square_num)

even_num = [num for num in num if num % 2 == 0]
print(even_num)


def double(x) :
    return x * 2

double_num = list(map(double, [1,2,3,4,5]))
print(double_num)


def triple(x) :
    return x * 3

triple_num = list(map(triple, [1,2,3,4,5]))
print(triple_num)