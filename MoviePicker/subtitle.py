import webvtt
import os

webvtt = webvtt.from_srt(os.path.join(os.getcwd(), r'MoviePicker\init.srt'))

def convert(filename):
    if 'vtt' in filename: # if the selected file is already a vtt, return the file
        return filename
    elif os.path.exists(filename.replace('srt', 'vtt')): # if a vtt conversion already occurs, return the correct file
            return filename.replace('srt', 'vtt')
        

    global webvtt 
    webvtt = webvtt.from_srt(filename)
    webvtt.save()
    return filename.replace('srt', 'vtt')