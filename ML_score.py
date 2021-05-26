import pandas as pd
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

answer_Path = "C:/Users/Tarrow/Desktop/total_answer_.csv"   # answer(label file)
guess_Path = "C:/Users/Tarrow/Desktop/KNN.csv"              # guess (ML result file)
answer_csv = pd.read_csv(answer_Path, names=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80])
guess_csv = pd.read_csv(guess_Path, names=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81])

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

true_positives = 0
true_negatives = 0
false_positives = 0
false_negatives = 0
for i in range(len(guess)):
  #True Positives
  if label[i] == 1 and guess[i] == 1:
    true_positives += 1
  #True Negatives
  if label[i] == 0 and guess[i] == 0:
    true_negatives += 1
  #False Positives
  if label[i] == 0 and guess[i] == 1:
    false_positives += 1
  #False Negatives
  if label[i] == 1 and guess[i] == 0:
    false_negatives += 1

scorefile = open("./KNN_ML_score.txt", 'w')
scorefile.write("==KNN.csv score==\n")
scorefile.write("accuracy_score = \t")
scorefile.write(str(accuracy_score(label, guess)))
scorefile.write("\nrecall_score = \t\t")
scorefile.write(str(recall_score(label, guess)))
scorefile.write("\nprecision_score = \t")
scorefile.write(str(precision_score(label, guess)))
scorefile.write("\nf1_score = \t\t")
scorefile.write(str(f1_score(label, guess)))
scorefile.write("\n\n\ttrue_positives =  ")
scorefile.write(str(true_positives))
scorefile.write("\n\ttrue_negatives =  ")
scorefile.write(str(true_negatives))
scorefile.write("\n\tfalse_positives = ")
scorefile.write(str(false_positives))
scorefile.write("\n\tfalse_negatives = ")
scorefile.write(str(false_negatives))
# print accuracy_score / recall_score / precision_score / f1_score
# filename is ./KNN_ML_score.txt

''' >> For RF_answer.csv <<
import pandas as pd
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

answer_Path = "C:/Users/Tarrow/Desktop/total_answer_.csv"   # answer(label file)
guess_Path = "C:/Users/Tarrow/Desktop/RF_answer.csv"        # guess (ML result file)
answer_csv = pd.read_csv(answer_Path, names=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80])
guess_csv = pd.read_csv(guess_Path, names=[1,2])

label = []
guess = []

for row in answer_csv.index:    # row length
    if answer_csv[80][row] == "benign":  # label normal
        label.append(0)
    else:                       # label anormal
        label.append(1)
del label[0]                    # delete first row ("Label")

for row in (guess_csv.index):   # row length
    if guess_csv[2][row] == "BENIGN":  # guess normal
        guess.append(0)
    else:                       # guess anormal
        guess.append(1)
del guess[0]                    # delete first row ("Label")

true_positives = 0
true_negatives = 0
false_positives = 0
false_negatives = 0
for i in range(len(guess)):
  #True Positives
  if label[i] == 1 and guess[i] == 1:
    true_positives += 1
  #True Negatives
  if label[i] == 0 and guess[i] == 0:
    true_negatives += 1
  #False Positives
  if label[i] == 0 and guess[i] == 1:
    false_positives += 1
  #False Negatives
  if label[i] == 1 and guess[i] == 0:
    false_negatives += 1

scorefile = open("./RF_answer_ML_score.txt", 'w')
scorefile.write("==RF_answer.csv score==\n")
scorefile.write("accuracy_score = \t")
scorefile.write(str(accuracy_score(label, guess)))
scorefile.write("\nrecall_score = \t\t")
scorefile.write(str(recall_score(label, guess)))
scorefile.write("\nprecision_score = \t")
scorefile.write(str(precision_score(label, guess)))
scorefile.write("\nf1_score = \t\t")
scorefile.write(str(f1_score(label, guess)))
scorefile.write("\n\n\ttrue_positives =  ")
scorefile.write(str(true_positives))
scorefile.write("\n\ttrue_negatives =  ")
scorefile.write(str(true_negatives))
scorefile.write("\n\tfalse_positives = ")
scorefile.write(str(false_positives))
scorefile.write("\n\tfalse_negatives = ")
scorefile.write(str(false_negatives))
# print accuracy_score / recall_score / precision_score / f1_score
# filename is ./KNN_ML_score.txt
'''




