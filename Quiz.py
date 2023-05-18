
# Multiple Choice Quiz program

# First from module Question.py import class Question
from Question import Question

# Question prompts array containing all the question promts
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
]

# An array of questions that would be asked on the test
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

# Function that will run the test. 
# It has to ask user the questions and check to see if they got the answer right

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer:
            score += 1
    print(f"You got {str(score)}/{str(len(questions))} correct")
run_test(questions)
