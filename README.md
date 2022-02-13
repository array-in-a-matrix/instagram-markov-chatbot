# Instagram Markov Chatbot

An Instagram chat bot which generates new sentences and sends them in direct messages.
Used code from [here](https://towardsdatascience.com/simulating-text-with-markov-chains-in-python-1a27e6d13fc6) as a base.

## Configuration

### JSON

- **`username`** / **`password`**
    - In the `login.json` file please place your account username and password in the `username` and `password` entries respectively.

- **`dataset`**
    - This is the path to the text file which will be used to generate messages.

- **`recent`**
    - The bot will message the top most recent *n<sup>th</sup>* chat, where the *n<sup>th</sup>* chat is the number chosen in the `recent` entry.
- **`interval`**
    - The `interval` entry controls how often the bot sends a message in seconds.

### Command-line

- **`headless`**
    - If you want to run the program headlessly append `MOZ_HEADLESS=1` to the beginning of the command.
- **`message length`**
    - Optional argument (integer) that determine the length of the sentence. If no argument is provided or a non integer number was given, messages will generate with variable length between 1 and 30.