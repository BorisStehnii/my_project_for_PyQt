from functools import partial


class CalcController:

    def __init__(self, view, model):

        self._view = view
        self._model = model

        self._assign_signals()

    def _assign_signals(self):
        for btn in self._view.buttons:
            t_btn = btn.text()

            btn.clicked.connect(partial(self.update_display, t_btn))

    def update_display(self, value):
        if value in ['C', 'CE']:
            result = ''
        elif value == '=':
            result = self._model.evaluate_expression(self._view.display.text())
        else:
            result = self._view.display.text() + value
        self._view.display.setText(result)

