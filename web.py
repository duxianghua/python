from flask import Flask,render_template
app = Flask(__name__)

@app.route('/index.html')
def index():
	a=['192.168.1.223','ok','13ms','21.23','7 day','12312','32','2 day','4.32.4','2016-03-01']
	return render_template('index.html'navigation=a)


@app.route('/<pagename>')
def page():
	return pagename

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='80')