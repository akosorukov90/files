import os


def count_str(file_path):
    count = 0
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            count += 1
    file_count_str[file_path] = count


def glue_file(file_path):
    max_str = 0
    with open(file_path, 'w', encoding='utf-8') as f:
        for key, value in file_count_str.items():
            list_value.append(value)
            list_value.sort()
        print(list_value)



file_path_1 = os.path.join(os.getcwd(), '1.txt')
file_path_2 = os.path.join(os.getcwd(), '2.txt')
file_path_3 = os.path.join(os.getcwd(), '3.txt')
file_path_result = os.path.join(os.getcwd(), 'result.txt')
file_count_str = {}

count_str(file_path_1)
count_str(file_path_2)
count_str(file_path_3)
print(file_count_str)

glue_file(file_path_result)