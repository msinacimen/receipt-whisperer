resultList = []
indexResultList = []


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
    for i in indexResultList:
        bitlist = list(0 for i in range(unique_labels_len))
        bitlist[i] = 1
        oneHotEncodedList.append(bitlist)
    return oneHotEncodedList


def splitfunction(text:str):
    words = text.split()
    for word in words:
        resultList.append(word)
        indexResultList.append(1)



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
    for word in resultList:
        tag = checkTag(word)
        if tag != None:
            if(word.find("<start_") != -1):
                control = tag
            if(word.find("<start_") != -1 and word.find("<end_") == -1):
                indexResultList[counter] = indexAssignment(tag,"B")
                counter+=1
            elif(word.find("<start_") != -1 and word.find("<end_") != -1):
                indexResultList[counter] = indexAssignment(tag,"B")
                counter+=1
            else:
                indexResultList[counter] = indexAssignment(tag,"B")
                counter+=1
            if(word.find("<end_") != -1):
                control = None
        elif control !=None:
            indexResultList[counter] = indexAssignment(control,"l")
            counter+=1
        else:
            counter+=1  


def oneHotEncodedFunction(texts):
    resultList.clear
    indexResultList.clear
    splitfunction(texts)
    tagingWords()
    return one_hot_encode_index_list()



texts="""<start_"date">08 09 2021<end_"date">

<start_"company_name">İREN mahmut ECZANESİ<end_"company_name">

ECZ. İREM GÜNDOĞDU

<start_"amount">*50 , 00<end_"amount">

CUMHURİYET MH. MİTHAT PAŞA CD.

NO:41 EFELER / AYDIN

TEL: 0 256 214 34 76

V.D:EFELER 28462485852

: <start_"date">08/09/2021<end_"date">

: <start_"time">11:05:35<end_"time">

: <start_"receipt_number">0003<end_"receipt_number">

TARİH

SAAT

FİŞ NO

İLAÇ.1

08

*50,00

<start_"tax">*3,70<end_"tax">

<start_"amount">*50,00<end_"amount">

TOPKDV

TOPLAM

KREDİ

<start_"amount">*50,00<end_"amount">

TEB

************0615

MERSIS : 2846248585200001

EKÜ NO:0002

Z NO:1392

IŞVERI NO:000000000857006

TERMINAL NO:579215

41GIN NO:0207

<start_"date">08 09 2021<end_"date">

4.0049.26

MASTERCARD

SIRA NO:000002

<start_"time">11:05:48<end_"time">

AID A0000000041010

SATIS

T 0****** **** ****

<start_"amount">50, 00<end_"amount"> TL

TUTAR

ONAY KODU: 882914

REFERANS NO: 125111510070

KART TÜRÜ: MC YI KK

TEMASSIZ İŞLEM

TUTAR KARSILIGI MAL HIZMET ALDIM

KART SAHIBİNE AİTTIR

.TURK EKONOMI BANKASI A.$. ---

TICARET SICIL NO : 189356

MERSIS NO: 0876004342000105

TEB KAMPUS C-D BLOK SARAY MH SOKULLU CD

NO : 7A-7B UMRANIVE 34768 ISTANBUL

www.teb.com.tr

TEB

MASTERCARD PAYPASS

EKÜ NO:0002

Z NO:1392

NF JI 20041334

"""



oneHotEncodedList = oneHotEncodedFunction(texts)


for i in range(len(oneHotEncodedList)):
    print(f"{oneHotEncodedList[i]} ----- {resultList[i]}  ---->  {indexResultList[i]}")