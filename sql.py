import mysql.connector

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor()
print('''       1.search by word
          2.search by lenth of the word(all words within limit)''')

n = int(input("enter choice: "))

if(n == 1):
    word = input("ENTER a WORD: ")
    query = cursor.execute("SELECT * from Dictionary WHERE Expression = '%s' "% word)
    results = cursor.fetchall()
elif(n == 2):
    lenmin = int(input("ENter lenth of word(min): "))
    lenmax = int(input("Enter lenth of word(max): "))
    query = cursor.execute("SELECT * from Dictionary WHERE length(Expression) > %d-1 AND length(Expression) < %d+1 "%(lenmin,lenmax))
    results = cursor.fetchall()
else:
    print("INvalid choice")

if results:
    for r in results:
        print(r)
else:
    print("No word found!")