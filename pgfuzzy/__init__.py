from django.db import connection

def soundex(text):
    cursor = connection.cursor()
    cursor.execute("SELECT soundex(%s)", [text])
    row = cursor.fetchone()
    return row[0]

def difference(text, text1):
    cursor = connection.cursor()
    cursor.execute("SELECT difference(%s, %s)", [text, text1])
    row = cursor.fetchone()
    return row[0]

def levenshtein(source, target):
    cursor = connection.cursor()
    cursor.execute("SELECT levenshtein(%s, %s)", [source, target])
    row = cursor.fetchone()
    return row[0]

def metaphone(text, max_output_length):
    cursor = connection.cursor()
    cursor.execute("SELECT metaphone(%s, %s)", [text, max_output_length])
    row = cursor.fetchone()
    return row[0]

def dmetaphone(text):
    cursor = connection.cursor()
    cursor.execute("SELECT dmetaphone(%s)", [text])
    row = cursor.fetchone()
    return row[0]
