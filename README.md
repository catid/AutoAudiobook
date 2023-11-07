# OpenAI Audiobook Generator

So today OpenAI released really good text-to-speech features, the faster `gpt-4-1106-preview` model, JSON mode, April 2023 knowledge cut-off, and lots of other good stuff.  To experiment with what these things can do, I "wrote" this project while on the elliptical for an hour using the ChatGPT (GPT-4) app on my cellphone, then pasted the Python scripts into this repo.  I pushed this code to GitHub a few hours later after stringing it all together in the Cursor fork of Visual Studio code, which uses GPT-4 to assist with software development.

It cost me $1 to test it.  And it works!

The cool thing is that each character gets their own unique voice actor.  There's a good example at 5:00 in the output:

[Example output audiobook](https://soundcloud.com/chris-taylor-12673225/output-audiobook?si=0343e4dc64cc4098a9b34afb62506427&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing#t=5%3A06)

## Setup

Install Python 3.10 or newer and Conda.

Create a conda environment:

```bash
conda create -n book python=3.10
conda activate book
pip install -r requirements.txt
```

Modify the `api_key.py` file to specify your OpenAI key, which you generate here: https://platform.openai.com/api-keys


## Split the audiobook into context-sized chunks

```bash
conda activate book
python 1_split.py
```

This will create the `split` folder with text files.


## Identify characters

```bash
conda activate book
python 2_chars.py
```

This will create the `assigned` folder with JSON files containing all the dialog assigned to different speakers.


## Cast characters

```bash
conda activate book
python 3_cast.py
```

This will parse the `assigned` folder and produce a JSON file `casting.json` you can edit to select voice actors.  Defaults are selected by round-robin for simplicity.


## Speak the parts

```bash
conda activate book
python 4_speak.py
```

This will read the `casting.json` and the `assigned` folder and produce .mp3 chunks using OpenAI TTS in the `speech` folder.


## Generate the audiobook

```bash
conda activate book
python 5_assemble.py
```

This will read the .mp3 chunks from the `speech` folder and assemble them end-to-end into a long .mp3 audiobook.  Congrats it's done!


## Discussion

I tried to use this with a more adult book, and the result was that GPT-4 is too censored to process the text.  It straight up refuses to repeat the words 'fuck' or 'whore', for example, so the way that I'm doing the assignment of voice actors to the parts automatically won't work for some books.

Sometimes it fails to assign the correct character to a passage, or it drops a line.  So for practical use you should probably inject the missing lines back in by hand and modify the character names where they are wrong.

Also the TTS API is very slow in high-definition mode, so for now it's impractical for a full book.  Probably you'd want to use the regular version for now or wait for it to speed up.
