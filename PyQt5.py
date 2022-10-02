# Вводим строку из чисел и букв. По нажатию на первую кнопку в лэйбл передавать только буквы  одной строкой,
# а по нажатию на вторую кнопку вывести сумму всех цифр. По нажатию на третью кнопку вывести историю вывода
# (т.е. у нас есть строка и при нажатии на 1 или 2 кнопку записывать в историю результаты разбора строки)
# Также есть второй лэйбл. Выводить в первый или второй лэйбл информацию по нажатию на кнопку с текстовой меткой.

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QRadioButton, QLabel


class Main(QMainWindow):  # наследуем класс Main от QMainWindow
    def __init__(self):
        self.mem = []  # делаем список памяти
        super(Main, self).__init__()  # вызываем конструктор с класса QMainWindow

        self.setFixedSize(500, 600)  # Размер нашего окна
        self.setWindowTitle('Python3')  # Название нашего окна

        self.ll = QLineEdit(self)  # Наше окно для записи
        self.ll.move(10, 10)  # Её положение в основном окне

        self.sth = QPushButton('1 But', self)  # помещаем окно 1 But на экране и устанавливает его размер
        self.sth.setGeometry(100, 100, 75, 75)
        self.sth.clicked.connect(self.add_w_label)  # при нажатии 1 But обращаемся к функции add_label

        self.sth2 = QPushButton('2 But', self)
        self.sth2.setGeometry(100, 200, 75, 75)  # Размер нашей кнопки 75x75 и отступ в окне по Х=100 и по Y=200
        self.sth2.clicked.connect(self.add_i_label)

        self.sth3 = QPushButton('3 But', self)
        self.sth3.setGeometry(100, 300, 75, 75)
        self.sth3.clicked.connect(self.all_label)  # при нажатии 3 But обращаемся к функции all_label

        self.rb = QRadioButton('Button 1', self)  # QRadioButton представляет выбираемую кнопку с текстовой меткой
        self.rb.move(50, 50)

        self.rb2 = QRadioButton('Button 2', self)
        self.rb2.move(150, 50)

        self.ql = QLabel('Label 1', self)  # QLabel используется для отображения текста или рисунка.
        self.style = 'border:2px solid black'  # граница нашей label оформлена черным
        self.ql.setStyleSheet(self.style)
        self.ql.setGeometry(200, 100, 75, 400)  # помещаем окно Label на экране и устанавливает его размер.
        # Первые два параметра х и у - это позиция окна. Третий - ширина, и четвертый - высота окна.

        self.ql2 = QLabel('Label 2', self)
        self.style2 = 'border:2px solid black'
        self.ql2.setStyleSheet(self.style)
        self.ql2.setGeometry(300, 100, 75, 400)

    def add_w_label(self):  # создаем функцию добавления в Label слов
        self.w_ = []  # список букв
        for i in self.ll.text():  # итерируем наш текст записанный в окне QLineEdit
            if i.isalpha():
                self.w_.append(i)  # добавляем найденные буквы в список букв

        self.word = ''.join(self.w_)  # буквы соединяем в строку
        print(self.w_, self.word)
        if self.rb.isChecked():  # если активирована Button 1
            self.ql.setText(self.word)  # заполняем буквами Label 1
        elif self.rb2.isChecked():  # если активирована Button 2
            self.ql2.setText(self.word)  # заполняем буквами Label 1
        self.mem.append(self.word)  # дополняем значения в список памяти
        print(self.mem)

    def add_i_label(self):  # создаем функцию добавления в Label цифр
        self.i_ = []  # список цифр
        for i in self.ll.text():
            if i.isdigit():
                self.i_.append(int(i)) # добавляем найденные цифры в список цифр в формате int
        self.int = str(sum(self.i_))  # сумма цифр переводим в строку
        print(self.i_, self.int)
        if self.rb.isChecked():  # если активирована Button 1
            self.ql.setText(self.int)  # заполняем суммой Label 1
        elif self.rb2.isChecked():  # если активирована Button 2
            self.ql2.setText(self.int)  # заполняем суммой Label 1
        self.int = int(self.int)  # переводим строку в число для заполнения списка памяти
        self.mem.append(self.int) # дополняем значения в список памяти
        print(self.mem)

    def all_label(self):  # создаем функцию добавления во все Labels сразу
        self.all_label = self.ll.text()  # обращаемся к функции add_w_label, чтобы забирать итерированные данные
        mem = ''  # строка памяти
        for i in self.mem:  # итеррируем список памяти
            mem += str(i) + '\n'  # добавляем значения строка и переходим на новую строчку
        if self.rb.isChecked():
            self.ql.setText(mem)  # заполняем значениями из памяти в Label 1
        elif self.rb2.isChecked():
            self.ql2.setText(mem)  # заполняем значениями из памяти в Label 1


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создаем объект из класса QApplication
    ex = Main()
    ex.show()  # Метод show() отображает виджет на экране
    sys.exit(app.exec_())  # sys.exit() гарантирует чистый выход
