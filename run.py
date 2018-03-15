from flask import Flask, render_template
from app.modules.Controller import controller

app = Flask("HanaToPython", template_folder='app/templates', instance_relative_config=True)
app.register_blueprint(controller)
app.config.from_object('config.DevelopmentConfig')


@app.route("/")
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(use_reloader=True)
