# nobar
I enjoy watching movies and tv series together with my friends, since the pandemic it's been hard to do that, so we watch movies together through platforms such as Discord and Zoom, but there are several problems, first of all, Zoom is great, its by far the best platform to watch movies, it supports audio sharing accross the board, and supports video optiomazation. But it is not free and certainly not cheap for broke college students. Discord fares better in the financial categories but is beaten in all other aspects. It only supports audio sharing when you share a windows, not the entire screen, and furthermore it doesn't allow you to share VLC player.
Netflix through browser works though, so that's something. And then I got an Idea to look for video players that works on browser and take local video file. To my surprise there aren't any, or at least I didn't find them when I was looking for it, so I set out to built just that.
I initially want to keep this simple and just built a static webpage without any backend, but because how HTML handles file input, I cannot simply build a file picker with HTML that works just the way I want it (or at least I haven't figured out a way yet, do let me know if you have a suggestion, I really want to cut the services part :D), more on that later.

## Initial Setup
1. Clone the repository
    ```
    git clone https://github.com/deXOR0/nobar.git
    ```
2. Install the requirements
    ```
    pip install requirements.txt
    ```
4. On nobar.bat, change this line
    ```
    python "F:\Film & TV Show\Nobar\nobar.py" %*
    ```
    To
    ```
    python "<your app path>\Nobar\nobar.py" %*
    ```
5. You're done! You can skip step 2 if you don't care about the file picker. You can still use it by typing in the path yourself

## How to use
1. Run from the shortcut provided or from the batch file.
2. Alternatively, you can run it with command line
    ```
    python nobar.py
    ```
3. If you dont use the services, you can open the html file directly
4. In order to use subtitle, you need to open chrome with this command
    ```
    start chrome nobar.html --allow-file-access-from-files
    ```
    If you're on linux or mac os, use this command
    ```
    google-chrome nobar.html --allow-file-access-from-files
    ```
    If you are run it with step 1 or 2, this is already done automatically, you can also skip this step if you don't want to use external subtitle file (srt or vtt will work, srt will automatically be converted to vtt by the flask service)

## Restrictions
Windows does not use relative path between drives, as it is not mounted on a single root directory, unlike literally everything else is the market, so the only downside is that you have to have a separete instance of this app on each of your drive if you have multiple drives. This problem only occurs in windows. I solved this problem by creating a 'files' directory and copy the file from other drives into it. This solves the problem but it is very impracticle and takes a lot of time. I implemented some functions to automatically clean the directory in an effort to make it less demanding on storage space. 

## Prerequisites
- Python 3.x
- pip
- Chrome Web Browser

## The Architecture
It started out as a simple front end stack (HTML, CSS, Js with some Bootstrap), but I quickly ran into an issue. HTML doesn't allow full path on their file picker for security reasons. So I built a simple service that serve filepickers with Flask.
This is how the app works
1. Starts flask services
2. Opens chrome and serve the html page
3. JavaScript will make the requests
4. Flask service will handle the request accordingly
5. The default will be set to 127.0.0.1:5000
6. Both /get_movie and /get_subtitle will return a json string
7. JavaScript will take the json string and modify the innerhtml of the video player and title to match the files
