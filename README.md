# CONTRIBUTOR
(c) 2020 RyuichiUeda and YuyaKobayashi

# 実行環境
  OS ubutu desktop 20.04 LTS
  
  ROS1
  
  gTTS 2.2.1
  
# 環境構築

以下のスクリプトを使用しROSの環境構築をしました。
https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_desktop

#　パッケージ

1. 本パッケージをインストールします。  
  
    $ cd ~/catkin_ws/src  
    $ git clone  https://github.com/yuyakobayashi7/tategakiMaker.git
    
    $ cd ~/catkin_ws
    $ catkin_make
    $ source ~/.bashrc
  
2. 音声ファイルを出力するため、gTTSをインストールします

   $ pip3 install gtts
   
# 実行方法

以下の3つのコードをそれぞれ別の端末上で実行してください。
出力された音声ファイルはプログラムを実行したディレクトリに作られます。
    
    $ rosrun tategakiMaker yoko.py
    $ rosrun tategakimaker tate.py
    $ rosrun tategakiMaker voice.py
    


# 映像
 後ではる

   
# LINECENSE

gTTS  MIT License

ROS   BSD
 
