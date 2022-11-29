from flask import Flask,render_template
p1 = Flask(__name__)

@p1.route('/')
def main():
    return render_template('try.html')
if __name__ == '__main__':
    p1.run(host="0.0.0.0",port=8082)
