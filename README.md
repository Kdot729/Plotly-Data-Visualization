# Plotly Data Visualization

# Table of Contents
<ol>
    <li>
        <a href="#project-description">Project Description</a>
    </li>
    <li>
        <a href="#installation-requirements">Installation Requirements</a>
        <ul>
            <li>Without Docker
                <ul>
                    <li><a href="#mac/linux">Mac/Linux</a></li>
                    <li><a href="#windows">Windows</a></li>
                </ul>
            </li>
            <li><a href="#with-docker">With Docker</a></li>
        </ul>
    </li>
</ol>

# Project Description
Program uses Plotly to create data visualizations for NFT sales from 10KTF

# Installation Requirements
- This program ran on python 3.12.0
- Using an older version of python might not work because their might be package conflicts with requirements.txt
- Either download python 3.12.0, use Docker or install the packages without using requirements.txt with
~~~
python -m pip install flask pandas plotly
~~~

## Without Docker

<!--Note Need to explicitly use h3 to link to this header -->
<h3 id="mac/linux">Mac/Linux</h3>

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
python -m pip install -r requirements.txt
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
python -m pip install -r requirements.txt
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
