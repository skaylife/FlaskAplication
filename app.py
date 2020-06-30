from flask import Flask
from pyfladesk import init_gui


app = Flask(__name__)



from routes import *



if __name__ == '__main__':
    init_gui(app, port=5000, width=900, height=750,
             window_title="PyFladesk", icon="appicon.png", argv=None)