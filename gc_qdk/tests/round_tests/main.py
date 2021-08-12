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
from gc_qdk.main import GCoreQDK
from gc_qdk.tests.round_tests import functions


class MyTestCase(unittest.TestCase):
    """ Кастомный TestCase """
    def __init__(self, *args, **kwargs):
        super(MyTestCase, self).__init__(*args, **kwargs)
        self.qdk = GCoreQDK('192.168.100.118', 4455)

    def test_litter_tko_internal_gross(self):
        """ Самый типовой въезд. Машина с ТКО въезжает на территорию и 
        взвешивает брутто """
        functions.start_round(self.qdk, 'external', 'auto', dlinnomer=False,
                              polomka=False, trash_cat=1)

