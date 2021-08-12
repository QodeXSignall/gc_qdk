""" Тесты встроенного обработчика ответов от GCore. Выделен в отдельный файл,
поскольку в обычных тестах функционала, каждый ответ обрабатывается отдельно.
Здесь же, обработка будет полностью на плечах обработчика. """


import unittest
from gc_qdk.main import GCoreQDK


class ResOpTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(ResOpTest, self).__init__(*args, **kwargs)
        func_dict = {'get_status': self.get_status_operator}
        self.qdk = GCoreQDK('192.168.100.118', 4455,
                            start_resp_operator=func_dict)

    def get_status_operator(self, *args, **kwargs):
        return "RETURN MESSAGE"

    def test_get_status_operator(self):
        self.qdk.get_status()


if __name__ == '__main__':
    unittest.main()
