# напиши модуль для реализации секундомера
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.properties import BooleanProperty

class Seconds(Label):
    done = BooleanProperty(False)
    def __init__(self, total, **kwargs):
        self.done = False
        self.total = total
        self.curent = 0
        my_text = 'Прошло секунд: ' + str(self.curent)
        super().__init__(text = '[size=20]' + '[b]' + '[color=#5baf16]' + my_text + '[/color]' + '[/b]' + '[/size]', markup = True, size_hint = (1, 0.2), pos_hint={'center_x': 0.5})
    def restart(self, total, **kwargs):
        self.done = False
        self.total = total
        self.curent = 0
        self.text = ('[size=20][b][color=#5baf16]Прошло секунд: ' + str(self.curent) + '[/color][/b][/size]')
        self.start()
    def start(self):
        Clock.schedule_interval(self.change, 1)

    def change(self, dt):
        self.curent += 1
        self.text = ('[size=20]'+'[b]'+'[color=#5baf16]' + 'Прошло секунд: ' + str(self.curent) + '[/color]'+'[/b]'+'[/size]')
        if self.curent >= self.total:
            self.done = True
            return False