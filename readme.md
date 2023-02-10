# Service for learning english using examples

The HappyEnglish app with which you can search for fragments from TED educational videos with the specific words and phrases. The point of this app: make learning English easier -- you can find new words in the context using the app. 

## Web app


Check `requirments.txt` for required packages.

Go to the directory with Flask web-application:

``cd happy_english_service``

Just print in console to launch the app: 
`` python ./run_service.py ``

And go to the ``http://127.0.0.1:5000/ `` in your browser. 

## Appendix: Making new database with subtitles

In case you want to make db bigger by downloading more subtitles, you can use tools directory:

``cd tools``

* ``create_database.py`` - creates new database using the command (the argument is the path to db):

``python ./create_database.py ../database.sqlite``

* ``fill_database.py`` - should be used to fill database with subtitles (the argument is the path to db):

``python ./fill_database.py ../database.sqlite``
