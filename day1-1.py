with open("adventofcode22/input1-1.txt") as text_file:
    list_of_food = []
    summed_list_of_food = []
    temp_list = []
    for line in text_file:
        stripped_lines = line.strip()
        if not stripped_lines == '':
            temp_list.append(int(stripped_lines))
        if stripped_lines == '':
            list_of_food.append(temp_list)
            summed_list_of_food.append (sum(temp_list))
            temp_list = []

print(summed_list_of_food)
print(max(summed_list_of_food))
miniListe = sorted((summed_list_of_food),reverse=True)[:3]
print(sum(miniListe))

# elf_number = [None]*len(summed_list_of_food)

# for i in range (len(summed_list_of_food)):
#     elf_number[i]=i+1

# print (elf_number)

# paired_list = zip(summed_list_of_food, elf_number)
# print(sorted(zip(summed_list_of_food, elf_number),reverse=True)[:3])

# for i in paired_list:
#     print(i)

# print(sorted((paired_list)))