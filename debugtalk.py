'''
@Author: gq.guo
@Date: 2020-07-24 22:56:58
LastEditors: gq.guo
LastEditTime: 2020-08-06 17:33:46
@Description: file content
'''

import os
import sys
import time
import csv
import json

import yaml
import requests
from loguru import logger

base_path = os.getcwd()
config_file = os.listdir(os.path.join(base_path, 'config'))[0]
file_path = os.path.join(base_path, 'config', config_file)
with open(file_path, 'r') as f:
        # print(f.readlines())
    yaml_data = yaml.safe_load(f)

def get_test_file(file_name: str, file_dir: str = None) -> str:
    base_path = os.getcwd()
    file_path = os.path.join(base_path, file_dir, file_name)
    return file_path


def get_base_url(key: str = 'test') -> str:
        # print(datas)
        return yaml_data.get('base_url').get(key)


def get_slack_channel(channel: str):
    return yaml_data.get('slack').get(channel)


def sleep(n_secs):
    time.sleep(n_secs)
    # time.sleep(n_secs)


def get_test_data(file_name, file_dir, key=None,connection_id=None):
    """
    @description:
    @param {type}
    @return:
    """
    file_path = get_test_file(file_name, file_dir)
    if not os.path.exists(file_path):
        raise FileExistsError("test data NOT FOUND,pls check!!!")
    with open(file_path, 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            if key == row[0]:
                # print(key, '--->', row[1])
                try:
                    data = json.loads(row[1])
                    if connection_id:
                        data['connection']['id'] = connection_id
                    return data
                except json.JSONDecodeError:
                    return row[1]


def get_shop_domain(ecommerce: str) -> str:
    return yaml_data.get(ecommerce).get('domain')


def create_order(file_name, file_dir, key, ecommerce):
    domain = get_shop_domain(ecommerce)
    url = "{}/orders.json".format(domain)
    data = get_test_data(file_name=file_name,file_dir=file_dir,key=key)
    headers = {
        "X-Shopify-Access-Token":os.environ[ecommerce]
    }
    response = requests.post(url,json=data,headers=headers)
    order_id = response.json()['order']['id']
    return str(order_id)


def str_params(params):
    return str(params)

    
if __name__ == "__main__":
    # print(get_value(('base_url', 'test')))
    # post_params = get_test_data('connections.csv', 'testdata', 'post_pass')
    # print(post_params)
    id = create_order('orders.csv','testdata','order_pass','shopify')
    print(id)