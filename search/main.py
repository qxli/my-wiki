#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from search import Index

content = '../content'


def get_file_list(dir):
    for root, dirs, files in os.walk(dir):
        for filespath in files:
            yield os.path.join(root, filespath)

if __name__ == '__main__':
    idx = Index('index')
    f_list = get_file_list(content)
    for path in f_list:
        with open(path, 'r') as f:
            data = f.read()
            title = os.path.basename(path)
            idx.build(title, data, path)
