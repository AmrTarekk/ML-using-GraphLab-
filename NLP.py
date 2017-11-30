from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import aiml
import random, re 





def NLP(message) :

    #input
    #message = raw_input("Enter your message >> ")

    # work Tokenizing
    #print(word_tokenize(message))
    message = word_tokenize(message)

    # defining stop words
    #Minimizing probability
    stop_words = set(stopwords.words("english"))

    filtered_sentence = []

    #filtering Method
    for w in message:
        if w not in stop_words:
            filtered_sentence.append(w)

    message = filtered_sentence
    #print(message)

    #lemmatizing to adjective
    lemmatizer = WordNetLemmatizer()
    Lemmatized_sentence = []
    for w in message:
        Lemmatized_sentence.append(lemmatizer.lemmatize(w, pos="a"))
    #print(Lemmatized_sentence)
    message = Lemmatized_sentence


        #Our References
    Reference_sentence = [ 'hello','good' , 'doctor' , 'student' ]
    Z = True

    Reference_found = []
    Meaning_sentence = []
    #Meaning vs References
    if Z == True  :
        for w in message :
            for syn in wordnet.synsets(w):
                for l in syn.lemmas():
                    Meaning_sentence.append(l.name())

        message1 = set(Meaning_sentence)
#    print (message1)
        for w in message1:
            if w in Reference_sentence:
                Reference_found.append(w)
    #for w in Reference_found :
        #print (w) 
    
    for w in Reference_found :
        if w == "hello" :
            #entering aiml sentence   
            response = mybot.respond("hello")
            print (response)
            return True 
        else :
            print("Can YOu try again ? ")
            return False



mybot=aiml.Kernel()
mybot.learn('test_chat.aiml')


while True:
    message = raw_input("Enter your message >> ")
    if message == "quit":
        exit()
    else:
        response = mybot.respond(message)
        print (response)
        test = False 
        if response == "" :
            test = NLP(message)

