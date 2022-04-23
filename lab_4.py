

"""
This program allows a user three tries to guess the correct answer to the question
question ="what is the capital of California"
answer= Sacramento

we first set max_tries = 3, then we create a loop to iterate three times. for each iteration,
we ask the user for the answer (user input). then based on the answer the user gives, we check
to see if the user input matches the answer, if so , print "Correct". then terminate the loop with a 
break statement

if the user could not guess the correct answer within max_tries, we print 
"you have used up your allotment of guesses." then print "the correct answer is california".

"""

"""
main
    question= "what is the capital of California"
    answer= " Sacramento"
    ask(question, answer)


ask
    tries=0
    loop three times
        increment tries
        ask user input()
        check to see user of user input is equal to answer
            if so, print correct then exit loop
        if not correct
            print to the user, you have used your allotment of guesses,
            print the correct answer "the correct answer is sacramento"

    main

"""


def main():
    question = "what is the capital of California?"
    answer = " Sacramento"
    ask(question, answer)


def ask(question, answer, max_tries=3):
    tries = 0
    ans=""
    while tries < max_tries:
        tries = tries+1
        ans = input(question)
        if ans == answer:
         print("Correct: ")
         break
    if ans != anser:
        print("You have used up your allotment of guesses")


main()