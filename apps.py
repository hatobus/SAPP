# coding: utf-8
from flask import Flask, render_template, render_template, request, url_for
from werkzeug.datastructures import TypeConversionDict
import test2

#import test2
app = Flask(__name__) #インスタンス生成

@app.route("/",methods=['GET','POST']) 
def index(): 

   # city1 = request.form.get('Leave')
   # city2 = request.form.get('go')
    return render_template('index.html', ms = "") 

@app.route("/result", methods=['GET','POST']) #アプリケーション/indexにアクセスが合った場合
def result():
   
    # city1 = request.args.get("Leave", default="aa", type=str)
    # city2 = request.args.get("go", default="aa", type=str)
    if request.method == "POST":
        city1 = request.form.get("Leave")
        city2 = request.form.get("go")
    dist = test2.calcRadiation().init(city1,city2)
    return render_template('result.html', ms = city1 ,ds = dist) 
    # return city1
#ここがサーバーサイドからクライアントサイドへなにかを渡すときのポイントになります。

if __name__ == "__main__":
    # webサーバー立ち上げ
    app.run(debug=True)
    #app.run()

