# salty_app/routes/home_routes.py
from flask import Blueprint
from salty_app.sql_query_function import fetch_query_comments, fetch_query


# Instantiate new blueprint object
home_routes = Blueprint("home_routes", __name__)


# "index" Route
@home_routes.route("/")
def index():
    return """<xmp>
    WELCOME TO SALTIEST!
    \n
    YOU ARE CURRENTLY IN THE DATA LANDING PAGE. SEE BELOW FOR RETRIEVAL INSTRUCTIONS.
    \n
    \n
    \n
    VISIT THE FOLLOWING ADDRESSES TO RETRIEVE KEY VALUE PAIR DATA(Local):
    \n
    http://localhost:5000/home
    \n
    http://localhost:5000/top20_saltiest_users
    \n
    http://localhost:5000/top20_sweetest_users
    \n
    http://localhost:5000/top10_commenters
    \n
    http://localhost:5000/top100_salty_comments
    \n
    http://localhost:5000/top100_sweetest_comments
    \n
    \n
    \n
    VISIT THE FOLLOWING ADDRESSES TO RETRIEVE KEY VALUE PAIR DATA(Heroku):
    \n
    https://saltyapp.herokuapp.com/home
    \n
    https://saltyapp.herokuapp.com/top20_saltiest_users
    \n
    https://saltyapp.herokuapp.com/top20_sweetest_users
    \n
    https://saltyapp.herokuapp.com/top10_commenters
    \n
    https://saltyapp.herokuapp.com/top100_salty_comments
    \n
    https://saltyapp.herokuapp.com/top100_sweetest_comments
    </xmp>"""


# "home" Route
@home_routes.route("/home")
def data_function():
    query = """
    SELECT *
    FROM salty_db_2
    """

    return fetch_query_comments(query)


# "top20_saltiest_users" Route
@home_routes.route("/top20_saltiest_users")
def data_function_1():
    query = """
    SELECT *
    FROM (
        SELECT
            AVG(salty_comment_score_neg) AS avg_saltiness_score,
            author_name,
            COUNT(DISTINCT comment_id) AS comment_count
        FROM
            salty_db_2
        WHERE
            salty_comment_score_neg > 0
        GROUP BY
            author_name
        ORDER BY
            avg_saltiness_score DESC) AS comment_query
    WHERE
        comment_count > 3
    LIMIT 20
    """

    columns = ['avg_saltiness_score', 'author_name', 'comment_count']

    return fetch_query(query, columns)


# "top20_saltiest_users" Route
@home_routes.route("/top20_sweetest_users")
def data_function_2():
    query = """
    SELECT *
    FROM (
        SELECT
            AVG(salty_comment_score_pos) AS avg_sweetness_score,
            author_name,
            COUNT(DISTINCT comment_id) AS comment_count
        FROM
            salty_db_2
        WHERE
            salty_comment_score_pos > 0
        GROUP BY
            author_name
        ORDER BY
            avg_sweetness_score DESC) AS comment_query
    WHERE
        comment_count > 3
    LIMIT 20
    """

    columns = ['avg_sweetness_score', 'author_name', 'comment_count']

    return fetch_query(query, columns)


# "top10_commenters" Route
@home_routes.route("/top10_commenters")
def data_function_3():
    query = """
    SELECT
        COUNT(DISTINCT comment_id) as comment_count,
        author_name
    FROM salty_db_2
    GROUP BY author_name
    ORDER BY comment_count DESC
    LIMIT 10
    """

    columns = ['comment_count', 'author_name']

    return fetch_query(query, columns)


# "top100_salty_comments" Route
@home_routes.route("/top100_salty_comments")
def data_function_4():
    query = """
    SELECT *
    FROM salty_db_2
    WHERE salty_comment_score_neg > 0
    ORDER BY salty_comment_score_neg DESC
    LIMIT 100
    """

    return fetch_query_comments(query)


# "top100_sweetest_comments" Route
@home_routes.route("/top100_sweetest_comments")
def data_function_5():
    query = """
    SELECT *
    FROM salty_db_2
    WHERE salty_comment_score_pos > 0
    ORDER BY salty_comment_score_pos DESC
    LIMIT 100
    """

    return fetch_query_comments(query)
