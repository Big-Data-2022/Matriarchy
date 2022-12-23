# def main(x, y):
#     return x+y
# print(main(1,1))

# l = lambda x, y: x+y
# print(l(1, 1))

# l = lambda *a: a
# print(l(1,2,3,4,5,6,7,8,9))

# l = lambda *a: set(a)
# print(l(1,2,3,4,5,6,7,8,9))

#____________no work
# def calculate(num, num2):
#     while True:
#         num = int(input("num1 "))
#         num2 = int(input("num2 "))
#         table = input("""
#         +   1
#         -   2
#         *   3
#         /   4
#         //  5
#         **  6
#         >:""")
#         if table == "1":
#             rez = lambda x, y: x+y
#             print(rez(num, num2))
#         elif table == "2":
#             rez = lambda x, y: x-y
#             print(rez(num, num2))
#         elif table == "3":
#             rez = lambda x, y: x*y
#             print(rez(num, num2))
#         elif table == "4":
#             rez = lambda x, y: x/y
#             print(rez(num, num2))
#         elif table == "5":
#             rez = lambda x, y: x//y
#             print(rez(num, num2))
#         elif table == "6":
#             rez = lambda x, y: x**y
#             print(rez(num, num2))
# calculate(int(input("num1 ")), int(input("num2 ")))
#________________


#________________
# a = [1,2,3,4]
# l = list(map(lambda x: x*x, a))
# print(l)
#________________

# l = list(filter(lambda x: x % 2 == 0, [1,2,3,4]))
# print(l)

#_________________

# def main(lists):
#     for i in range(0, len(lists)):
#         for f in range(i, len(lists)):
#             if (lists[i] % 2 == 1 and lists[f] % 2 == 1):
#                 if (lists[f] < lists[i]):
#                     num = lists[i]
#                     lists[i] = lists[f]
#                     lists[f] = num
#     return lists

# print(main([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))

#____________________

