# Basic python article web scraper.

This program uses BeautifulSoup to find the title and main text of ABCNews sports articles. Then the main body of the article is sent to ChatGPT and summarized in 50 words or less using the **OpenAI API**. Finally, a file with the name of the original article is created in **'Data > processed'** that contains the AI response.

## Requirements

- Python 3.9
- BeautifulSoup library (`pip install beautifulsoup4`)
- Requests library (`pip install requests`)
- OpenAI library (`pip install openai`)
- Pytest library (`pip install pytest`)
- Validators library (`pip install validators pytest`)

## Setup Instructions
* In a compatible terminal environment for executing Conda commands, initialize the conda environment with the **requirements.yml** file.
~~~bash
conda create --name env_name --file requirements.yml
~~~

* Create a text file named **'input.txt'** within the folder **'Data > raw'** and fill it with ABCNews Sports article URLs.
  * <span style="font-size: small; color: grey;">One URL per line.</span>

* Within the **module_3** folder, decrypt the **.env** file containing the OpenAI API key using the password sent over email.
~~~bash
cd module_3

openssl enc -d -aes-256-cbc -in .env.enc -out .env
~~~
* You will be prompted to enter the decryption password to access the decrypted **.env** file.
  * Ensure the **.env** file is in module_3 before running.

* Run the Python program **run.py**
~~~bash
python3 run.py
~~~


## LLM API Usage
To setup a program that makes API calls with OpenAI's ChatGPT...
### Get an OpenAI API key:
* Go to [OpenAI's Developer Platform](https://platform.openai.com/docs/overview) and create an account.
  * Click **Sign up** in the top right corner.
  * Create an account.
* Navigate to the [API keys](https://platform.openai.com/api-keys) tab.
  * The API keys tab is on the left side of the screen in a bar that pops out.
* Click "Create new secret key" and copy the key it gives you somewhere for later.
### Create **.env** File
* Create a file named ".env"
  * Put the following in the **.env** file
~~~makefile
OPENAI_API_KEY=sk-yourkey
~~~
### <span style="color:red;">Warning: Do not put API key on github</span>
* Create a **.gitignore** file so your private key will not go to github.
  * Put the following in the **.gitignore** file
~~~bash
directory/of/file/.env
~~~
* Encrypt the **.env** you post on github.
  * Run this command in the terminal
~~~bash
openssl enc -aes-256-cbc -in .env -out .env.enc
~~~
* You will be prompted to enter a password for encryption
#### To decrypt file
~~~bash
openssl enc -d -aes-256-cbc -in .env.enc -out .env
~~~
### Code function or module that utilizes API
Example:
~~~python
# Function takes in a string that will act as user response then using a prompt, calls OpenAI's API and outputs an AI response
def get_ai_response(text):
    prompt = "Summarize the following article in less than 50 words." # Create a custom prompt for the AI
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo", # Enter desired gpt model
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": text},
        ]
    )
    return completion.choices[0].message.content
~~~