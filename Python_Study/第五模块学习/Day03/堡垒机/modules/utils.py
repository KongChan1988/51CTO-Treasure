#-*-coding:utf-8 -*-
# Author: D.Gray
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def print_err(msg, quit=False):
    '''

    :param msg:
    :param quit:
    :return:
    '''
    output = "\033[31;1mError: %s\033[0m" % msg
    if quit:
        exit(output)
    else:
        print(output)

def yaml_parser(yml_filename):
    '''
    yaml方法load yaml file and return
    :param yml_filename:
    :return:
    '''
    try:
        yaml_file = open(yml_filename, 'r')
        data = yaml.load(yaml_file)
        return data
    except Exception as e:
        print_err(e)