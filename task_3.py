import os


class File:
    all_files = []

    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.count = 0
        self.all_files.append(self)

    def get_count_str(self):
        count = 0
        with open(self.path, 'r', encoding='utf-8') as f:
            for line in f:
                count += 1
        self.count = count


def glue_files():
    all_count_str = []
    for file in File.all_files:
        all_count_str.append(file.count)
    all_count_str.sort()
    file_path_result = os.path.join(os.getcwd(), 'result.txt')
    with open(file_path_result, 'w', encoding='utf-8') as f_write:
        for count in all_count_str:
            for value in File.all_files:
                if value.count == count:
                    f_write.write(value.name + '\n')
                    f_write.write(str(value.count) + '\n')
                    with open(value.path, 'r', encoding='utf-8') as f_read:
                        for line in f_read:
                            f_write.write(line)


def file_name_path(file_list):
    for file in files:
        file_path = os.path.join(os.getcwd(), file)
        file_new = File(file, file_path)
        for file in File.all_files:
            file.get_count_str()


files = ['1.txt', '2.txt', '3.txt']
file_name_path(files)
glue_files()