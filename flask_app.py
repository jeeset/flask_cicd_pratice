from flask import Flask

app_100  = Flask(__name__)

@app_100.route("/")
def index():
	return "This is index"

@app_100.route("/hello")
def hello():
        return "<h1>Hello World!</h1>"

@app_100.route("/healthz")
def healthz():
	return {"status":"ok"}

def add_numbers(a, b):
	return a + b

if __name__ == "__main__":
	app_100.run(host="0.0.0.0", port=5000)
