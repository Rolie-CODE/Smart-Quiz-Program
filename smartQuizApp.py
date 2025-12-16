from openai import OpenAI

client = OpenAI(api_key="your api should be here")

def chatWithGPT(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content



print("Welcome to your Smart Quiz Program")
print("----------------------------------")
print("Select Mode:")
print("==============")
print("1. Quiz Mode") 
print("2. Set Questions From Slides")
print("3. Exit Program")
choice =input("Enter mode (1/2/3): ")

if choice == "1":
    print("You have selected Quiz Mode")
    print("Select level of difficulty: easy, medium, hard")
    no = 0
    while True:

        no += 1

        difficulty = input("Enter difficulty: ").lower()
        print(f"You have selected {difficulty} level")
        if difficulty == "easy":
            prompt = (
                "Ask me ONE easy multiple-choice computer science question. "
                "Label options A, B, C, D. "
                "Silently remember the correct answer."
            )

        elif difficulty == "medium":
            prompt = (
                "Ask me ONE medium multiple-choice computer science question. "
                "Label options A, B, C, D. "
                "Silently remember the correct answer."
            )

        elif difficulty == "hard":
            prompt = (
                "Ask me ONE hard multiple-choice computer science question. "
                "Label options A, B, C, D. "
                "Silently remember the correct answer."
            )


        question = chatWithGPT(prompt)
        print("Here is your question:")
        print(question)

        user_answer = input("Answer: ").capitalize()

        response = chatWithGPT(
            f"This was the question:\n{question}\n\n"
            f"My answer is {user_answer}. "
            "Check if it is correct or incorrect and explain briefly."
        )

        print(response)
        continue_quiz = input("Do you want to try another question? (yes/no): ").lower()
        if continue_quiz != "yes":
            print("Thank you for playing the quiz!")
            print(f"You answered {no} question(s).")
            break

elif choice == "2":
    
    print("You have selected Set Questions From Slides")
    while True:

        slides = input("Paste your slide content here: ")

        prompt = (
            f"Go through the text in {slides} and create a multiple choice question from the content"
            "Label options A, B, C, D and silently remember the correct answer."
            "Do not repeat any questions and also dont tell me the answer yet"
        )

        question = chatWithGPT(prompt)
        print("Here is your question:")
        print(question)

        user_answer = input("Answer: ").capitalize()

        response = chatWithGPT(
            f"This was the question:\n{question}\n\n"
            f"My answer is {user_answer}. "
            "Check if it is correct or incorrect and explain briefly."
        )

        print(response)
        continue


elif choice == "3":
    print("Exiting the program. Goodbye!")





# while True:
#     userInput = input("You: ")
#     if userInput.lower() == "exit":
#         break
#     reply = chatWithGPT(userInput)
#     print("Bot:", reply)