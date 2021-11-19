from functools import partial
from PyQt5.QtWidgets import QCheckBox


class NoteController:

    def __init__(self, view):

        self._view = view
        # self._model = model
        self._assign_signal()

    def _assign_signal(self):
        btn = self._view.add_button
        btn.clicked.connect(partial(self.update_list_tasks))

    def update_list_tasks(self):
        task = self.create_task()
        task.setStyleSheet('font-size: 13pt; color: black')
        self._view.list_tasks.append(task)

        self._view.display.setText('')

        self._view.box_check_text.addWidget(task)

    def create_task(self):
        task = QCheckBox(f"{self._view.display.text()}")
        task.stateChanged.connect(partial(self._view.update_list_completed_tasks, task))
        return task

