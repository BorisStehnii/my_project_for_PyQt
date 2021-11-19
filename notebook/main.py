import sys

from PyQt5.QtWidgets import QApplication

from app.viev import NoteView
from app.model import NoteModel
from app.controller import NoteController


def main():
    app = QApplication(sys.argv)

    view = NoteView()
    model = NoteModel
    NoteController(view=view)

    view.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
