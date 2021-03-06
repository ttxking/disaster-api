import sys
import os
from flask import render_template

if not os.path.exists("config.py"):
    print("Configuration 'config.py' not found.  "
          "You may create one from 'config.py.example'.")
    exit(1)

from config import OPENAPI_AUTOGEN_DIR

if not os.path.exists(OPENAPI_AUTOGEN_DIR):
    print("Folder '{}' not found.  "
          "Execute openapi-generator to generate it, "
          "e.g.,".format(OPENAPI_AUTOGEN_DIR))
    print()
    print("  "
          "java -jar openapi-generator-cli-X.Y.Z.jar generate \\\n"
          "     -i openapi/disaster-api.yaml \\\n"
          "     -o {} -g python-flask".format(OPENAPI_AUTOGEN_DIR))
    print()
    exit(1)

sys.path.append(OPENAPI_AUTOGEN_DIR)

try:
    import connexion
except ModuleNotFoundError:
    print("Please install all required packages by running:"
          " pip install -r requirements.txt")
    exit(1)

from openapi_server import encoder

app = connexion.App(__name__, specification_dir='./openapi/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('disaster-api.yaml',
            arguments={'title': 'Thailand Disaster API'},
            pythonic_params=True)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/rain-avg', methods=['GET'])
def rain_avg():
    return render_template('rain-avg.html')


@app.route('/landslide', methods=['GET'])
def landslide_ratio():
    return render_template('landslide.html')


@app.route('/earthquake', methods=['GET'])
def earthquake():
    return render_template('earthquake.html')


if __name__ == '__main__':
    app.run(port=8080, debug=True)
