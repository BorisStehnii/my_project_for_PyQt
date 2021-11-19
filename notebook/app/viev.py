from PyQt5.QtWidgets import (QMainWindow, QWidget, QScrollArea, QCheckBox,
                             QVBoxLayout, QHBoxLayout, QLineEdit, QGridLayout, QPushButton)
from functools import partial

class NoteView(QMainWindow):

    def __init__(self):
        super().__init__()

        self.list_tasks = []

        self.setWindowTitle('notebook')
        self.setFixedSize(500, 300)

        self._central_widget = QWidget(self)
        self.setCentralWidget(self._central_widget)

        self.main_layout = QVBoxLayout()
        self._central_widget.setLayout(self.main_layout)

        self._create_display()
        self._create_list_tasks()
        self._create_list_completed_tasks()



    def _create_display(self):

        self.add_text_widget = QHBoxLayout()

        self.display = QLineEdit()
        self.display.setFixedHeight(40)
        self.display.setStyleSheet('font-size: 20pt; color: black')

        self.add_button = QPushButton("Add")
        self.add_button.setFixedSize(60, 40)
        self.add_button.setStyleSheet('font-size: 20pt; color: black')

        self.add_text_widget.addWidget(self.display)
        self.add_text_widget.addWidget(self.add_button)

        self.main_layout.addLayout(self.add_text_widget)

    def _create_list_tasks(self):

        self.display_scroll = QScrollArea()
        self.display_scroll.setFixedHeight(100)
        self.display_scroll.setWidgetResizable(True)

        self.buffer_widget = QWidget()
        self.display_scroll.setWidget(self.buffer_widget)

        self.box_check_text = QVBoxLayout(self.buffer_widget)
        self.box_check_text.addStretch()

        self.main_layout.addWidget(self.display_scroll)

    def _create_list_completed_tasks(self):

        self.display_scroll_completed = QScrollArea()
        self.display_scroll_completed.setFixedHeight(100)
        self.display_scroll_completed.setWidgetResizable(True)

        self.buffer_widget_completed = QWidget()
        self.display_scroll_completed.setWidget(self.buffer_widget_completed)

        self.box_check_text_completed = QVBoxLayout(self.buffer_widget_completed)
        self.box_check_text_completed.addStretch()

        self.main_layout.addWidget(self.display_scroll_completed)

    def update_list_completed_tasks(self, task):
        _task = task
        self.box_check_text_completed.addWidget(_task)
        self.delete_completed_tasks(task=_task)

    def delete_completed_tasks(self, task):
        self.box_check_text.removeWidget(task)

