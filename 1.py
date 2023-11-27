import sys
import io
import random
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow

t = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1229</width>
    <height>853</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>470</x>
      <y>610</y>
      <width>201</width>
      <height>81</height>
     </rect>
    </property>
    <property name="text">
     <string>Нарисовать</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1229</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>"""

class Ellips(QMainWindow):
    def __init__(self):
        super().__init__()
        self.x, self.y = 600, 425
        self.initUI()

    def initUI(self):
        f = io.StringIO(t)
        uic.loadUi(f, self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            p = random.randrange(20, 1000)
            r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            qp.setBrush(QColor(r, g, b))
            qp.drawEllipse(self.x - (p // 4), self.y - (p // 4), (p // 2), (p // 2))
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ellips()
    ex.show()
    sys.exit(app.exec())

