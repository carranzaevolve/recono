# dependancy: mysql-connector-python (https://dev.mysql.com/downloads/connector/python/2.1.html)
import mysql.connector
import config

def conn():      
    try:

        connection = mysql.connector.connect( user=config.DB_USER, password=config.DB_PASSWORD, host = config.DB_HOST, database=config.DB_DATABASE)
        cur = connection.cursor()
        return cur, connection

    except mysql.connector.Error as err:
        print('Database connection failed for '+config.DB_USER+'@'+config.DB_HOST+'/'+config.DB_DATABASE)
        exit()

# def execute(sql):
#     return cursor.execute(sql)

    # if commit == True:
    #     connection.commit()
    # else:
    #     if single == True:
    #         return cursor.fetchone()
    #     else:
    #         return cursor.fetchall()
        
# def execute(tuple, single = False, args = {}, commit = False):
#     cursor.execute(tuple, args)

#     if commit == True:
#         connection.commit()
#     else:
#         if single == True:
#             return cursor.fetchone()
#         else:
#             return cursor.fetchall()

def lastrowid():
    return cursor.lastrowid

def close():
    connection.close()

# def get_bad_words():
#     sql = ("SELECT word FROM word_blacklist")
#     results = execute(sql)
#     return results

# def get_moderation_method():
#     sql = ("SELECT var_value FROM settings "
#     "WHERE var_key = %(key)s")
#     results = execute(sql, True, {'key':'moderation_method'})
#     return results[0]

# def current_events():
#     sql = ("SELECT count(id) FROM events WHERE event_date >= DATE_SUB(NOW(), INTERVAL 2 hour) AND event_date <= DATE_ADD(NOW(), INTERVAL 5 hour)")
#     results = execute(sql, True)
#     return results[0]

# def insert_social_post(channel, filter_type, post_id, validate, user_name, user_id, user_profile_picture, text, post_date, image_url, state):
#     try:
#         san_user_name = html_parser.unescape(user_name.encode('utf-8').strip()).decode("utf8").encode('ascii','ignore')
#     except:
#         san_user_name = html_parser.unescape(user_name.strip())
#     try:
#         san_text = html_parser.unescape(text.encode('utf-8').strip()).decode("utf8").encode('ascii','ignore')
#     except:
#         san_text = html_parser.unescape(text.strip())

#     insert_post = ("INSERT IGNORE INTO social_posts "
#         "(channel, filter_type, post_id, validate, user_name, user_id, user_profile_picture, text, post_date, image_url, state)"
#         "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
#     execute(insert_post, False, [channel, filter_type, str(post_id), validate,
#         san_user_name.strip(), user_id, user_profile_picture, san_text.strip(), post_date, image_url, state], True)

# def delete_posts(ids):
#     fmt = ','.join(['%s'] * len(ids))
#     cursor.execute("DELETE FROM `social_posts` WHERE id IN (%s)" % fmt,
#                     tuple(ids))
#     connection.commit()

# def update_campaigns(campaigns):
#     sql = ("UPDATE social_campaigns "
#         "SET last_updated = NOW()"
#         "WHERE id IN ("+(','.join(str(c) for c in campaigns))+")")
#     execute(sql, False, None, True)
