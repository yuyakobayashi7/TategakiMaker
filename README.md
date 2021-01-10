# CONTRIBUTOR
(c) 2020 RyuichiUeda and YuyaKobayashi

# 実行環境
  OS ubutu desktop 20.04 LTS
  
  ROS1
  
  gTTS 2.2.1
  
# 環境構築

以下のスクリプトを使用しROSの環境構築をしました。
https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_desktop

# パッケージのインストール

1. 本パッケージをインストールします。  
  
    $ cd ~/catkin_ws/src  
    $ git clone  https://github.com/yuyakobayashi7/tategakiMaker.git
    
    $ cd ~/catkin_ws
    
    $ catkin_make
    
    $ source ~/.bashrc
  
2. 音声ファイルを出力するため、gTTSをインストールします

   $ pip3 install gtts
   
# 実行方法

1. まずはじめに roscore を立ち上げてください。

    $ roscore

2. 次に、以下の3つのコードをそれぞれ別の端末上で実行してください。
    
    $ rosrun tategakiMaker yoko.py
    
    $ rosrun tategakimaker tate.py
    
    $ rosrun tategakiMaker voice.py
    
# プログラムの説明

  入力した文字列を縦書きに出力します。
  
  利用すると利用者への感謝のメッセージの音声ファイルが作られます。
  
  gTTSを利用するのでインターネットに接続した状態で実行してください。
  
  ubuntu 20.04 の場合は、出力された音声ファイルは/home/userに作られます。
  
  保存先を ./ にしています。環境によってはパス名が少し違うかもしれません。
  

# 映像
 https://youtu.be/-BBS-tfj6Hc

   
# LINECENSE

This repository is licensed under the BSD license

gTTS MIT License　
https://pypi.org/project/gTTS/

ROS BSD License
 
