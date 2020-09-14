import psycopg2

# Table creation
commands = (  # Table 1
    '''CREATE TABLE IF NOT EXISTS TwitterUser(User_Id BIGINT PRIMARY KEY, User_Name TEXT);''',
    # Table 2
    '''CREATE TABLE IF NOT EXISTS TwitterTweet(Tweet_Id BIGINT PRIMARY KEY,
                                                User_Id BIGINT,
                                                Tweet TEXT,
                                                Retweet_Count INT,
                                                CONSTRAINT fk_user
                                                FOREIGN KEY(User_Id)
                                                REFERENCES TwitterUser(User_Id));''',
    # Table 3
    '''CREATE TABLE IF NOT EXISTS TwitterEntity(Id SERIAL PRIMARY KEY,
                                            Tweet_Id BIGINT,
                                            Hashtag TEXT,
                                            CONSTRAINT fk_user
                                            FOREIGN KEY(Tweet_Id)
                                            REFERENCES TwitterTweet(Tweet_Id));'''
)


# Connection to database server
try:
    connection = psycopg2.connect(host="localhost",
                                  database="TwitterDB",
                                  port=5432, user='root',
                                  password='')

    # Create cursor to execute SQL commands
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")
    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

    # Execute SQL commands
    for command in commands:
        # Create tables
        cursor.execute(command)
    print("Table was created successfully ")


except (Exception, psycopg2.Error) as e:
    print("Error while connecting to PostgreSQL", e)

finally:
    # Close communication with server
    if connection:
        cursor.connection.commit()
        cursor.close()
        connection.close()
        print('PostgreSQL connection is closed')
