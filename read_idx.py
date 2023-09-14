import pickle
with open("thresh", "rb") as score_file:
    Highscores = []
    while True:
        try:
            Highscores.append(pickle.load(score_file))
        except EOFError:
            break
for item in Highscores:
 print item
