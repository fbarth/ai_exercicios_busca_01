# Code for Artificial Intelligence subject

We are using this project to support actitivies related to the Artificial Intelligence subject that is part of an undergraduate Computer Science course. 

The topics discussed in the course are: 

1.	Artificial Intelligence Introduction;
2.	Intelligent Agents;
3.	Solving Problems by Searching;
4.	Informed Search Methods;
5.	Game Playing;
6.	Reinforcement Learning (Here, we present the concept of Learning from Observations, Supervised Learning and Unsupervised Learning. However, We have a specific course to discuss those topics.).

## How this project is structured 

We have four (4) folders: 

* *search*: this folder has implementations related to solving problem by searching, and informed search methods. We suggest to start from this folder in order to understand all the implementations (search, games, and reinLearn).

* *games*: this folder keeps source code related to game playing.

* *reinLearn*: this folder has source code related to reinforcement learning. Some examples are using the project [Gym](https://gym.openai.com/).

## How to setup the environment

To avoid any configuration problems, we recommend creating a virtual environment with python:

````bash
python3 -m virtualenv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
````

To quit the virtual environment, type `deactivate`. If you already have the virtual environment configured then type `source venv/bin/activate`. 


