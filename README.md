This is a simple Chatbot written in Python based on NLP Bot by Ed Bullen at https://github.com/edbullen/NLPBot/  
The bot uses some NLP with Python [NLTK](http://www.nltk.org/) and basic Machine Learning capabilities to demonstrate Sentence Classification using the NLTK and [scikit-learn](http://scikit-learn.org/stable/).  
The Stanford CoreNLP package, written in Java, is also used to parse grammar and extract sentence topics, subject, object etc.

## Python Library Dependencies ##
  
+ [sqlite3](https://docs.python.org/2/library/sqlite3.html)  
+ [nltk](http://www.nltk.org/install.html) 
+ [numpy](http://www.numpy.org/)
+ [pandas](http://pandas.pydata.org/)
+ [scipy](https://www.scipy.org/)
+ [scikit-learn](http://scikit-learn.org/stable/)
+ [Stanford CoreNLP Parser](https://stanfordnlp.github.io/CoreNLP/) This is a Java package that needs to be download and located in suitable dir for future ref
+ [Java](https://java.com/en/download/help/linux_x64rpm_install.xml) - tested with Java 8, java version "1.8.0_131"

## Files and Components ##

**Core Functionality**
+ `chatbot.py` - main ChatBot library 
+ `utils.py` - generic function utilities used by ChatBot (config, DB conn etc) 
+ `features.py` - library for extracting features from sentences using NLTK
+ `botserver.py` - Multi-Threaded server to allow multiple clients to connect to the ChatBot via network sockets
+ `simpleclient.py` - Simple network sockets client to connect to `botserver`

Default `botserver.py` logging location is 
```
./log/server.log
```

**Setup and Test**
+ `./config/config.ini` - template config file, requires editing before starting the chatbot for the first time. 
+ `database_setup.py` - drop and recreate the database tables (existing data gets lost).
+ `database_initialize.py` - initialize the server with some data.
+ `mlClassGenerateRfModel.py` - generate a scikit-learn Random Forest Model for sentence classification based on input CSV.  Default output file-name is "**RFmodel.ml**" 

## Install and Setup ##

Install the dependencies and modify the config.ini 

#### Starting the BotServer ####
The chatbot can be started with a multi-threaded server scheduler (`botserver.py`) that listens for connections on a TCP port. This is a very simple "bare-bones" multi session framework with no authentication and just relying on TCP sockets for connection.

Remote TCP Socket Connection requests are given a thread and their own session connection.

The botserver gives each session a connection to the shared database server.

```
python botserver.py &
```

#### Logging ####
Bot server output is logged to
```
./log/botserver.log
```
#### Stopping the Server ####
```
CTRL+C 
```
#### Local Client Connect #####
```
python simpleclient.py -a localhost -p 9999
```
#### Remote Client Connect #####

Make sure the botserver port is allowed through the firewall.
```
python simpleclient.py -a <ip_or_hostname> -p 9999
```
