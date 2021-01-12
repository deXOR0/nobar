from flask import Flask, jsonify
from flask_cors import CORS
from tkinter import Tk, filedialog
import pyperclip
import os
import subtitle
import atexit

converted_subtitle = ''

def exit_handler():
    os.remove(converted_subtitle)

atexit.register(exit_handler)

app = Flask(__name__)
CORS(app)
ANCHOR = os.getcwd().replace('\MoviePicker', '')

@app.route('/get_movie')
def get_movie():
    root = Tk()
    root.wm_attributes('-topmost', 1)
    root.withdraw()
    filename = filedialog.askopenfilename(parent=root, title='Select a movie file', filetypes=[("Movie files", ".mp4 .mkv")])
    rel_path = os.path.relpath(filename, ANCHOR)
    pyperclip.copy(rel_path)

    return jsonify(rel_path)

@app.route('/get_subtitle')
def get_subtitle():
    global converted_subtitle
    root = Tk()
    root.wm_attributes('-topmost', 1)
    root.withdraw()
    filename = filedialog.askopenfilename(parent=root, title='Select a subtitle file', filetypes=[("Subtitle files", ".srt .vtt")])
    converted_subtitle = subtitle.convert(filename)
    rel_path = os.path.relpath(converted_subtitle, ANCHOR)

    return jsonify(rel_path)


if __name__ == '__main__':
    app.run(debug=True)