import PyQt5.QtWidgets as qtw
import random
import string


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Password Generator')
        self.setLayout(qtw.QVBoxLayout())
        self.keypad()
        self.setGeometry(120,120,200,75)

        self.show()

    def keypad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        self.result_field = qtw.QLineEdit()
        gen_btn = qtw.QPushButton('Generate', clicked = self.final_password)

        container.layout().addWidget(self.result_field,0,0,1,3)
        container.layout().addWidget(gen_btn,2,1)
        self.layout().addWidget(container)

    def numpass(self):# Generates random numbers.
        random_num = random.sample(range(0,9), 6)
        return list(map(str, random_num))

    def letterpass(self):# Genrates random uppercase and lowercase letters.
        letters = string.ascii_letters
        random_string = ''.join(random.choice(letters) for i in range(7))
        return list(random_string)

    def symbol(self):# Selects random symbol from symbols list.
        symbols = ['!','@','#','%','&','*','(',')']
        random_symbol = random.choice(symbols)
        return list(random_symbol)

    def final_password(self):# Combines and randomises each function into a single string.
        li = (self.numpass()+self.letterpass()+self.symbol())
        random.shuffle(li)
        final_string = ''.join(str(i) for i in li)
        self.result_field.setText(final_string)
        

app = qtw.QApplication([])
mw = MainWindow()
app.setStyle(qtw.QStyleFactory.create('Fusion'))
app.exec_()
