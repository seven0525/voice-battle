# Voice Battle
Voice Battleは、英語の発音の良さで相手と戦う対戦ゲームです。
相手の選択した英語フレーズを、対戦者が読み上げることによって精度を分析し相手のHPを削ります。

## アプリ画面

#### 起動画面
<img src="images/s1.png" width=50%>

#### 名前入力
<img src="images/s2.png" width=50%>

#### 相手に読ませたいフレーズの選択
<img src="images/s3.png" width=50%>

##### 録音中
<img src="images/s4.png" width=50%>

##### 結果
<img src="images/s5.png" width=50%>


## 技術
PyAudioを使ってマイクから音声を録音し、その読み取った音声が正しく認識されているかをSpeech to Textにて確認し分析しています。  
結果はHTML/CSS,JSにて表示しています。（HTMLパラメーターを使用）  
アプリ化はFlaskで行なっており、Herokuにデプロイしています。   


## 使用方法
[こちら]()より遊ぶことができます。   
ローカルにて実行したい場合は、GCPにてAPIのトークンを取得し値を代入してください。   



# スライド
["Voice Battle"](https://docs.google.com/presentation/d/1iFBaAtMOZIyeMXX9wZGxW85CJJjavnLxNM28rjb9rYc/edit?usp=sharing)
