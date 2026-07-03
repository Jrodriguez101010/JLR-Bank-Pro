import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('JLR Bank Pro - Alpha 0.1')
        self.setMinimumSize(900, 600)
        self.setCentralWidget(QLabel('JLR Bank Pro iniciado correctamente'))

def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()