""" Модуль содержит декораторы, модуляторы различных ситуцаий.
По сути, они выполняют следующие функции:
1) Блокируют\Деблокируют фотоэлементы
2) Меняют показания на весах
В различных порядках, эмулируя различные ситуации"""


import time
from gc_qdk.tests.round_tests import functions
from gc_qdk.tests.round_tests import response_operators

def normal_entering(func):
    """ Декоратор, оборачивающий выполнение всех работ с точками доступа """
    def wrapper(*args, **kwargs):
        qdk = args[0].qdk
        weight_qdk = args[0].weight_qdk
        print(args, kwargs)
        print(dir(args[0]))
        response = func(*args, **kwargs)
        record_id = response['info']['record_id']
        time.sleep(10)
        qdk.block_external_photocell()
        qdk.get_data()
        time.sleep(3)
        qdk.unblock_external_photocell()
        qdk.get_data()
        time.sleep(4)
        functions.change_weight(weight_qdk, 500)
        functions.change_weight(weight_qdk, 1000)
        functions.change_weight(weight_qdk, 3540)
        functions.change_weight(weight_qdk, 7000)
        time.sleep(2)
        functions.change_weight(weight_qdk, 13240)
        time.sleep(10)
        functions.change_weight(weight_qdk, 7000)
        qdk.block_internal_photocell()
        qdk.get_data()
        time.sleep(3)
        qdk.unblock_internal_photocell()
        qdk.get_data()
        functions.change_weight(weight_qdk, '0')
        time.sleep(10)
        qdk.get_record_info(record_id=record_id)
        response = qdk.get_data()
        args[0].assertTrue(response['status'])
    return wrapper

def normal_entering_decorator(func):
    """ Декоратор, оборачивающий выполнение всех работ с точками доступа """
    def wrapper(*args, **kwargs):
        qdk = args[0].qdk
        weight_qdk = args[0].weight_qdk
        response = func(*args, **kwargs)
        time.sleep(10)
    return wrapper
