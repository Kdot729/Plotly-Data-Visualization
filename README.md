# Plotly Data Visualization

# Table of Contents
- Project Description
- Installation
    - Without Docker
    - With Docker

---

# Project Description
Program uses Plotly to create data visualizations for NFT sales from 10KTF

# Installation
- This program ran on python 3.12.0
- Using an older version of python might not work because their might be package conflicts with requirements.txt
- Either download python 3.12.0, use Docker or install the packages without using requirements.txt with
~~~
python -m pip install flask pandas plotly
~~~

## Without Docker

### Mac/Linx
- Create virtual environment named .venv
~~~
python -m venv .venv 
~~~

- Activate virtual environment
~~~
source .venv/bin/activate
~~~

- Install packages
~~~
pip install -r requirements.txt
~~~

- Run flask in debug mode
~~~
python -m flask --debug run
~~~ 

### Windows
- Create virtual environment named .venv
~~~
python -m venv .venv 
~~~

- Activate virtual environment
~~~
.venv\Scripts\Activate
~~~

- Install packages
~~~
pip install -r requirements.txt
~~~

- Run flask in debug mode
~~~
python -m flask --debug run
~~~ 

## With Docker
- Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Make sure Docker Desktop is running
- Build the image and run the container
~~~
docker-compose up --build
~~~
