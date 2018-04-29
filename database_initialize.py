import chatbot   # Test the ML classification routing in chatbot.py
import features  # custom fn extract features from a sentence
import utils

import sys
import profile

conf = utils.get_config()

DBFILE = conf["Sqlite"]["filepath"]

statements = [
"Python is an interpreted interactive object-oriented programming language.",
"The Python Software Foundation is an independent non-profit organization that holds the copyright on Python versions 2.1 and newer.",
"Python is a high-level general-purpose programming language that can be applied to many different classes of problems.",
"The latest Python source distribution is always available from python.org at https://www.python.org/downloads/",
"The standard documentation for the current stable version of Python is available at https://docs.python.org/3/",
]

print("Connecting to database...")
connection = utils.db_connection(DBFILE)
cursor =  connection.cursor()
print("...connected")
for statement in statements:
	print("Storing the statement: {0}".format(statement))
	chatbot.store_statement(statement, cursor)
connection.commit()
print("done")