quiz_data = {
    "python": [
        {
            "question": "What keyword is used to create a function in Python?",
            "answer": "def"
        },
        {
            "question": "Which data type stores True or False?",
            "answer": "bool"
        }
    ]
}

subject = input("Enter subject: ").lower()

if subject in quiz_data:

    print("\nQuiz Questions:\n")

    score = 0

    for q in quiz_data[subject]:

        print(q["question"])

        user_answer = input("Your Answer: ")

        if user_answer.lower() == q["answer"].lower():

            print("Correct!\n")
            score += 1

        else:

            print("Wrong!")
            print("Correct Answer:", q["answer"])

    print("\nFinal Score:", score)

else:
    print("Subject not found")