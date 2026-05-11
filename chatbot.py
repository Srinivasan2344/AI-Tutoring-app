from transformers import pipeline

chatbot = pipeline("text-generation", model="gpt2")


def ask_tutor(question):
    response = chatbot(question, max_length=50)
    return response[0]['generated_text']


question = "Explain Newton's first law"
print(ask_tutor(question))
while True:

    question = input("Ask Your Question: ").lower()

    if question == "hi":
        print("Hello Student!")

    elif "python" in question:
        print("Python is a programming language.")

    elif "ai" in question:
        print("AI means Artificial Intelligence.")

    elif "machine learning" in question:
        print("Machine Learning helps computers learn from data.")

    elif question == "bye":
        print("Goodbye!")
        break

    else:
        print("Sorry, I don't know that answer.")