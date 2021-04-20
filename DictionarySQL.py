import mysql.connector


#Connection
con = mysql.connector.connect(
user = , 
password = ,
host = ,
database = 
)

cursor = con.cursor()
#word = getWord()

word = input("Enter word: ")
query = cursor.execute("SELECT * FROM Dictionary where Expression = '%s'" % word)
results = cursor.fetchall()

if results:
    for result in results:
        print(result[1])
else:
    print("No word found!")