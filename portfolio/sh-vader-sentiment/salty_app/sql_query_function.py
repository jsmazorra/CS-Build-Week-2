import os
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv


# Load environment variables from .env
load_dotenv()


# Defining "create_comment_table" Function
def create_comment_table(cursor, conn):
    print("-----------------")

    create_table_query = '''
        CREATE TABLE IF NOT EXISTS salty_db_2 (
            comment_id INT,
            author_name VARCHAR,
            comment_text VARCHAR,
            salty_comment_score_pos FLOAT,
            salty_comment_score_neg FLOAT,
            PRIMARY KEY (comment_id)
            )
            '''
    cursor.execute(create_table_query)
    conn.commit()


# Defining "populate_comment_table_query" Function
def populate_comment_table_query(cursor, conn, i, item_json, maxitem):
    query = f'''
        SELECT
            comment_id
        FROM salty_db_2
        WHERE comment_id={maxitem}
        '''
    cursor.execute(query)
    record = cursor.fetchone()
    if record is None:
        print(f'Adding comment with id {maxitem} to database')
        # The record isn't found in the database
        # add the record to the database
        query = '''
        INSERT INTO salty_db_2 (comment_id, author_name, comment_text)
        VALUES %s
        '''
        execute_values(
            cursor,
            query,
            [
                (
                    str(item_json['id']),
                    item_json['by'],
                    item_json['text']
                )
            ]
        )
        conn.commit()
        i += 1
    else:
        # The record is already in the database
        # Alert the console
        print(f"WARNING: Duplicate entry {maxitem} found in database!")
    return i, maxitem


def fetch_query_comments(query):
    """
    Creates a connection to a database, returns query from comments table
    as a list of dictionaries
    Input: query = string
    """
    # Elephant SQL -- PostgreSQL Credentials
    ELE_DB_USER = os.getenv('ELE_DB_USER')
    ELE_DB_NAME = os.getenv('ELE_DB_NAME')
    ELE_DB_PW = os.getenv('ELE_DB_PW')
    ELE_DB_HOST = os.getenv('ELE_DB_HOST')

    # Creating Connection Object
    conn = psycopg2.connect(dbname=ELE_DB_NAME,
                            user=ELE_DB_USER,
                            password=ELE_DB_PW,
                            host=ELE_DB_HOST
                            )
    # Creating Cursor Object
    cursor = conn.cursor()
    # Fetch comments query
    query = query
    # Execute query
    cursor.execute(query)
    # Query results
    comments = list(cursor.fetchall())
    # Key-value pair names for df columns
    columns = ["comment_id",
               "username",
               "comment_text",
               "score_pos",
               "score_neg"]
    # List of tuples to DF
    df = pd.DataFrame(comments, columns=columns)
    print(type(df))
    # DF to dictionary
    pairs = df.to_json(orient='records')
    print(type(pairs))
    # Closing Connection
    conn.close()

    return pairs


def fetch_query(query, columns):
    """
    Creates a connection to a database, returns query from users table
    as a list of dictionaries
    Input: query = string
    """
    # Elephant SQL -- PostgreSQL Credentials
    ELE_DB_USER = os.getenv('ELE_DB_USER')
    ELE_DB_NAME = os.getenv('ELE_DB_NAME')
    ELE_DB_PW = os.getenv('ELE_DB_PW')
    ELE_DB_HOST = os.getenv('ELE_DB_HOST')

    # Creating Connection Object
    conn = psycopg2.connect(dbname=ELE_DB_NAME,
                            user=ELE_DB_USER,
                            password=ELE_DB_PW,
                            host=ELE_DB_HOST
                            )
    # Creating Cursor Object
    cursor = conn.cursor()
    # Fetch comments query
    query = query
    # Execute query
    cursor.execute(query)
    # Query results
    comments = list(cursor.fetchall())
    # Key-value pair names for df columns
    columns = columns
    # List of tuples to DF
    df = pd.DataFrame(comments, columns=columns)
    print(type(df))
    # DF to dictionary
    pairs = df.to_json(orient='records')
    print(type(pairs))
    # Closing Connection
    conn.close()

    return pairs
