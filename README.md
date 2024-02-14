# Basic python article web scraper.

This program uses BeautifulSoup to find the title and main text of ABCNews sports articles for analysis and utilization in other projects.

## Instructions
* In a compatible terminal environment for executing Conda commands, initialize the conda environment with the **requirements.yml** file.
~~~bash
conda create --name env_name --file requirements.yml
~~~
* Create a text file named **'input.txt'** within the same folder as **project.py** and fill it with ABCNews Sports articles URLs.
  * <span style="font-size: small; color: grey;">One URL per line.</span>
* Run the Python program **project.py**
~~~bash
python3 project.py
~~~

If the **Articles** folder does not already exist, it will be created. Then the article titles and main text bodies from the URLs in **input.txt** will each be put in their own text files within the **Articles** folder.