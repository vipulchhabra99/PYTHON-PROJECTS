import random
import time

Answers = ['It is certain',
           'It is decidedly so',
           'Keep Quiet',
           'Reply hazy, try again',
           'Ask again later',
           'Concentrate and ask again',
           'My reply is no',
           'Outlook not so good',
           'Very doubtful',
           'Naman Lalit',
           'Mrinaal Lalit',
           'Sorry Ask Again']
length=len(Answers)
def query():
    question=input("Please ask any query: ")
    print("Let Me See If I Can Help You ")
    time.sleep(1)
    print("Plz Wait")
    time.sleep(1)
    print(Answers[random.randint(0,length-1)])
    print("\n")

query()

question2=input("Would you like to ask any other question? Y or N: " )
while question2== str("Y"):
    query()
    question2=input("Would you like to ask any other question? Y or N: " )

else :
    print("So,It looks like you don't have any queries.")
    answer=input("Press any Key to exit the program.Thank you ")
               
