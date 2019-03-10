from flask import Flask, request, redirect, url_for, render_template, g
from time import sleep
import random
from Player import Player
import voice_recognition as voice_recognition

target_time = 10
players = []
atk_turn = 0 # 攻撃しているプレイヤーのインデックス。0: 先攻、1: 後攻

phrase_list = [
    "The rainy season is coming",
    "Thank you for your cooperation",
    "How was your weekend?",
    "I feel so irritated because nothing goes well",
    "I would like to pick up my baggage",
    "You cannot live your life for other people",
    "We are who we choose to be",
    "I do not regret the things I have done",
    "It is not our abilities that show what we truly are",
    "Love you now and forever",
    "Life is like a box of chocolates, you never know what you are going to get",
    "They want tp tell you you cannot do it",
    "You cannot live your life to please others",
    "You learn to ignore the names people call you",
    "This could mean losing girlfriends",
    "It could mean not eating for three or four days",
    "All the others are a test of your endurance",
    "it will be better than anything else you can imagine",
    "All we have to decide is what to do with the time that is given to us",
    "It is what you do right now that makes a difference",
    "Our lives are defined by opportunities",
    "Great men are not born great"
]

def up_timer(secs):
    for i in range(0,secs):
        print("のこり{}秒です".format(target_time-i))
        sleep(1)
    print("時間です！")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/input')
def input():
    return render_template("input.html")

@app.route('/send',methods=["POST","GET"])
def send():
    if request.method == "POST":
        global phrase_list
        players.append(Player(request.form["first_name"], 1000, 1000)) # Player1: name, hp, max_hp
        players.append(Player(request.form["second_name"], 1000, 1000)) # Player2: name, hp, max_hp
        phrase_list1 = random.choices(phrase_list, k=4)
        phrase_number = len(phrase_list1)
        return render_template("phrase_show.html", phrase_list=phrase_list1, phrase_number=phrase_number)
    else:
        return render_template("input.html")

@app.route('/send2', methods=["POST", "GET"])
def send2():
    """
    battle.html -> phrase_show.html
    """
    global phrase_list
    phrase_list2 = random.choices(phrase_list, k=4)
    phrase_number = len(phrase_list2)
    return render_template("phrase_show.html", phrase_list=phrase_list2, phrase_number=phrase_number)

@app.route('/choice',methods=["POST","GET"])
def choice():
    global phrase
    phrase = request.form["select_phrase"]
    return render_template("phrase_speak.html",phrase=phrase)

@app.route("/voice") # phrase_speak.htmlで3秒経過したらこっちに移動
def voice():
    global user_phrase
    user_phrase = voice_recognition.main()
    return render_template("user_phrase.html", user_phrase=user_phrase)

@app.route('/battle') #JSで画面遷移するときに引数を一緒に持っていく方法が分からない
def send_battle():
    global players
    points = voice_recognition.compare_phrase(phrase, user_phrase)
    players[atk_turn].receive_damage(points) # 発音の正確さのポイント -> ダメージに反映
    # 
    if atk_turn == 0:
        atk_turn = 1
    elif atk_turn == 1:
        atk_turn = 0
    return render_template("battle.html", players=players, points=points) # 戦闘画面で表示するプレイヤーのデータをHTML側に渡す

if __name__ == '__main__':
    app.run(debug=True, port=8000)
