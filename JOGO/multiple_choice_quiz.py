from question import Question

question_prompts = [
    "What color are apples? \n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas? \n(a) Green\n(b) Yellow\n(c) Teal\n\n",
    "What color are Strawberries? \n(a) Magenta\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "b"),
]



def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print("voce tem " + str(score) + "/" + str(len(questions)) + " corretos")
run_test(questions)