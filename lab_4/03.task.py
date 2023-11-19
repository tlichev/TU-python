letters = list(input())
output = {}

letters_set = set(letters)

for letter in letters_set:
    output[letter] = letters.count(letter)
sorted_dict = dict(sorted(output.items()))

[print(f"{k}:{v}", end="  ") for k, v in sorted_dict.items()]
