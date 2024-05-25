from PyQt5 import *
from PyQt5.QtWidgets import *
from pygame.time import wait

app = QApplication([])
Coins = "123"
app.setStyleSheet("""
        QDialog {
            color:#35374B;
        background-color: white;
        }
        
        QWidget {
            color:#35374B;
        background-image: url("Back.png");
        }

    """)











play1 = QPushButton("Зіграти в 1 рівень")
play2 = QPushButton("Зіграти в 2 рівень")
play3 = QPushButton("Зіграти в 3 рівень")
play4 = QPushButton("Зіграти в 4 рівень")
play5 = QPushButton("Зіграти в 5 рівень")
play6 = QPushButton("Зіграти в 6 рівень")
play7 = QPushButton("Зіграти в 7 рівень")
play8 = QPushButton("Зіграти в 8 рівень")
Map = QPushButton("Переглянути карту рівнів")
coins = QLabel("Ваші монети -"+"Coins")





window = QWidget()
window.resize(700, 500)

menu_play = QDialog()
menu_play.resize(400,250)

menu_play.show()

H1 = QVBoxLayout()
V1 = QHBoxLayout()
V2 = QHBoxLayout()
V3 = QHBoxLayout()
V4 = QHBoxLayout()

menu_play.setLayout(H1)
H1.addLayout(V1)
H1.addLayout(V2)
H1.addLayout(V3)
H1.addLayout(V4)


V1.addWidget(play1)
V1.addWidget(play2)
V2.addWidget(play3)
V2.addWidget(play4)
V3.addWidget(play5)
V3.addWidget(play6)
V4.addWidget(play7)
V4.addWidget(play8)
H1.addWidget(Map)
H1.addWidget(coins)


def watch_map():
    window.show()





Map.clicked.connect(watch_map)
app.exec()
