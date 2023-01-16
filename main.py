from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')


@app.errorhandler(404)
def err_not_found(e):
    return render_template('error_404.html')


if __name__ == "__main__":
    app.run(debug=True)