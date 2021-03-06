# -*- coding: utf8 -*-
__author__ = 'MR.wen'
import os
import yaml
import io


def _get_yaml():
    """
    解析yaml
    :return: s  字典
    """
    path = os.path.join(os.path.dirname(__file__) + '/ticket_config.yaml')
    f = io.open(path ,encoding='utf-8')
    s = yaml.load(f)
    f.close()
    return s.decode() if isinstance(s, bytes) else s


if __name__ == '__main__':
    print(_get_yaml())