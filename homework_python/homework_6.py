# ===Задача 42.===
# Реализовать RLE алгоритм. Реализовать модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах

def get_data_from_file(link):
    data = open(link, 'r')
    in_str = data.read()
    data.close()
    return in_str


def push_encode_file(str, link):
    with open(link, 'w') as data:
        data.write(str)


def rle_encode(data):
    encode = ''
    pr_char = ''
    count = 1

    if not data:
        return ''
    for char in data:
        if char != pr_char:
            if pr_char:
                encode += str(count) + pr_char + ' '
            count = 1
            pr_char = char
        else:
            count += 1
    encode += str(count) + pr_char + ' '
    return encode


def rle_decode(data):
    decode = ''
    count = ''
    i = 0
    while i <= (len(data)-1):
        count += data[i]
        if data[i] == ' ':
            decode += data[i - 1] * int(count[:-2])
            count = ''
        i += 1
    return decode


inp_link = '/Users/igor/Desktop/belive/study_projects/HelloPython/homework_python/files_homework_tasks/task_42_input_data.txt'
out_link = '/Users/igor/Desktop/belive/study_projects/HelloPython/homework_python/files_homework_tasks/task_42_outputs_data.txt'

inp_data = get_data_from_file(inp_link)
code = rle_encode(inp_data)
push_encode_file(code, out_link)

print(inp_data)
print(code)
print(rle_decode(code))
