# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
#
# print(add(4, 6, 9))

def calculate(**kwargs):
    # print(type(kwargs))
    for key, value in kwargs.items():
        print(key)
        print(value)


calculate(add=3, multiply= 5)