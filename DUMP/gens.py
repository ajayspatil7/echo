import os
from itertools import chain
import sys


def generate_data_files():
    data_files = []
    data_dirs = ('ECHO_V1', 'ECHOV1_LOGS', 'README')
    for path, dirs, files in chain.from_iterable(os.walk(data_dir) for data_dir in data_dirs):
        install_dir = os.path.join(sys.prefix, 'share/echo/' + path)
        list_entry = (install_dir, [os.path.join(path, f) for f in files if not f.startswith('.')])
        data_files.append(list_entry)

    return data_files

print(generate_data_files())