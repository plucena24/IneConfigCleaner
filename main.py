import os
import re

file_name = re.compile(r"[rs]w?\d\d?\.txt")

def file_ext_renamer(path, new_ext):
    for fn in os.listdir(path):
        full_name = os.path.join(path, fn)
        if not os.path.isfile(full_name) or file_name.search(full_name):
            continue
        new_name1 = full_name.replace('-confg', '.txt')
        new_name2 = full_name.replace('-confg.txt', '.txt')
        if full_name.endswith('-confg.txt'):
            os.rename(full_name, new_name2)
        else:
            os.rename(full_name, new_name1)


def things_to_change(change_items, path):
    os.chdir(path)
    _files_in_dir = os.listdir(os.curdir)
    for _file in _files_in_dir:
        with open(_file, 'r') as fi:
            content = fi.read()

        for k, v in change_items.iteritems():
            if k in content:
                content = content.replace(k, v)
            else:
                continue

        with open(_file, 'w') as fo:
            fo.write(content)


if __name__ == '__main__':

    dir_path = r'C:/foundation.lab.final.configs.finished'

    change = {'version ': 'enable\nconfigure terminal\nversion ', 'interface GigabitEthernet1\n ip address dhcp\n': 'interface GigabitEthernet1\n no shutdown\n', 'interface Vlan1\n ip address dhcp': 'interface Vlan1\n no shutdown'}

    file_ext_renamer(dir_path, '.txt')
    things_to_change(change, dir_path)






