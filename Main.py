import random

from PyQt5 import *
from PyQt5.QtWidgets import *
from pygame.time import wait

app = QApplication([])
coins = "10"
numb = 0
app.setStyleSheet("""
        QPushButton {
            color:#35374B;
        background-color: #FFFFCC;
        }
        
        QWidget {
            color:#35374B;
        background-image: url("Back.png");
        }
        
                
        QLabel#introduction {
            color: #FF6666;
            border: 20px;
            font-size: 33px;
            fx-border-size: 15px;
        }
        QLabel#okk {
            color: #999900;
            font-size: 22px;

        }

    """)





add_perclick_button = QPushButton("Збільшити кількість монет за правильну відповідь")




coins_count = QLabel("Ваші монети:"+coins)
intro = QLabel("Математичні завдання!")
ans1 = QPushButton("49")
ans2 = QPushButton("7")
ans3 = QPushButton("23")
ans4 = QPushButton("50")
ans5 = QPushButton("2.3")
ans6 = QPushButton("6")



shop = QPushButton("Магазин")

question = QLabel("Нажміть на кнопку старту для створення питання")
Start = QPushButton("Створити питання")




window = QWidget()
window.resize(700, 500)

K1 = QVBoxLayout()

B1 = QHBoxLayout()
B2 = QHBoxLayout()



B2.addWidget(add_perclick_button)


window.setLayout(K1)

K1.addLayout(B1)
K1.addLayout(B2)









menu_play = QDialog()
menu_play.resize(400,250)

menu_play.show()

H1 = QVBoxLayout()
V1 = QHBoxLayout()
V2 = QHBoxLayout()
V3 = QHBoxLayout()
V4 = QHBoxLayout()
V5 = QHBoxLayout()

menu_play.setLayout(H1)
H1.addLayout(V1)
H1.addLayout(V2)
H1.addLayout(V3)
H1.addLayout(V4)
H1.addLayout(V5)





V1.addWidget(question)
V1.addWidget(coins_count)
H1.addWidget(intro)
V2.addWidget(ans1)
V2.addWidget(ans2)
V3.addWidget(ans3)
V3.addWidget(ans4)
V4.addWidget(ans5)
V4.addWidget(ans6)
V5.addWidget(shop)
V5.addWidget(Start)



def gotoshop():
    window.show()



def next_question():
    rand = random.randint(1,8)
    if rand == 1:
        question.setText("Скільки буде 7*7")
        numb = 49
    if rand == 2:
        question.setText("Скільки буде (7+3)*5")
        numb = 50
    if rand == 3:
        question.setText("Скільки буде (2.6/2)+1")
        numb = 2.3
    if rand == 4:
        question.setText("Скільки буде 30-7")
        numb = 23
    if rand == 5:
        question.setText("Скільки буде 3*4/2")
        numb = 6
    if rand == 6:
        question.setText("Скільки буде √25")
        numb = 5
    if rand == 7:
        question.setText("Скільки буде √2401")
        numb = 49
    if rand == 8:
        question.setText("Скільки буде 50*123-6100")
        numb = 50


def start_game():
    intro.setText("   ")
    rand = random.randint(1,8)
    if rand == 1:
        question.setText("Скільки буде 7*7")
        numb = 49
    if rand == 2:
        question.setText("Скільки буде (7+3)*5")
        numb = 50
    if rand == 3:
        question.setText("Скільки буде (2.6/2)+1")
        numb = 2.3
    if rand == 4:
        question.setText("Скільки буде 30-7")
        numb = 23
    if rand == 5:
        question.setText("Скільки буде 3*4/2")
        numb = 6
    if rand == 6:
        question.setText("Скільки буде √25")
        numb = 5
    if rand == 7:
        question.setText("Скільки буде √2401")
        numb = 49
    if rand == 8:
        question.setText("Скільки буде 50*123-6100")
        numb = 50

def answr1():
    if numb == 49:
        coins + 1
        print("f")
    else:
        coins + 0
        next_question()

def answr2():
    if numb == 7:
        coins + 1
    else:
        coins + 0
        next_question()



ans1.clicked.connect(answr1)
Start.clicked.connect(start_game)
intro.setObjectName("introduction")
coins_count.setObjectName("okk")
ans1.clicked.connect(next_question)
shop.clicked.connect(gotoshop)
app.exec()
