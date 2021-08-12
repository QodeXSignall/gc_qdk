.. _rst-markup-label:

Реестр методов
==============
Начало взвешивания
--------------

.. code-block:: python
   :emphasize-lines: 1-3,5

   def start_round(self, car_number: str, course: str, car_choose_mode: str,
                dlinnomer: bool = False, polomka: bool = False,
                carrier: int = None, trash_cat: int = None,
                trash_type: int = None, notes: str = None,
                operator: int = None, duo_polygon: int = None):

Отдать команду на начало процедуры  (раунда) взвешивания.

.. note::
    Имейте в виду, что система может в отдельный момент времени обрабатывать только один заезд. При попытке отправить эту команду во время исполнения другой процедуры, будет возвращена ошибка.

:param car_number: Гос. номер, в строковом представлении, типа "A111AA702"
:param course: Направление, с какой стороны стоит машина (external/internal)
:param car_choose_mode: Спсособ инициации заезда (auto/manual):
    если auto - значит система сама увидела машину,
    если manual - значит заезд инициируют вручную
:param dlinnomer: Спец. проткол "Длинномер" (True/False)
:param polomka: Спец. протокол "Поломка" (True/False)
:param carrier: ID перевозчика
:param trash_cat: ID категории груза
:param trash_type: ID вида груза
:param notes: Комментарий весовщика
:param operator: ID весовщика
:param duo_polygon: ID объекта, принимающего груз
