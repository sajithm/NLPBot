import os

import warnings
warnings.filterwarnings("ignore")  # suppress warnings when we try to drop non-existant tabs

import utils  # General utils including config params and database connection

conf = utils.get_config()

DBFILE = conf["Sqlite"]["filepath"]

def try_drop(cursor,table_name):
    SQL = 'DROP TABLE IF EXISTS ' + table_name
    print(SQL)
    cursor.execute(SQL)

print("Configuring Tables for database: {0}".format(DBFILE))
print("\n** ALL EXISTING TABLES AND DATA WILL BE LOST **\n")

response = utils.query_yes_no("Continue?")

if response:
    print("Connecting to database...", end=" ")
    connection = utils.db_connection(DBFILE)
    cursor = connection.cursor()
    print("connected.")
    
    print("\nCreating words table:")
    try:
        try_drop(cursor, "words")
        SQL = 'CREATE TABLE words ( hashid TEXT UNIQUE, word TEXT UNIQUE )'
        print(SQL)
        cursor.execute(SQL)
    except Exception as e:
        print("\n** ERROR **", e)
        
    print("\nCreating sentences table:")
    try:
        try_drop(cursor, "sentences")
        SQL = 'CREATE TABLE sentences (hashid TEXT UNIQUE, sentence TEXT, used INT DEFAULT 0 NOT NULL)'    
        print(SQL)
        cursor.execute(SQL)
    except Exception as e:
        print("\n** ERROR **", e)
        
    print("\nCreating statements table:")
    try:
        try_drop(cursor, "statements")
        SQL = 'CREATE TABLE statements (sentence_id TEXT, word_id TEXT, class TEXT)'    
        print(SQL)
        cursor.execute(SQL)
    except Exception as e:
        print("\n** ERROR **", e)
        
    print("\nAdding statements table INDEXES:")
    try:
        indexes = ['CREATE INDEX statements_sentenceid_idx ON statements(sentence_id)',
                   'CREATE INDEX statements_wordid_idx ON statements(word_id)']
        for index in indexes:
            SQL = index
            print(SQL)
            cursor.execute(SQL)
    except Exception as e:
        print("\n** ERROR **", e)
        
    print("\nCreating associations table:")
    try:
        try_drop(cursor, "associations")
        SQL = 'CREATE TABLE associations (word_id TEXT NOT NULL, sentence_id TEXT NOT NULL, weight REAL NOT NULL)'
        print(SQL)
        cursor.execute(SQL)
    except Exception as e:
        print("\n** ERROR **", e)
    
    print("\nAdding associations table INDEXES:")
    try:
        indexes = ['CREATE INDEX associations_wordid_idx ON associations(word_id)',
                   'CREATE INDEX associations_sentenceid_idx ON associations(sentence_id)']
        for index in indexes:
            SQL = index
            print(SQL)
            cursor.execute(SQL)
    except Exception as e:
        print("\n** ERROR **", e)
        
    print("\nCreating results table:")
    try:
        try_drop(cursor, "results")
        SQL = 'CREATE TABLE results (sentence_id TEXT, sentence TEXT, weight REAL)'
        print(SQL)
        cursor.execute(SQL)
    except Exception as e:
        print("\n** ERROR **", e)
        
    print("\nDone.")
##############################    
    
else:
    exit(0)