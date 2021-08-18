""" Модуль содержит тесты заездов разного вида, с разными направлениями
с разными сценариями, разными протоколами и курсами. Описани каждого кейса
прилагается.
Каждая функция - взвешивание. Названия взвешивания генерируются таким образом:
 test_{litter}_{protocol}_{course}_{stage}
 где
 litter - Буква, что бы добиться выполнения тестов по порядку (a,b,c,d)
 protocol - протокол авто (ТКО, Tails, NEG и т.д.),
 course - направление, с которого подъехало авто (external\internal),
 stage - что взвешивает авто в данный момент, брутто или тара (gross/tare)

 Гос. номера для заездов подбираются рандомом.
 По итогу тестов заезды удаляются.
 """

import unittest
import time
from gc_qdk.main import GCoreQDK
from gc_qdk.tests.round_tests import functions
from gc_qdk.tests.round_tests import situations
from qdk.main import QDK
from gc_qdk.tests.round_tests import response_operators
from gc_qdk.tests.round_tests import cfg


class MyTestCase(unittest.TestCase):
    """ Кастомный TestCase """
    def __init__(self, *args, **kwargs):
        super(MyTestCase, self).__init__(*args, **kwargs)
        funcs_dict = {'round_status':
                          {'method': response_operators.main_response_operator}
                      }
        self.qdk = GCoreQDK('192.168.100.118', 4455, only_show_response=False,
                            start_resp_operator=funcs_dict)
        self.qdk.make_connection()

        #self.weight_qdk = QDK('192.168.100.118', 2292)
        #self.weight_qdk.make_connection()


    @functions.set_situation('normal_round')
    @functions.waiter
    def test_a_tails_external_gross(self, course='external', choose_mode='auto',
                                  dlinnomer=False, polomka=False,
                                  trash_cat=1):
        """ Самый типовой въезд. Машина с ТКО въезжает на территорию и 
        взвешивает брутто """
        a_car_num = functions.get_random_carnum()
        cfg.a_car_num = a_car_num
        functions.start_round(self.qdk, course=course,
                              car_choose_mode=choose_mode,
                              dlinnomer=dlinnomer, polomka=polomka,
                              trash_cat=trash_cat, car_num=cfg.a_car_num)
        self.qdk.start_response_operator()
        self.qdk.subscribe()

    @functions.set_situation('normal_round')
    @functions.waiter
    def test_b_tails_internal_tare(self, course='internal',
                                  choose_mode='auto',
                                  dlinnomer=False, polomka=False,
                                  trash_cat=1):
        """ Самый типовой въезд. Машина с ТКО въезжает на территорию и
        взвешивает брутто """
        functions.start_round(self.qdk, course=course,
                              car_choose_mode=choose_mode,
                              dlinnomer=dlinnomer, polomka=polomka,
                              trash_cat=trash_cat, car_num=cfg.a_car_num)


if __name__ == '__main__':
    unittest.main()
