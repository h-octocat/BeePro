# BeePro
A suite of spelling bee tools that won me the Manhattan spelling bee. Get the full story at henryks.net.

## Setup
BeePro is only compatible with Windows, MacOS, and Linux. Other operating systems won't be able to fully run BeePro.

The latest version of python is reccomended to run BeePro. You can install python at [python.org](https://python.org).

In order to setup, first install the requirements:
```
pip install -r requirements.txt
```

If you would like the dictionary functionality, go to the Merriam Webster dictionary api at [dictionaryapi.com](https://dictionaryapi.com) and setup an API key. Once you get an API key, create a .env file and add `DICT_API=YOUR_API_KEY`, replacing "YOUR_API_KEY" with your actual API key.

If you do not set up a dictionary key, all requests for a definition will return `definition error`. 

## Storing words
All setd of words should be stored as a .txt text file, with each word being seperated by a new line. Here's an example file:

```
Idiosyncratic
Apocryphal
Aniseikonia
```

If a word has multiple acceptable spellings, use "OR" to seperate them like so:

```
anemic OR anaemic
sauerkraut OR sourcrout
steinkirk OR steenkirk
```

## Features
BeePro comes with three python scripts: study, test, and removedupes.

Removedupes.py does as the name suggests, removing duplicate words in a text file. 

Study.py helps you study a list of words. It will tell you how to spell a word, read it multiple times, and give you its definition. Then, it will ask you how to spell it.

Test.py drills you on all the words, reading them and asking you to spell them. It has the option to save the words you got wrong in a seperate file at the end.
