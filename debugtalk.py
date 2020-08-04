'''
@Author: your name
@Date: 2020-07-24 22:56:58
@LastEditTime: 2020-08-03 15:30:38
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /automate_test_paltform/debugtalk.py
'''
import os
import sys
import time
import csv
import json

import yaml
from loguru import logger


def get_test_file(file_name: str, file_dir: str = None) -> str:
    base_path = os.getcwd()
    file_path = os.path.join(base_path, file_dir, file_name)
    return file_path


def get_value(key, file_path=None):
    """
    @description: get key-value form file given
    @param file_path: config files path
    @param {type} key: list or set of keys
    @return:
    """
    if file_path is None:
        base_path = os.getcwd()
        config_file = os.listdir(os.path.join(base_path, 'config'))[0]
        file_path = os.path.join(base_path, 'config', config_file)
    # print(file_path)
    with open(file_path, 'r') as f:
        # print(f.readlines())
        data = yaml.safe_load(f)
        # print(datas)
        return data.get(key[0]).get(key[1])


def get_base_url(key: str = 'test') -> str:
    base_path = os.getcwd()
    config_file = os.listdir(os.path.join(base_path, 'config'))[0]
    file_path = os.path.join(base_path, 'config', config_file)
    with open(file_path, 'r') as f:
        # print(f.readlines())
        data = yaml.safe_load(f)
        # print(datas)
        return data.get('base_url').get(key)


def sleep(n_secs):
    return n_secs * 10
    # time.sleep(n_secs)


def get_test_data(file_name, file_dir, key=None,connection_id=None):
    """
    @description:
    @param {type}
    @return:
    """
    file_path = get_test_file(file_name, file_dir)
    logger.info('file path:[{}]'.format(file_path))
    if not os.path.exists(file_path):
        raise FileExistsError("test data NOT FOUND,pls check!!!")
    with open(file_path, 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            if key == row[0]:
                # print(key, '--->', row[1])
                try:
                    data = json.loads(row[1])
                    logger.info('data ------>{}'.format(data))
                    if connection_id:
                        data['connection']['id'] = connection_id
                    logger.info('use data ---->{}'.format(data))
                    return data
                except json.JSONDecodeError as e:
                    logger.error(e)
                    logger.error('data error --.{}'.format('test'))
                    return row[1]

def response_process(response):
    if response.status_code == 200:
        # logger.error(response.text)
        data = json.loads(response.text)
        response.content = data
        logger.info('type is {}'.format(type(response.content)))
        logger.info('response body-->{}'.format(response.content))
        # return response.json()
        return response
    pass


if __name__ == "__main__":
    # print(get_value(('base_url', 'test')))
    post_params = get_test_data('connections.csv', 'testdata', 'post_pass')
    print(post_params)
