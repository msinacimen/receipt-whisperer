import os

wordsList = []
wordsIndextList = []


label_list = ["<start_\"company_name\">",
              "<end_\"company_name\">",
                  "<start_\"date\">",
                  "<end_\"date\">",
                  "<start_\"time\">",
                  "<end_\"time\">",
                  "<start_\"receipt_number\">",
                  "<end_\"receipt_number\">",
                  "<start_\"tax\">",
                  "<end_\"tax\">",
                  "<start_\"amount\">",
                  "<end_\"amount\">"]

label_list2= ["Pad","Others","B_Comp","l_Comp","B_Date","l_Date","B_Time","l_Time",
                  "B_Receipt","l_Receipt","B_Tax","l_Tax","B_Amount","l_Amount"]

 

def one_hot_encode_index_list():
    oneHotEncodedList = []
    unique_labels_len = len(sorted(set(label_list2)))
    for i in wordsIndextList:
        bitlist = list(0 for i in range(unique_labels_len))
        bitlist[i] = 1
        oneHotEncodedList.append(bitlist)
    return oneHotEncodedList


def splitfunction(text:str):
    words = text.split()
    for word in words:
        wordsList.append(word)
        wordsIndextList.append(1)



def indexAssignment(tag,last):
    if(tag==None):
        return None
    index = label_list.index(tag)+2
    if(last == "l"):
       index +=1
    return index


def checkTag(word:str):
    for tag in label_list:
        index = word.find(tag)
        if index != -1:
            return tag    
    return None



def tagingWords():
    control = None
    counter = 0
    for word in wordsList:
        tag = checkTag(word)
        if tag != None:
            if(word.find("<start_") != -1):
                control = tag
            if(word.find("<start_") != -1 and word.find("<end_") == -1):
                wordsIndextList[counter] = indexAssignment(tag,"B")
                counter+=1
            elif(word.find("<start_") != -1 and word.find("<end_") != -1):
                wordsIndextList[counter] = indexAssignment(tag,"B")
                counter+=1
            else:
                wordsIndextList[counter] = indexAssignment(tag,"B")
                counter+=1
            if(word.find("<end_") != -1):
                control = None
        elif control !=None:
            wordsIndextList[counter] = indexAssignment(control,"l")
            counter+=1
        else:
            counter+=1  


def oneHotEncodedFunction(texts):
    wordsList.clear
    wordsIndextList.clear
    splitfunction(texts)
    tagingWords()
    return one_hot_encode_index_list()




folder_path = "C:\\Users\\mirac\\OneDrive\\Masaüstü\\BitirmeProjesi\\dataset\\training-data"  # localdeki train dosya adresi
file_list = os.listdir(folder_path)
y_train = []

for file_name in file_list:
    if file_name.endswith(".txt"):
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
            oneHotEncodedList = oneHotEncodedFunction(text)
            y_train.append(oneHotEncodedList)
            