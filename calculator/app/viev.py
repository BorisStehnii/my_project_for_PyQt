from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLineEdit, QGridLayout, QPushButton
from PyQt5.QtCore import Qt


class CalcView(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Simple Calculator')
        self.setFixedSize(700, 550)

        self._central_widget = QWidget(self)
        self.setCentralWidget(self._central_widget)

        self.main_layout = QVBoxLayout()
        self._central_widget.setLayout(self.main_layout)

        self._create_display()
        self._create_buttons()

    def _create_display(self):
        self.display = QLineEdit()

        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(60)
        self.display.setReadOnly(True)

        self.display.setStyleSheet('font-size: 40pt; color: gray')

        self.main_layout.addWidget(self.display)

    def _create_buttons(self):
        self.lbuttons = QGridLayout()
        self.buttons = []
        button_cords = {
            '1': (2, 0),
            '2': (2, 1),
            '3': (2, 2),

            '4': (1, 0),
            '5': (1, 1),
            '6': (1, 2),

            '7': (0, 0),
            '8': (0, 1),
            '9': (0, 2),

            '0': (3, 0),
            '00': (3, 1),
            '.': (3, 2),
            '+': (3, 3),
            '-': (2, 3),

            '/': (0, 3),
            '*': (1, 3),
            '=': (2, 4, 2, 1),
            'C': (0, 4),
            'CE': (1, 4)

        }

        for t_btn, cord in button_cords.items():
            q_btn = QPushButton(t_btn)
            if t_btn == '=':
                q_btn.setFixedSize(130, 230)
            else:
                q_btn.setFixedSize(130, 110)
            q_btn.setStyleSheet('font-size: 40pt; color: gray')
            self.lbuttons.addWidget(q_btn, *cord)
            self.buttons.append(q_btn)

        self.main_layout.addLayout(self.lbuttons)





