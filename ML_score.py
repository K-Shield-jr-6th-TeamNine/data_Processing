import pandas as pd
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

answer_Path = "C:/Users/Tarrow/Desktop/total_answer_.csv"   # answer(label file)
guess_Path = "C:/Users/Tarrow/Desktop/KNN.csv"              # guess (ML result file)
answer_csv = pd.read_csv(answer_Path, names=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80])
guess_csv = pd.read_csv(guess_Path, names=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80])

label = []
guess = []

for row in answer_csv.index:    # row length
    if answer_csv[80][row] == "benign":  # label normal
        label.append(0)
    else:                       # label anormal
        label.append(1)
del label[0]                    # delete first row ("Label")

for row in (guess_csv.index):   # row length
    if guess_csv[80][row] == 0 or guess_csv[80][row] == "0":  # guess normal
        guess.append(0)
    else:                       # guess anormal
        guess.append(1)
del guess[0]                    # delete first row ("Label")

print("accuracy_score = ",end='')
print(accuracy_score(label, guess))
print("recall_score = ",end='')
print(recall_score(label, guess))
print("precision_score = ",end='')
print(precision_score(label, guess))
print("f1_score = ",end='')
print(f1_score(label, guess))
# print accuracy_score / recall_score / precision_score / f1_score
