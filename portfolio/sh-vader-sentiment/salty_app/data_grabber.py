import requests
import html
import re
import os
import psycopg2
from dotenv import load_dotenv
from sql_query_function import create_comment_table
from sql_query_function import populate_comment_table_query


# Defining "wrangle" Function
def wrangle(jsonin):
    # print(type(jsonin))
    if 'dead' in jsonin:
        return {}
    if 'kids' in jsonin:
        jsonin.pop('kids')
    jsonin.pop('time')
    # get rid of html tags and quotes
    # regex code from:
    # https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string

    # remove snippets of other people's comments in comments
    # do this before unescape to differentiate html tags from user
    # inputted ">"s
    if 'text' in jsonin:
        # print('Cleaning comment with ID:',jsonin['id'])
        # print(jsonin['text'])
        cleanr = re.compile('&gt;.*<p>')
        jsonin['text'] = re.sub(cleanr, '', jsonin['text'])
        # print(jsonin['text'])
        jsonin['text'] = html.unescape(jsonin['text'])
        # make ends of paragraphs newlines
        jsonin['text'] = jsonin['text'].replace('<p>', ' ')
        # print(jsonin['text'])
        # clean all other html tags
        cleanr = re.compile('<.*?>')
        jsonin['text'] = re.sub(cleanr, '', jsonin['text'])
        # print(jsonin['text'],'\n')
        return jsonin
    else:
        return {}


if __name__ == "__main__":
    # env
    ENV_PATH = os.path.join(os.getcwd(), '.env')
    load_dotenv(ENV_PATH)

    # Elephant SQL -- PostgreSQL Credentials
    ELE_DB_USER = os.getenv('ELE_DB_USER')
    ELE_DB_NAME = os.getenv('ELE_DB_NAME')
    ELE_DB_PW = os.getenv('ELE_DB_PW')
    ELE_DB_HOST = os.getenv('ELE_DB_HOST')

    # Creating Connection Object
    conn = psycopg2.connect(dbname=ELE_DB_NAME,
                            user=ELE_DB_USER,
                            password=ELE_DB_PW,
                            host=ELE_DB_HOST)

    # Creating Cursor Object
    cursor = conn.cursor()

    # Get input from user on which id to start from
    print('Remember: Ctrl+C will stop adding items to the database.')
    maxitem = input('What ID to start from? (leave blank to use latest)')
    if not maxitem:
        url = "https://hacker-news.firebaseio.com/v0/maxitem.json"
        maxitem = requests.get(url)
        maxitem = maxitem.json()
        maxitem = int(maxitem)
    else:
        maxitem = int(maxitem)

    i = 0
    while True:
        try:
            url = f'https://hacker-news.firebaseio.com/v0/item/{maxitem}.json'
            item = requests.get(url)
            item_json = item.json()
            if not isinstance(item_json, dict):
                maxitem -= 1
                continue
            # Catch in case comment doesn't have text for some reason
            item_json = wrangle(item_json)
            # print(item_json)
            if 'type' in item_json:
                if item_json['type'] == "comment":
                    # print('adding to database')
                    # Check to make sure entry isn't in database already
                    # create_user_table(cursor, conn)
                    create_comment_table(cursor, conn)

                    i, maxitem = populate_comment_table_query(cursor,
                                                              conn,
                                                              i,
                                                              item_json,
                                                              maxitem)

            maxitem -= 1
        except KeyboardInterrupt:
            print(f'{i} records added to database.')
            break
