from flask import Flask, jsonify
from flask_cors import CORS
from tkinter import Tk, filedialog
from shutil import copy
import os
import subtitle
import atexit

def exit_handler():
    for f in FILE_LIST:
        try:
            os.remove(f)
        except:
            pass

atexit.register(exit_handler)

app = Flask(__name__)
CORS(app)
ANCHOR = os.getcwd().replace('\MoviePicker', '')
FILE_FOLDER = os.path.join(ANCHOR, 'files')

# Preload the movie and subtitle list to clean files from previous sessions if the session didn't close properly
FILE_LIST = list(map(lambda s : os.path.join(FILE_FOLDER, s), os.listdir(FILE_FOLDER)))

def get_filename(filename):
    return filename.split('/')[-1]

def file_existed(filename):
    return os.path.isfile(filename)

@app.route('/get_movie')
def get_movie():
    global FILE_LIST
    root = Tk()
    root.wm_attributes('-topmost', 1)
    root.withdraw()
    filename = filedialog.askopenfilename(parent=root, title='Select a movie file', filetypes=[("Movie files", ".mp4 .mkv")])
    try:
        rel_path = os.path.relpath(filename, ANCHOR)
    except:
        movie_file = os.path.join(FILE_FOLDER, get_filename(filename))
        if file_existed(movie_file):
            pass
        else:
            copy(filename, FILE_FOLDER)
            FILE_LIST.append(movie_file)
        return jsonify(movie_file)
    
    return jsonify(rel_path)

@app.route('/get_subtitle')
def get_subtitle():
    global FILE_LIST
    root = Tk()
    root.wm_attributes('-topmost', 1)
    root.withdraw()
    filename = filedialog.askopenfilename(parent=root, title='Select a subtitle file', filetypes=[("Subtitle files", ".srt .vtt")])
    converted_subtitle = subtitle.convert(filename)
    FILE_LIST.append(converted_subtitle)
    try:
        rel_path = os.path.relpath(converted_subtitle, ANCHOR)
    except:
        subtitle_file = os.path.join(FILE_FOLDER, get_filename(converted_subtitle))
        if file_existed(subtitle_file):
            pass
        else:
            copy(converted_subtitle, FILE_FOLDER)
            FILE_LIST.append(subtitle_file)
        return jsonify(subtitle_file)

    return jsonify(rel_path)


if __name__ == '__main__':
    app.run(debug=True)
