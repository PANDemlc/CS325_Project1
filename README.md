# Basic python article web scraper.

This program uses BeautifulSoup to find the title and main text of ABCNews sports articles. Then the main body of the article is sent to chatGPT and summarized in 50 words or less using the **OpenAI API**. Finally, a file with the name of the original article is created in **'Data > processed'** that contains the AI response.

## Instructions
* In a compatible terminal environment for executing Conda commands, initialize the conda environment with the **requirements.yml** file.
~~~bash
conda create --name env_name --file requirements.yml
~~~
* Create a text file named **'input.txt'** within the folder **'Data > raw'** and fill it with ABCNews Sports article URLs.
  * <span style="font-size: small; color: grey;">One URL per line.</span>
* Within the **module_3** folder, decrypt the **.env** file containing the OpenAI API key using the password sent over email.
~~~bash
openssl enc -d -aes-256-cbc -in .env.enc -out .env
~~~
* You will be prompted to enter the decryption password to access the decrypted **.env** file.
  * Ensure the **.env** file is in module_3 before running.
* Run the Python program **run.py**
~~~bash
python3 run.py
~~~
