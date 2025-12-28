# напиши здесь свое приложение
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from instructions import *
from ruffier import *
from seconds import *
from kivy.core.window import Window
from runner import *
from sits import *
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup

Window.clearcolor = '#ace5a3'
def check_inst(str_num):
    try:
        return int(str_num)
    except:
        return False 
name = ''
age = 0
result_1 = 0
result_2 = 0
result_rest = 0
color = '#5e7cbe'
class MainScr(Screen):
    def __init__(self, name='main'):
        super().__init__(name=name)
        self.text1 = Label(text = '[size=19]' + '[b]' + '[color=#5e7cbe]' + txt_instruction + '[/color]' + '[/b]' + '[/size]', markup = True, size_hint_y=None, font_size='24sp', halign = 'center', valign='top')
        self.scroll = ScrollView(size_hint=(1, 1), pos_hint={'center_x': 0.52})
        self.scroll.add_widget(self.text1)
        self.text1.bind(size = self.resize)
        self.popup = Popup(title='Внимание!!', size_hint=(None, None), size=(400, 300), content=Label(text='[b]' + '[color=#ef453f]' + 'Введите целое и положительное число,\n и возраст от 7 лет' + '[/b]', markup = True))
        text_name = Label(text = '[b]' + '[color=#5e7cbe]' + 'Введите  имя -' + '[/color]' + '[/b]', markup = True)
        text_age = Label(text = '[b]' + '[color=#5e7cbe]' + 'Введите возраст -' + '[/color]' + '[/b]', markup = True)
        self.name1 = TextInput(halign='center', multiline=False, size_hint=(0.9, 0.96))
        self.age1 = TextInput(halign='center', multiline=False, size_hint=(0.9, 0.96))
        photo = Image(source='helth_photo.png', size_hint=(0.2, 0.2), pos_hint={'center_x': 0.25})
        button_start = Button(text = 'Начать', size_hint=(0.7, 0.9), background_color = color)
        self.except_lable = Label(text= '', markup = True, size_hint=(1, 0.14), pos_hint={'center_x': 0.7})
        l_layout = BoxLayout(orientation = 'vertical')
        h_layout1 = BoxLayout(size_hint=(0.95, 0.1), padding = 4)
        h_layout2 = BoxLayout(size_hint=(0.95, 0.1), padding = 4)
        h_layout3 = BoxLayout(size_hint = (0.4, 0.2), pos_hint={'center_x': 0.5})
        l_layout.add_widget(self.scroll)
        l_layout.add_widget(photo)
        h_layout1.add_widget(text_name)
        h_layout1.add_widget(self.name1)
        h_layout2.add_widget(text_age)
        h_layout2.add_widget(self.age1)
        h_layout3.add_widget(button_start)
        l_layout.add_widget(self.except_lable)
        l_layout.add_widget(h_layout1)
        l_layout.add_widget(h_layout2)
        l_layout.add_widget(h_layout3)
        self.add_widget(l_layout)
        button_start.on_press = self.transport

    def resize(self, *args):
        self.text1.text_size = (self.text1.width, None)
        self.text1.texture_update()
        self.text1.height = self.text1.texture_size[1]
    def transport(self):
        global name, age
        name = self.name1.text
        age = check_inst(self.age1.text)
        if age == False or age <= 0: 
            self.except_lable.text = '[b]' + '[color=#ef453f]' + 'Введите целое и положительное число' + '[/b]'
            self.popup.open()
        else:
            self.manager.current = 'screen1'

class FirstScreen(Screen):
    def __init__(self, name='screen1'):
        super().__init__(name=name)
        self.lbl_sec = Seconds(1)
        self.lbl_sec.bind(done = self.sec_finished)
        self.text1 = Label(text = '[size=21]' + '[b]' + '[color=#5e7cbe]' + txt_test1 + '[/color]' + '[/b]', markup = True, size_hint_y=None, font_size='24sp', halign = 'center', valign='top')
        self.scroll = ScrollView(size_hint=(1, 0.7), pos_hint={'center_x': 0.51})
        self.scroll.add_widget(self.text1)
        self.text1.bind(size = self.resize)
        self.popup = Popup(title='Внимание!!', size_hint=(None, None), size=(400, 300), content=Label(text='[b]' + '[color=#ef453f]' + 'Введите целое и положительное число' + '[/b]', markup = True))
        text_name = Label(text = '[b]' + '[color=#5e7cbe]' + 'Введите результат -' + '[/color]' + '[/b]', markup = True,)
        self.pulse = TextInput(halign='center', multiline=False, size_hint=(1, 0.9))
        self.pulse.disabled = True
        self.button_start = Button(text = 'Начать', size_hint=(0.5, 0.8), background_color = color)
        self.except_lable = Label(text='', markup = True, size_hint=(1, 0.1), pos_hint={'center_x': 0.73}) 
        l_layout = BoxLayout(orientation = 'vertical', padding=100)
        h_layout1 = BoxLayout(size_hint=(0.95, 0.1), padding = 4, pos_hint={'center_x': 0.5})
        h_layout3 = BoxLayout(size_hint = (0.4, 0.2), pos_hint={'center_x': 0.5})
        l_layout.add_widget(self.scroll)
        h_layout1.add_widget(text_name)
        h_layout1.add_widget(self.pulse)
        h_layout3.add_widget(self.button_start)
        l_layout.add_widget(self.lbl_sec)
        l_layout.add_widget(self.except_lable)
        l_layout.add_widget(h_layout1)
        l_layout.add_widget(h_layout3)
        self.add_widget(l_layout)
        self.button_start.on_press = self.transport
    def sec_finished(self, *args):
        self.pulse.disabled = False
        self.button_start.disabled = False
        self.button_start.text = 'Продолжить'
        self.button_start.background_color = '#01ff00'
    def resize(self, *args):
        self.text1.text_size = (self.text1.width, None)
        self.text1.texture_update()
        self.text1.height = self.text1.texture_size[1]
    def transport(self):
        if self.lbl_sec.done == False:
            self.button_start.disabled = True
            self.lbl_sec.start()        
        else:
            global result_1
            result_1 = check_inst(self.pulse.text)
            if result_1 == False or age <= 0:
                self.except_lable.text = '[b]' + '[color=#ef453f]' + 'Введите целое и положительное число' + '[/b]'
                self.popup.open()
            else:
                self.manager.current = 'screen2'

class SecondScreen(Screen):
    def __init__(self, name='screen2'):
        super().__init__(name=name)
        self.sits = Sits(5, pos_hint={'center_x': 1, 'center_y': 0.65}) 
        self.runner = Runner(5, 1.5, size_hint=(0.6, 1), pos_hint={'center_x': 0.5, 'center_y': 0.7})
        self.runner.bind(finished = self.finish)
        self.text1 = Label(text = '[size=19]' + '[b]' + '[color=#5e7cbe]' + txt_test2 + '[/color]' + '[/b]' + '[/size]', markup = True, pos_hint={'center_x': 0.49}, size_hint_y=None, font_size='24sp', halign = 'center', valign='top')
        self.scroll = ScrollView(size_hint=(1, 1), pos_hint={'center_x': 0.47})
        self.scroll.add_widget(self.text1)
        self.text1.bind(size = self.resize)
        self.button_start = Button(text = 'Начать', size_hint=(0.38, 0.3), pos_hint={'center_x': 0.5}, background_color = color)
        l_layout = BoxLayout(orientation = 'vertical', padding = 100)
        h_layout1 = BoxLayout(size_hint = (0.8, 1), pos_hint={'center_x': 0.65})
        l_layout.add_widget(self.scroll)
        h_layout1.add_widget(self.sits)
        h_layout1.add_widget(self.runner)
        l_layout.add_widget(h_layout1)
        l_layout.add_widget(self.button_start)
        self.add_widget(l_layout)
        self.button_start.on_press = self.transport
    def finish(self, *args):
        self.button_start.disabled = False
        self.button_start.text = 'Продолжить'
    def resize(self, *args):
        self.text1.text_size = (self.text1.width, None)
        self.text1.texture_update()
        self.text1.height = self.text1.texture_size[1]
    def transport(self):
        if self.runner.value == 0:
            self.button_start.disabled = True
            self.runner.start()
            self.runner.bind(value = self.sits.next)
        else:
            self.manager.current = 'screen3'

class ThirdScreen(Screen):
    def __init__(self, name='screen3'):
        super().__init__(name=name)
        self.stage = 0
        self.text1 = Label(text = '[size=19]' + '[b]' + '[color=#5e7cbe]' +  txt_test3 + '[/color]' + '[/b]' + '[/size]', markup = True, size_hint_y=None, font_size='24sp', halign = 'center', valign='top')
        self.scroll = ScrollView(size_hint=(1, 1), pos_hint={'center_x': 0.5})
        self.scroll.add_widget(self.text1)
        self.text1.bind(size = self.resize)
        self.popup = Popup(title='Внимание!!', size_hint=(None, None), size=(400, 300), content=Label(text='[b]' + '[color=#ef453f]' + 'Введите целое и положительное число' + '[/b]', markup = True))
        before_rest = Label(text = '[b]' + '[color=#5e7cbe]' +  'Результат' + '[/color]' + '[/b]', markup = True)
        after_rest = Label(text = '[b]' + '[color=#5e7cbe]' +  'Результат после отдыха' + '[/color]' + '[/b]', markup = True)
        self.name1 = TextInput(halign='center', multiline=False, size_hint = (1, 1.5))
        self.age1 = TextInput(halign='center', multiline=False, size_hint = (1, 1.1))
        self.name1.disabled = True
        self.age1.disabled = True
        self.button_start = Button(text = 'Начать', background_color = color)
        self.except_lable = Label(text='', markup = True, size_hint=(1, 0.2), pos_hint={'center_x': 0.73})
        self.lbl_sec = Seconds(1)
        self.lbl_sec.bind(done = self.sec_finished)
        l_layout = BoxLayout(orientation = 'vertical', padding = 85)
        h_layout1 = BoxLayout(size_hint=(0.95, 0.1), padding = 4)
        h_layout2 = BoxLayout(size_hint=(0.95, 0.1), padding = 4)
        h_layout3 = BoxLayout(size_hint = (0.4, 0.2), pos_hint={'center_x': 0.5})
        l_layout.add_widget(self.scroll)
        h_layout1.add_widget(before_rest)
        h_layout1.add_widget(self.name1)
        h_layout2.add_widget(after_rest)
        h_layout2.add_widget(self.age1)
        h_layout3.add_widget(self.button_start)
        l_layout.add_widget(self.lbl_sec)
        l_layout.add_widget(self.except_lable)
        l_layout.add_widget(h_layout1)
        l_layout.add_widget(h_layout2)
        l_layout.add_widget(h_layout3)
        self.add_widget(l_layout)
        self.button_start.on_press = self.transport
    def sec_finished(self, *args):
        if self.lbl_sec.done:
            if self.stage == 0:
                self.stage = 1
                self.lbl_sec.restart(1)
                self.name1.disabled = False
            elif self.stage == 1:
                self.stage = 2
                self.lbl_sec.restart(1) 
            elif self.stage == 2:
                self.age1.disabled = False
                self.name1.disabled = False
                self.button_start.disabled = False
                self.button_start.text = 'Завершить'
                self.button_start.background_color = '#01ff00'
    def resize(self, *args):
        self.text1.text_size = (self.text1.width, None)
        self.text1.texture_update()
        self.text1.height = self.text1.texture_size[1]
    def transport(self):
        if self.lbl_sec.done == False:
            self.button_start.disabled = True
            self.lbl_sec.start()

        else:
            global result_2, result_rest
            result_2 = check_inst(self.name1.text)
            result_rest = check_inst(self.age1.text)
            if result_2 == False or result_1 <= 0:
                self.except_lable.text = ('[size=19]' + '[b]' + '[color=#ef453f]' + 'Введите целое и положительное число' + '[/color]' + '[/b]' + '[/size]')
                self.popup.open()
            elif result_rest == False or result_rest <= 0:
                self.except_lable.text = ('[size=19]' + '[b]' + '[color=#ef453f]' + 'Введите целое и положительное число' + '[/color]' + '[/b]' + '[/size]')
                self.popup.open()
            else:
                self.manager.current = 'screen4'
class FothScreen(Screen):
    def __init__(self, name='screen4'):
        super().__init__(name=name)
        self.final_text = Label(text = '[size=18]' + '[b]' + '[color=#5e7cbe]' + 'Ваше имя: ' + '[/color]' + '[/b]' + '[/size]', markup = True)
        self.ruffier_text = Label(text = '[size=18]' + '[b]' + '[color=#5e7cbe]' + txt_workheart + '[/color]' + '[/b]' + '[/size]', markup = True)
        self.ruffier_index = Label(text = '[size=18]' + '[b]' + '[color=#5e7cbe]' + txt_index + '[/color]' + '[/b]' + '[/size]', markup = True)
        l_layout = BoxLayout(orientation = 'vertical', size_hint=(0.5, 0.13), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        l_layout.add_widget(self.final_text)
        l_layout.add_widget(self.ruffier_index)
        l_layout.add_widget(self.ruffier_text)
        self.add_widget(l_layout)
        self.on_enter =  self.show_results
    def show_results(self):
        ruffier_show = test(int(result_1), int(result_2), int(result_rest), int(age))
        ruffier_index_show = ruffier_index(int(result_1), int(result_2), int(result_rest))
        self.final_text.text += ('[u]' + '[size=18]' + '[b]' + '[color=#5baf16]' + name + '[/color]' + '[/b]' + '[/size]' + '[/u]')
        self.ruffier_text.text += ('[u]' + '[size=18]' + '[b]' + '[color=#5baf16]' + ruffier_show + '[/color]' + '[/b]' + '[/size]' + '[/u]')
        self.ruffier_index.text += ('[u]' + '[size=18]' + '[b]' + '[color=#5baf16]' + str(ruffier_index_show) + '[/color]' + '[/b]' + '[/size]' + '[/u]')
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr())
        sm.add_widget(FirstScreen())
        sm.add_widget(SecondScreen())
        sm.add_widget(ThirdScreen())
        sm.add_widget(FothScreen())
        
        return sm

app = MyApp()
app.run()