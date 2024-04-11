from turtle import Turtle


secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while secret_word != guess and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Adivinhe a palavra secreta: ")
        guess_count += 1
    else:
        out_of_guesses = True

    if secret_word != guess:
        if out_of_guesses:
            print("Acabou suas chances")
        else:
            print("Resposta errada")
    else:
        print("Parabens")
