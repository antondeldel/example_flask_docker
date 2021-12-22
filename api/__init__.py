from flask import Flask, jsonify
import flask
import gunicorn
import sys
 
def create_app():
    app = Flask(__name__)

    @app.route("/api/test", methods=["GET"])
    def sample_route():
        return jsonify({"message": "This is a sample route3"})

    @app.route("/", methods=["GET"])
    def sample_route2():
        return jsonify({"message": "This is a sample route4",
        "flaskversion":str(flask.__version__)
        ,"gunicornversion":str(gunicorn.__version__)
        ,"PythonVersion":str(sys.version)
        
        })

    return app