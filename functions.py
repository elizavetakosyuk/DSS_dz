def create_file(name_file):
    with open(name_file, 'w') as file:
        pass


def write_file(name_file, text, rewrite_existing: bool = True):
    accesss_mode = 'w' if rewrite_existing else 'a'
    with open(name_file, accesss_mode) as file:
        file.write(text)


def read_file(name_file):
    from os import path
    if path.isfile(name_file):
        with open(name_file, 'r') as file:
            text_file = file.read()
            return text_file
    else:
        print(f'Файла {name_file} не существует')


def remove_file(name_file):
    from os import remove, path

    if path.isfile(name_file):
        remove(name_file)
        print_text = f'Файл {name_file} удалён'
    else:
        print_text = f'Файла {name_file} не существует'

    return print_text


def write_json(name_file, data, rewrite_existing: bool = True):
    import json
    accesss_mode = 'w' if rewrite_existing else 'a'
    with open(name_file, accesss_mode) as file:
        json.dump(data, file)


def read_json(name_file):
    import json
    from os import path
    if path.isfile(name_file):
        with open(name_file, 'r') as file:
            data = json.load(file)
            return data
    else:
        print(f'Файла {name_file} не существует')


def parse_xml(name_file):
    import xml.etree.ElementTree as ET
    tree = ET.parse(name_file)
    root = tree.getroot()

    print(f'Количество узлов в корне {len(root)}')

    for elem in root:
        print(elem.attrib['name'])
        for subelem in elem:
            print('\t', subelem.tag, subelem.text)
        print()
    return tree


def create_obj_xml(name, in_price, in_date):
    import xml.etree.ElementTree as ET
    pos = ET.Element('Pos')
    price = ET.SubElement(pos, 'price')
    date = ET.SubElement(pos, 'date')
    pos.set('name', name)
    price.text = in_price
    date.text = in_date
    return pos


def write_xml(name_file, tree, rewrite_existing: bool = True):
    accesss_mode = 'wb' if rewrite_existing else 'ab'
    with open(name_file, accesss_mode) as file:
        tree.write(file)


def add_new_obj_xml(xml_tree):
    import xml.etree.ElementTree as ET
    pos = xml_tree.getroot()

    # Записать в файл новые данные из консоли.
    print(f'Добавим новый элемент')
    name = input("Введите названи позиции: ")  # 'tort'
    price = input("Введите цену: ")  # '25'
    date = input("Введите срок хранения: ")  # '08'
    new_pos = create_obj_xml(name, price, date)

    pos.append(new_pos)

    new_tree = ET.ElementTree(pos)
    return new_tree


def create_zip(path, name_zip):
    import os
    import zipfile
    file_dir = os.listdir(path)

    with zipfile.ZipFile(name_zip, mode='w') as zf:
        for file in file_dir:
            add_file = os.path.join(path, file)
            zf.write(add_file)

    os.system(f'file {name_zip}')


def add_file_in_zip(name_zip):
    import zipfile
    from tkinter import filedialog as fd
    path = fd.askopenfile()
    path = path.name.replace('/', '\\')
    new_name_file = path[path.rfind('\\') + 1:]

    with zipfile.ZipFile(name_zip, mode='a') as zf:
        zf.write(path, arcname=new_name_file)

    return new_name_file


def get_list_file_in_zip(name_zip):
    import zipfile
    with zipfile.ZipFile(name_zip) as zf:
        zf.printdir()


def extract_file(name_zip, name_file):
    import zipfile
    with zipfile.ZipFile(name_zip, 'r') as zf:
        zf.extract(name_file, '.')


def get_info_file(path):
    from pathlib import Path

    p = Path(path)
    print('Информациия о файле:\n', p.stat())
