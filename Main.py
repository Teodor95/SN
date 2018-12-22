import sys
import time

import threading
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow  # Imported one more module

from Client.Client import runClient
from Server.Server import runServer


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Whats\'app'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        # self.statusBar().showMessage('In progress')  # Added
        self.show()


if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # ex = App()
    # sys.exit(app.exec_())

    t1 = threading.Thread(target=runServer(), args=())
    t2 = threading.Thread(target=runClient(), args=())

    t1.start()
    t2.start()
    t1.join()
    t2.join()
