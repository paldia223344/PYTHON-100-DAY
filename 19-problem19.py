def Remove(list,word):
    n=[]
    for i in list:
        if not(i == word):
            n.append(i.strip(word))
    return n   
   
list = [1,"Harry","dia pal","krishna"]
word = input("Enter a word to be removed")
print(Remove(list,word))