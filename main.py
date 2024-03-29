from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
  return 'Hello from Flask!'


@app.route('/admin')
def admin():
  return render_template("admin.html")


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80, debug=True)
