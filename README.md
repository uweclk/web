# T+ Web

This is the web code for the T+ application. This repository holds the Flask server and will soon hold the front-end code.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them

* [Anaconda](https://www.anaconda.com/distribution/) - Anaconda is an all-in-one machine learning in Python package.
* Use git clone or some other way to get this repository on your computer.

### Installing

Open the Anaconda Prompt (on Windows type Anaconda Prompt into the start menu search bar), use this command prompt to run the following commands.

Create a virtual environment for this project. This will make a type of container to section off all the packages we need for this project.
```
mkvirtualenv uweclk-web
```
At this point you will see both (base) and (uweclk-web) next to your command prompt line. This means that both the base and uweclk-web virtual environments are activated. Run the following command twice until there are no activate virutal environments.
```
conda deactivate
```
Now with no activated virtual environments, activate the uweclk-web environment:
```
workon uweclk-web
```
You will now see (uweclk-web) to the left of your command prompt line. This means our virtual environment is activated.

Next, navigate to wherever you downloaded this repository. On my computer this command is:
```
cd ./projects/uweclk/web
```
Use the conda package manager to download gensim. We use the conda package manager here because gensim has complicated and old dependencies that only conda installs correctly.
```
conda install gensim
```
Use the Python package manager(pip) to download all the required libraries for our project:
```
pip install -r requirements.txt
```
Run the Flask server:
```
python ./application.py
```
You should now have a running flask server on your computer. Access the website by putting this in your browser:
```
http://127.0.0.1:5000/
```

## Deployment

We are currently hosting this application on AWS. You can see the live version [here](http://uweclk-env.h32szuaur7.us-east-1.elasticbeanstalk.com/).

## Built With

* [Flask](https://www.palletsprojects.com/p/flask/) - The web framework used
* [pip](https://pip.pypa.io/en/stable/) - Dependency Management

## Authors

* **Colin Reilly** - *Initial work* - [colin.world](https://www.colin.world)
