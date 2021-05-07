import pandas as pd

file_Path = "C:/Users/Tarrow/Desktop/VScode/codes/lresult.csv"
# file path that CSV file from changing the pcap file with cicflowmeter

pcap_data = pd.read_csv(file_Path, names=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83])
# column naming

learning_data = pcap_data[[4,5,6,7,12,13,14,15,16,17,18,19,20,21,22,23,8,9,33,36,34,35,37,40,41,38,39,42,45,46,43,44,47,48,49,50,29,30,10,11,25,24,26,27,28,51,52,53,54,55,56,78,57,58,59,76,77,70,71,74,72,73,75,79,81,80,82,60,61,32,31,64,65,62,63,68,69,66,67,83]]
# swap and drop column

learning_data.to_csv("./learn_data.csv", header = False, index = False)
# save file
