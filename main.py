from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    app.run()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/ahahah')
def ahahah():
    return render_template('ahahah.html')

@app.route('/2')
def f2():
    return render_template('ahahah.html')


if __name__ == '__main__':
    main()
