import sys

from PyQt5.QtWidgets import QApplication

from app.viev import CalcView
from app.controller import CalcController
from app.model import CalcModel


def main():
    app = QApplication(sys.argv)

    view = CalcView()
    model = CalcModel()
    CalcController(view=view, model=model)

    view.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()



