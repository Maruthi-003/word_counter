#This program performs word counting operation
#This program expects a sentence as input and outputs number of words in the given input sentence 
#This program also outputs the number of ocuurances of a paticular word

#This part of code remove unneccessory leading and trailing spaces in the sentenced
def clean_input(sent):
    sentence=sent.strip()
    return sentence

#splitting the input into words and creating a list
def split_sentence(sent):
    lst=sent.split()
    return lst

#counting the total number of words the int gievn sentence
def total_count(word):
    total=len(word) 
    return total

#cleaning the words
def clean_words(word):
    cleaned_words=[]
    for w in word:
        each_letter=w[-1]
        #Checking whether the word contains any other characters than alphabets
        if( (ord(each_letter) >=65 and ord(each_letter) <=90) or (ord(each_letter) >=97 and ord(each_letter) <=122) ):
            letters=list(w)
            wor="".join(letters)
            cleaned_words.append(wor)
        else:
            #Remove other characters other than letters at the end
            lst=list(w)
            lst.pop(len(lst)-1)
            wor="".join(lst)
            cleaned_words.append(wor)
    return cleaned_words

#counting and printing the number of occurances of thw words
def count_occurances(words):
    print("The count of each word in the given input sentence :")
    check=[]
    for x in words:
        if x not in check:
            print(x,"-",words.count(x))
            check.append(x)
                

sen=input("Enter a sentence :")
cleaned_sentence=clean_input(sen)
words=split_sentence(cleaned_sentence)
print(f"Total number of words in the sentence is : {total_count(words)}")
cleaned_words=clean_words(words)
count_occurances(cleaned_words)