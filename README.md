# Instagram Markov Chatbot

An Instagram chat bot which generates new sentences from direct messages.
Currently bot uses a sentences from `dataset.txt` file to generate new sentences.
Code takes an optional argument (integer) that determine the length of the sentence.
Used code from [here](https://towardsdatascience.com/simulating-text-with-markov-chains-in-python-1a27e6d13fc6) as a base.
In the `login.json` file please place your account username and password in the `username` and `password` entries respectively.
The bot will message the top most recent *n<sup>th</sup>* chat, where the *n<sup>th</sup>* chat is the number chosen in the `recent` entry.
If you want to run the program headlessly append `MOZ_HEADLESS=1` to the beginning of the command.