from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
#from kivy.uix.floatlayout import FloatLayout

Window.size = (500,700)

Builder.load_file('calc.kv')

class MyLayout(Widget):
    def clear(self):
        self.ids.output.text = '0'

    def number(self, num)    :
        out = self.ids.output.text
        if out == "SyntaxError":
            self.ids.output.text = num
        elif out != "0":
            self.ids.output.text = out+num
        else:
            if num == ".":
                self.ids.output.text = out+num
            else:
                self.ids.output.text = num

    def back(self):
        equ = self.ids.output.text
        equ = equ[:-1]
        self.ids.output.text = equ

    def negative(self):
        str = self.ids.output.text
        if str[0] == "-":
            self.ids.output.text = str[1:]
        elif str[0] == "+":
            self.ids.output.text = "-"+str[1:]
        else:
            self.ids.output.text = "-"+str

    def equal(self):
        num = self.ids.output.text
        #length = len(num)
        try:
            #self.ids.output.text = str(int(eval(num)))
            self.ids.output.text = str(eval(num))
        except:
            self.ids.output.text = "SyntaxError"


class _App(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    _App().run()
