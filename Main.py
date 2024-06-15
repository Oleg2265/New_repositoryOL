import random
import json
from PyQt5 import *
from PyQt5.QtWidgets import *
from pygame.time import wait
start_game_work = 0
notes = {}
jackpot_chance = 0
x_buyer = 0
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
        QLabel#Cases {            
             color: #999900; 
             font-size: 22px;
                                    
        }
        QPushButton#Open_crate {                  
             color: #35374B;             
             background-color: #FFFFCC;      
        }                                            
    """)





add_perclick_button = QPushButton("Збільшити множувач монет:КОШТУЄ 10 МОНЕТ")
add_perclick_button5 = QPushButton("...")


open_case = QPushButton("Відкрити кейс(1-10000+ монет)")
coins_count = QLabel("Ваші монети:"+str(notes["coins"]))
intro = QLabel("Математичні завдання!")
ans1 = QPushButton("49")
ans2 = QPushButton("7")
ans3 = QPushButton("23")
ans4 = QPushButton("5")
ans5 = QPushButton("2.3")
ans6 = QPushButton("6")



shop = QPushButton("Магазин")

question = QLabel("Нажміть на кнопку старту для створення питання")
Start = QPushButton("Створити питання")
Case_count = QLabel("Ваші кейси:"+ str(notes["case_count"]))



window = QWidget()
window.resize(700, 500)

K1 = QVBoxLayout()

B1 = QHBoxLayout()
B2 = QHBoxLayout()
B3 = QHBoxLayout()


B2.addWidget(add_perclick_button)

K1.addWidget(coins_count)
K1.addWidget(Case_count)
B2.addWidget(add_perclick_button5)
B3.addWidget(open_case)


window.setLayout(K1)

K1.addLayout(B1)
K1.addLayout(B2)
K1.addLayout(B3)













menu_play = QDialog()
menu_play.resize(700,450)

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
        question.setText("Скільки буде 1-2+6")
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
        question.setText("Скільки буде 6-2-6-2+6+5")
        good = 8


def start_game():
    global good
    intro.setText("   ")
    rand = random.randint(1,8)
    global good
    global start_game_work
    if start_game_work == 0:
        rand = random.randint(1,8)
        if rand == 1:
            question.setText("Скільки буде 7*7")
            good = 1
        if rand == 2:
            question.setText("Скільки буде 1-2+6")
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
            question.setText("Скільки буде 6-2-6-2+6+5")
            good = 8
        start_game_work = 1

case_mon = random.randint(1,500)
def open_crates():
    global case_mon
    if notes["case_count"] >= 1:
        notes["case_count"] -= 1
        notes["coins"] += notes["money_x"]*case_mon
        Case_count.setText("Ваші кейси:"+ str(notes["case_count"]))
        coins_count.setText(("Ваші монети:"+str(notes["coins"])))



    else:
        pass

def jackpot():
    global jackpot_chance
    jackpot_chance = random.randint(0,30)
    if jackpot_chance == 7:
        notes["coins"] += 7*notes["money_x"]
        print("Джекпот!")

def answr49():
    global good
    if good == 1:
        notes["coins"] += notes["money_x"]
        print(1)
        jackpot()
    next_question()


def answr5():
    if good == 2:
        notes["coins"] += notes["money_x"]
        jackpot()
        print(2)
    next_question()


def answr2_3():
    if good == 3:
        notes["coins"] += notes["money_x"]
        jackpot()
        print(3)
    next_question()
def answr23():
    if good == 4:
        notes["coins"] += notes["money_x"]
        jackpot()
        print(4)
    next_question()
def answr6():
    if good == 5:
        notes["coins"] += notes["money_x"]
        jackpot()
        print(5)
    next_question()
def answr5_2():
    if good == 6:
        notes["coins"] += notes["money_x"]
        jackpot()
        print(6)
    next_question()
def answr2401():
    if good == 7:
        notes["coins"] += notes["money_x"]
        jackpot()
        print(7)
    next_question()
def answr7():
    if good == 8:
        notes["coins"] += notes["money_x"]
        jackpot()
        print(8)
    next_question()


def More_money_x():
    global x_buyer
    if x_buyer >= 4:
        add_perclick_button5.setText("Збільшити множувач монет на 5:КОШТУЄ 50 МОНЕТ")

    if notes["coins"]>10:
        notes["money_x"] += 1
        notes["coins"] -= 10
        print("Успішна покупка!")
        coins_count.setText("Ваші монети:" + str(notes["coins"]))
    else:
        print("Нехватає коштів!")
    x_buyer += 1

def More_money_x5():
    global x_buyer
    if x_buyer >= 5:
        if notes["coins"]>50:
            notes["money_x"] += 5
            notes["coins"] -= 50
            print("Успішна покупка!")
            coins_count.setText("Ваші монети:" + str(notes["coins"]))
        else:
            print("Нехватає коштів!")





Start.clicked.connect(start_game)
intro.setObjectName("introduction")
Case_count.setObjectName("Cases")
open_case.setObjectName("Open_crate")
coins_count.setObjectName("okk")
ans1.clicked.connect(answr49)
ans2.clicked.connect(answr7)
ans3.clicked.connect(answr23)
ans4.clicked.connect(answr5)
ans5.clicked.connect(answr2_3)
ans6.clicked.connect(answr6)
shop.clicked.connect(gotoshop)
add_perclick_button.clicked.connect(More_money_x)
add_perclick_button5.clicked.connect(More_money_x5)
open_case.clicked.connect(open_crates)
app.exec()
