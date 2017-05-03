from flask import Flask, request
app = Flask(__name__)
 
@app.route("/")
def hello():
    return '<form action="/result" method="GET"><input name="city1"><input type="submit" value="Echo"></form>'
    return render/template('index_html',ms = '')

@app.route("/result")
def echo(): 
    #return render_template('result.html', ms = 'city1' )
    return render_template('index.html')
    return "You said: " + request.args.get('city1', '')
 
if __name__ == "__main__":
    app.run()
