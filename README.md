# QuoterX

This project endeavors to develop a Twitter bot programmed to share a diverse array of inspirational quotes daily, scheduled precisely for 9:00 AM. Leveraging the ZenQuotes API alongside the Tweepy library, the bot will seamlessly curate and deliver thought-provoking content to engage and uplift its audience.

## Prerequisites

Before running the script, make sure you have the following:

1. Python 3 installed
    - If not installed, click [here](https://www.python.org/downloads/) to download the latest version of Python.

2. Tweepy library installed

    Run the following command in cmd if tweepy is not installed.    
    ```cmd
    pip install tweepy
    ```

3. Tokens and API Keys for Twitter Account Authentication and Access
    - Click [here](https://developer.twitter.com/en) to learn more about Twitter's Developer Platform

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/anujeshify/QuoterX.git
    ```

2. Install the required libraries:

    ```cmd
    pip install -r requirements.txt
    ```

3. Create a `config.py` file and add your Twitter API keys and tokens:

    ```python
    CONSUMER_KEY = 'your_consumer_key'
    CONSUMER_SECRET = 'your_consumer_secret'
    ACCESS_TOKEN = 'your_access_token'
    ACCESS_TOKEN_SECRET = 'your_access_token_secret'
    BEARER_TOKEN = 'your_bearer_token'
    ```

4. Run the script in Command Prompt:

    ```cmd
    python QuoterX.py
    ```

5. If you want to keep the Python Script running as a background process, then use the following command

    ```cmd
    start /B python QuoterX.py
    ```

5. If you want to stop the Python Script, then first find the Process ID of the Python Script that is runnning using the following command

    ```cmd
    tasklist | findstr "python"
    ```
This will show the python process with its PID (Process ID)

6. Kill the process by using the following command on cmd

    ```cmd
    taskkill /PID <process id> /F
    ```

Replace "Process id" with the PID displayed.
A Demonstration of the same is given below -
![ProcessKill](PATH)

## How it works

1. The script fetches a random quote from the [ZenQuotes API](https://zenquotes.io/).

2. If the author of the quote is "Unknown", it fetches another random quote until a valid author is obtained.

3. The script creates a tweet with the quote and author.

4. The tweet is posted using the Tweepy library and your Twitter API credentials.

5. The script runs continuously and checks the current time every second.

6. If the current time is 9:00 AM, it tweets a new quote.

## Documentation of Tools Used

* [Python](https://docs.python.org/3/) - Python Programming Language
* [Tweepy](https://docs.tweepy.org/en/stable/index.html) - Tweepy is a publicly available open-source Python library.
* [ZenQuotes API](https://docs.zenquotes.io/zenquotes-documentation/) - The ZenQuotes API is an incredibly easy to use data feed for your website or app.
* [Twitter Developer Platform](https://developer.twitter.com/en/docs) - Guides and reference materials to use Twitter Developer Platform


## Authors

* **Anujesh Bansal** - [anujeshify](https://github.com/anujeshify)

## Contribution
Contributions to this project are welcome! If you have any suggestions, bug fixes, or improvements, please feel free to open an issue or submit a pull request.
For any queries reach me at [anujeshbansaltoo@gmail.com](anujeshbansaltoo@gmail.com)

## Acknowledgments
Special thanks to the contributors and developers of the libraries and tools used in this project, including tweepy and ZenQuotes API.