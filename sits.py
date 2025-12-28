# напиши модуль для подсчета количества приседаний
from kivy.uix.label import Label

class Sits(Label):
    def __init__(self, total, **kwargs):
        self.curent_sits = 0
        self.total_sits = total
        my_text = ('[size=20][b][color=#5baf16]Осталось приседаний: ' + str(self.total_sits)  + '[/color][/b][/size]')
        super().__init__(text = '[size=20]' + '[b]' + '[color=#5baf16]' + my_text + '[/color]' + '[/b]' + '[/size]', markup = True, **kwargs)
    def next(self, *args):
        self.curent_sits += 1
        remain = max(0, self.total_sits - self.curent_sits)
        self.text = ('[size=20][b][color=#5baf16]Осталось приседаний: ' + str(remain)  + '[/color][/b][/size]')