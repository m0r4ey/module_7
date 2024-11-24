# Позиционирование в файле

def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    s_dict = { }
    i = 1
    for _ in strings:
        s_dict[(i, file.tell())] = _
        file.write(f'{_}\n')
        i += 1
    file.close()
    return s_dict

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)