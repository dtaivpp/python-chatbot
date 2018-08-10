# Rasa Chatbot Demo

# Introduction
After searching around on the internet we could not find anything beyond the most basic of examples of a chatbot so we have set out to create our own. This demo is being written from the usecase of a Christian University that is trying to engage with students providing useful information 24/7.

## Installation for Windows 10
While this demo is being written from the perspective of developing on Windows 10 environment the principlals are the same across platforms. 
1. Download and Install Python 3.6
2. Clone this repository
3. For those on Windows download and install Microsoft Visual C++ 14.0
4. Navigate to the directory you cloned to and run 
    `pip install -r requirements.txt`
5. Download the english spacy model with the command below (Note the medium one used takes up 1Gb)  
  - **On windows you need to do this from an administrative shell (search for cmd, right click and select "Run as Administrator")  
    `python -m spacy download en_core_web_md`  
6. Then link that to the english model  
    `python -m spacy link en_core_web_md en -f`
  - **If you run into problems here we found rolling back pip and then re-running helped  
      `python -m pip install pip 9.0.3`  
7. Then run the following command to get the simple intent creation page  
    `npm install rasa-nlu-trainer`  

## Installation Linux (tested on Ubuntu 18.04.1 LTS Minimal install)
Here we are simply installing on this system for running the bot not for training so we will be leaving off the intent creation page. 
1. Download and Install Python 3.6
2. Clone this repository
4. Navigate to the directory you cloned to and run 
    `sudo pip3 install -r requirements.txt`
5. Download the english spacy model with the command below (Note the medium one used takes up 1Gb)  
  - **If you are on windows you need to do this from an administrative shell (search for cmd, right click and select "Run as Administrator")  
  - **If using linux this must be run as a super-user
    `sudo python3 -m spacy download en_core_web_md`  
6. Then link that to the english model  
    `sudo python3 -m spacy link en_core_web_md en -f`
  - **If you run into problems here with pip3 not importing main we found the following command was able to relsove some of these problems
      `sudo python3 -m pip uninstall pip && sudo apt install python3-pip --reinstall`  

## Training the Rasa NLU
The first thing to do when going to train the NLU is to load up some data into data/data.json. The quickest way to do this is using the rasa nlu trainer we insalled in step 7 of the last section. You do this by running the following line from the command line.  
    `rasa-nlu-trainer`  

Next you will want to train the nlu model on your custom inpytents. To do so from the command line you will need to run `python train_nlu.py` which will train the NLU to recognize the intents and any entities that are associated. This will persist in /models/nlu/default/nlu.

## Pipeline for the BOT (todo: Expand on steps)
1. Install the required depenencies
2. Training the Rasa NLU
3. Training the core with the dialogue stories (run `python train_rasa_core.py`)
4. At this point you can either load the bot into slack with slack_handler.py or train further using train_rasa_terminal.py