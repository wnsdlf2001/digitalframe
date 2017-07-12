from PyQt4.QtGui import *
import update_img
import subprocess
import sys
class Mydialog(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle('Digital Frame')
        self.setGeometry(600,600,500,300)
        self.setStyleSheet("background: url(:/backimage/rasp.jpg)")

        btnDown = QPushButton("Download",self)
        btnDown.resize(100,50)
        btnDown.move(200,50)
        btnGIF = QPushButton("Show GIF",self)
        btnGIF.resize(100, 50)
        btnGIF.move(200,125)
        btnPic = QPushButton("Show Picture",self)
        btnPic.resize(100, 50)
        btnPic.move(200,200)

        self.show()

        btnDown.clicked.connect(self.btnDownClick)
        btnGIF.clicked.connect(self.btnGIFClick)
        btnPic.clicked.connect(self.btnPicClick)


    def btnDownClick(self):
        update_img.GIF()
        update_img.pic()

    def btnGIFClick(self):
            subprocess.call(['python', 'play2.py'])
            print('*** play contents')

    def btnPicClick(self):
            subprocess.call(['python', 'play.py'])
            print('*** play contents.')


app = QApplication(sys.argv)
dialog = Mydialog()
dialog.show()
sys.exit(app.exec_())
