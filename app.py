from flask import Flask, jsonify, abort, send_from_directory

UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

if __name__ == "__main__":
    app.debug = True
    app.run()
                               

