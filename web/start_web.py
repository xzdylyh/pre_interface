from flask import Flask, render_template

app = Flask(__name__)

@app.route('/report/<report_name>')
def  report(report_name):
    return render_template(r'/report/{}'.format(report_name))

if __name__ == "__main__":
    # app.debug = True
    app.run()