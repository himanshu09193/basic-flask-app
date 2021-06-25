from flask import Flask, render_template
app = Flask(__name__)

# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', the_title='Real Estate housing - Helps in finding your home')

@app.route('/symbol.html')
def symbol():
    return render_template('symbol.html', the_title='Contact us')

@app.route('/myth.html')
def myth():
    return render_template('myth.html', the_title='Choose from listing')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)