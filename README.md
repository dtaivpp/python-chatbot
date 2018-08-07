# Rasa Chatbot Demo

<<<<<<< HEAD

###What the Chatbot is
  This is a chatbot built with the Rasa stack. It uses the Rasa NLU unit along with the Rasa Core to first interperete what is being asked of it and then to decide on the best action based on that. 
=======
# Introduction
After searching around on the internet we could not find anything beyond the most basic of examples of a chatbot so we have set out to create our own. This demo is being written from the usecase of a Christian University that is trying to engage with students providing useful information 24/7.

## Installation
While this demo is being written from the perspective of developing on Windows 10 environment the principlals are the same across platforms. 
1. Download and Install Python 3.6
2. Clone this repository
3. For those on Windows download and install Microsoft Visual C++ 14.0
4. Navigate to the directory you cloned to and run 
    `pip install -r reuqirements.txt`
5. Download the english spacy model with the command below (Note the medium one used takes up 1Gb)  
  - **If you are on windows you need to do this from an administrative shell (search for cmd, right click and select "Run as Administrator")  
    `python -m spacy download en_core_web_md`  
6. Then link that to the english model  
    `python -m spacy link en_core_web_md en -f`
  - **If you run into problems here we found rolling back pip and then re-running helped  
      `python -m pip install pip 9.0.3`  
7. Then run the following command to get the simple intent creation page  
    `npm install rasa-nlu-trainer`  

That is it (as far as installation is concerned that is). Continue on to see how we will use thse

## Training the Rasa NLU
The first thing to do when going to train the NLU is to load up some data into data/data.json. The quickest way to do this is using the rasa nlu trainer we insalled in step 7 of the last section. You do this by running the following line from the command line.  
    `rasa-nlu-trainer`  
>>>>>>> develop
