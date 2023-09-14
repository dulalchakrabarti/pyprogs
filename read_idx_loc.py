import pickle
with open("thresh_loc", "rb") as score_file:
    Highscores1 = []
    while True:
        try:
            Highscores1.append(pickle.load(score_file))
        except EOFError:
            break
with open("thresh", "rb") as score_file:
    Highscores2 = []
    while True:
        try:
            Highscores2.append(pickle.load(score_file))
        except EOFError:
            break
for a, b in zip(Highscores1, Highscores2):
 print a
 print b
