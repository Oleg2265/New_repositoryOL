import random
import json
from PyQt5 import *
from PyQt5.QtWidgets import *
from pygame.time import wait

notes = {}
def read_data():
    global notes
    with open("database.json", "r", encoding="utf-8") as file:
        notes = json.load(file)



def write_data():
    global notes
    with open("database.json", "w", encoding="utf-8") as file:
        json.dump(notes, file, ensure_ascii=False, indent=4)
read_data()
app = QApplication([])

good = 0
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





add_perclick_button = QPushButton("Збільшити множувач монет:КОШТУЄ 10 МОНЕТ")
add_perclick_button5 = QPushButton("Збільшити множувач монет на 5:КОШТУЄ 50 МОНЕТ")



coins_count = QLabel("Ваші монети:"+str(notes["coins"]))
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
K1.addWidget(coins_count)
B2.addWidget(add_perclick_button5)



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
    coins_count.setText("Ваші монети:" + str(notes["coins"]))
    window.show()



def next_question():
    global good
    rand = random.randint(1,8)
    if rand == 1:
        question.setText("Скільки буде 7*7")
        good = 1
    if rand == 2:
        question.setText("Скільки буде (7+3)*5")
        good = 2
    if rand == 3:
        question.setText("Скільки буде (2.6/2)+1")
        good = 3
    if rand == 4:
        question.setText("Скільки буде 30-7")
        good = 4
    if rand == 5:
        question.setText("Скільки буде 3*4/2")
        good = 5
    if rand == 6:
        question.setText("Скільки буде √25")
        good = 6
    if rand == 7:
        question.setText("Скільки буде √2401")
        good = 7
    if rand == 8:
        question.setText("Скільки буде 50*123-6100")
        good = 8


def start_game():
    global good
    intro.setText("   ")
    rand = random.randint(1,8)
    global good
    rand = random.randint(1,8)
    if rand == 1:
        question.setText("Скільки буде 7*7")
        good = 1
    if rand == 2:
        question.setText("Скільки буде (7+3)*5")
        good = 2
    if rand == 3:
        question.setText("Скільки буде (2.6/2)+1")
        good = 3
    if rand == 4:
        question.setText("Скільки буде 30-7")
        good = 4
    if rand == 5:
        question.setText("Скільки буде 3*4/2")
        good = 5
    if rand == 6:
        question.setText("Скільки буде √25")
        good = 6
    if rand == 7:
        question.setText("Скільки буде √2401")
        good = 7
    if rand == 8:
        question.setText("Скільки буде 50*123-6100")
        good = 8



def answr49():
    if good == 1:
        notes["coins"] += notes["money_x"]
    next_question()


def answr50():
    if good == 2:
        notes["coins"] += notes["money_x"]
        print(1)
    next_question()


def answr2_3():
    if good == 3:
        notes["coins"] += notes["money_x"]
    next_question()
def answr23():
    if good == 4:
        notes["coins"] += notes["money_x"]
    next_question()
def answr12():
    if good == 5:
        notes["coins"] += notes["money_x"]
    next_question()
def answr6():
    if good == 6:
        notes["coins"] += notes["money_x"]
    next_question()
def answr49_2():
    if good == 7:
        notes["coins"] += notes["money_x"]
    next_question()
def answr50_2():
    if good == 8:
        notes["coins"] += notes["money_x"]
    next_question()


def More_money_x():
    if notes["coins"]>10:
        notes["money_x"] += 1
        notes["coins"] -= 10
        print("Успішна покупка!")
        coins_count.setText("Ваші монети:" + str(notes["coins"]))
    else:
        print("Нехватає коштів!")

def More_money_x5():
    if notes["coins"]>50:
        notes["money_x"] += 5
        notes["coins"] -= 50
        print("Успішна покупка!")
        coins_count.setText("Ваші монети:" + str(notes["coins"]))
    else:
        print("Нехватає коштів!")




Start.clicked.connect(start_game)
intro.setObjectName("introduction")
coins_count.setObjectName("okk")
ans1.clicked.connect(next_question)
ans1.clicked.connect(answr49)
ans1.clicked.connect(answr49_2)
ans3.clicked.connect(answr23)
ans4.clicked.connect(answr50)
ans4.clicked.connect(answr50_2)
ans5.clicked.connect(answr2_3)
ans6.clicked.connect(answr6)
shop.clicked.connect(gotoshop)
add_perclick_button.clicked.connect(More_money_x)
add_perclick_button5.clicked.connect(More_money_x5)
app.exec()
