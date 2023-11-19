
numbers = []
[numbers.append(i)for i in range(1,int(input("Please enter a number -> "))+1)]

output_dict = {}

for i in range(len(numbers)):
    output_dict[numbers[i]] = numbers[-(i+1)]


[print(f"{k}:{v}", end="  ") for k, v in output_dict.items()]


