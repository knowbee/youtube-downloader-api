from flask import jsonify, Flask, request
from flask_cors import CORS, cross_origin
from controllers import getVideo, getAudio

app = Flask(__name__)
cors = CORS(app)


@app.route('/video', methods=['GET', 'POST'])
@cross_origin()
def init():
  yt_url = str(request.args.get("url"))
  return jsonify(getVideo(yt_url))  
  
@app.route('/audio', methods=['GET', 'POST'])
@cross_origin()
def audio():
  yt_url = str(request.args.get("url"))
  return jsonify(getAudio(yt_url))
