def change_elements(num_list, n):

    for i in range(len(num_list)):
        if num_list[i] > n:
            num_list[i] = 0

number_list = [2,3,43,53,242,12,3,4325,64]
num = 12

change_elements(number_list, num)
print(", ".join(map(str, number_list)))