from flask import Flask, request, redirect, url_for, render_template, g
from time import sleep
import random
from Player import Player
import voice_recognition as voice_recognition

target_time = 10
players = []

phrase_list = ["Do, or do not. There is no “try”.",
"Love cannot be found where it doesn’t exist, nor can it be hidden where it truly does.",
"Oh yes, the past can hurt. But you can either run from it, or learn from it.",
"Why are you trying so hard to fit in when you were born to stand out?",
"Life moves pretty fast. If you don’t stop and look around once in a while, you could miss it.",
"You can’t live your life for other people. You’ve got to do what’s right for you, even if it hurts some people you love.",
"We are who we choose to be.","Don’t let anyone ever make you feel like you don’t deserve what you want.",
"I don’t regret the things I’ve done, but those I did not do.",
"It is not our abilities that show what we truly are… it is our choices.",
"Run, Forrest, run!",
"My momma always said, “Life is like a box of chocolates, you never know what you’re gonna get.",
"Don’t ever let somebody tell you you can’t do something, not even me. Alright? You dream, you gotta protect it. People can’t do something themselves, they wanna tell you you can’t do it. If you want something, go get it. Period.",
"To see the world, things dangerous to come to, to see behind walls, to draw closer, to find each other and to feel. That is the purpose of life.",
"You cannot live your life to please others. The choice must be yours.",
"After a while, you learn to ignore the names people call you and just trust who you are.",
"If you’re going to try, go all the way. Otherwise don’t even start. This could mean losing girlfriends, wives, relatives, jobs. And maybe your mind. It could mean not eating for three or four days. It could mean freezing on a park bench. It could mean jail. It could mean derision. It could mean mockery, isolation. Isolation is the gift. All the others are a test of your endurance. Of how much you really want to do it. And you’ll do it, despite rejection in the worst odds. And it will be better than anything else you can imagine.",
"All we have to decide is what to do with the time that is given to us.",
"It’s what you do right now that makes a difference.",
"Our lives are defined by opportunities, even the ones we miss.",
"Great men are not born great, they grow great. - Mario Puzo, from The Godfather",
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
        players.append(Player(request.form["first_name"], 1000)) # Player1: name, hp
        players.append(Player(request.form["second_name"], 1000)) # Player2: name, hp
        phrase_list = random.choices(phrase_list, k=4)
        phrase_number = len(phrase_list)
        return render_template("phrase_show.html", phrase_list=phrase_list,phrase_number=phrase_number)
    else:
        return render_template("input.html")

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
    points = voice_recognition.compare_phrase(phrase, user_phrase)
    return render_template("battle.html", players=players, points=points) # 戦闘画面で表示するプレイヤーのデータをHTML側に渡す

if __name__ == '__main__':
    app.run(debug=True, port=8000)
