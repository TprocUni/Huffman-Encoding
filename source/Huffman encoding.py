#Huffman Encoding

#imports
from heapq import heappush, heappop, heapify
from bitmap import BitMap
from bitarray import bitarray
import re
import json

#functions

#calculates the frequency of each character in the sample text
def calcFrequencies(sampleText):
    for c in sampleText:
        if c in frequency:
            frequency[c] += 1   #increases value in dict by 1
        else:
            frequency[c] = 1    #creates new value in dict


#gets the sample text from a txt file
def getSampleText(fileLocation):
    f = open(fileLocation, "r")
    sampleText = str(f.read())
    f.close()
    return sampleText

#transforms the dictionary of values into a 2d array, then a heap
def transformToList(freqDict):
    heap = [[freq, [symbol, ""]] for symbol, freq in frequency.items()] #the null space is for the huffman code string
    heapify(heap)                                                       #transform the list into a heap tree structure
    while len(heap) > 1:
        right = heappop(heap)                                           #Pops and returns the smallest item
        for couple in right[1:]:                                        #loops through each right node
            couple[1] = '0' + couple[1]                                 #add zero to all the right node
        left = heappop(heap)                                            #same with left
        for couple in left[1:]:  
            couple[1] = '1' + couple[1]                                 #add one to all the left node
        heappush(heap, [right[0] + left[0]] + right[1:] + left[1:])     #add values onto the heap
    #creats the final heap/tree
    huffmanList = right[1:] + left[1:]
    return huffmanList


def transformToTree(huffmanList):
    huffmanDict = {i[0]:bitarray(str(i[1])) for i in huffmanList}    #adding the elements to the huffmanList
    return huffmanDict

def saveEncodedString(encodedString):
    invalidChars = re.compile(r"[<>/{}[\]~`]")
    fileName = str(input("Please enter your desired file name, X for default save into 'compressed_file.bin' or press enter to cancel: "))
    if fileName == "":
        return "File has not been saved"
    elif invalidChars.search(fileName):
        return "File name cannot contain the following: <>/\{}[]~`"
    elif fileName == "X":
        f = open("compressed_file.bin", "wb")
        encodedString.tofile(f)
        f.close()
        return "File saved to default location (compressed_file.bin)"
    else:
        fileName+=".bin"
        f = open(fileName, "wb")
        encodedString.tofile(f)
        f.close()
        return (f"File saved to user specified location ({fileName})")

def selectEncodingTree(originalHuffmanList):
    print('''
Please select an encoding tree to use:
1 - English based
2 - Finnish based
3 - French based
4 - custom (based from file to be encoded)
5 - back to main menu''')
    valid = False
    while valid == False:
        try:
            choice = int(input())
            if choice not in [1,2,3,4,5]:
                print ("Please only enter integer values between 1 and 5.")
            else:
                valid = True
        except ValueError:
            print("Please only enter integer values between 1 and 5.")
    if choice == 1:
        f = open("huffman_tree_english.json","r")
        huffmanList = json.load(f)
        f.close()
        print("set to English encoding tree.")
        return huffmanList
    elif choice == 2:
        f = open("huffman_tree_finnish.json","r")
        huffmanList = json.load(f)
        f.close()
        print("set to Finnish encoding tree.")
        return huffmanList
    elif choice == 3:
        f = open("huffman_tree_french.json","r")
        huffmanList = json.load(f)
        f.close()
        print("set to French encoding tree.")
        return huffmanList
    elif choice == 4:
        huffmanList = customEncoding()
        if huffmanList == 0:
            print("Invalid Huffman tree, using previous tree")
            return originalHuffmanList
        else:
            print("set to custom encoding tree.")
            return huffmanList
    elif choice == 5:
        return originalHuffmanList

def customEncoding():
    print("Would you like to to create a Huffman tree from a .txt file or by inputting a string:\n1 - txt file\n2 - string\n3 - quit")
    valid = False
    while valid == False:
        try:
            choice = int(input())
            if choice not in [1,2,3]:
                print("please input either 1, 2 or 3")
            else:
                valid = True
        except ValueError:
            print("please input either 1, 2 or 3")
    if choice == 1:
        fileName = str(input("please input the file name without the suffix '.txt', also ensure that it is in the same folder as the program. If you wish to use/edit the text stored in the \nsample text file it will be used as default and you may press enter: "))
        if fileName == "":
            f = open("sample.txt", "r")
            text = f.read()
            f.close()
        else:
            try:
                f = open(fileName+".txt", "r")
                text = f.read()
                f.close()
            except FileNotFoundError:
                print("Invalid file name, check the file exists or you spelt it correctly.")
    elif choice == 2:
        text = str(input("Please enter a string to use for the creation of a Huffman tree: "))
    elif choice == 3:
        return 0
    calcFrequencies(text)
    huffmanList = transformToList(frequency)
    f = open("huffman_tree_custom.json", "w")
    json.dump(huffmanList, f)
    f.close()
    return huffmanList

def encodeFile(huffmanList):
    huffmanDict = transformToTree(huffmanList)
    encodedString = bitarray()
    print('''
Would you like to encode a txt file or input a string?
1 - txt file
2 - string
3 - quit''')
    valid = False
    while valid == False:
        try:
            choice = int(input())
            if choice not in [1,2,3]:
                print("please input either 1, 2 or 3")
            else:
                valid = True
        except ValueError:
            print("please input either 1, 2 or 3")
    if choice == 1:
        fileName = str(input("please input the file name without the suffix '.txt', also ensure that it is in the same folder as the program. If you wish to use/edit the text stored in the \nsample text file it will be used as default and you may press enter: "))
        if fileName == "":
            f = open("sample.txt", "r")
            text = f.read()
            f.close()
        else:
            try:
                f = open(fileName+".txt", "r")
                text = f.read()
                f.close()
            except FileNotFoundError:
                print("Invalid file name, check the file exists or you spelt it correctly.")
    elif choice == 2:
        text = str(input("please enter string to be encoded: "))
    elif choice == 3:
        return 0
    encodedString.encode(huffmanDict, text)
    return encodedString

def decode(huffmanList):
    decodedText = bitarray()
    choice = str(input("please input the file name without the suffix '.bin' that you wish to decode, also ensure that it is in the same folder as the program.\nIf you wish to use the default file press enter: "))
    if choice == "":
        fileName = "compressed_file.bin"
    else:
        fileName = choice+".bin"
    try:
        f = open(fileName, "rb")
        decodedText.fromfile(f)
        f.close()
        decodedText = decodedText[:-byteAvoidance] #removes extra bits
        decodedText = "".join(decodedText.decode(transformToTree(huffmanList)))
        return decodedText
    except FileNotFoundError:
        print("Invalid file name, check the file exists or you spelt it correctly.")
        return None

#main
def main():
    #setting up global dicts and local variables
    global frequency
    frequency = {}
    string = ""
    global byteAvoidance
    #used when we convert back to string so that the extra digits added are removed (due to it being stored in bytes)
    f = open("huffman_tree_english.json","r")
    huffmanList = json.load(f)
    f.close()
    running = True
    while running == True:
        print('''
Welcome to the Huffman encoding compression software created by Ted Proctor
please select an option:
1 - encode a file
2 - change Huffman encoding tree
3 - decode a file
4 - quit''')
        valid = False
        while valid == False:
            try:
                choice = int(input())
                if choice not in [1,2,3,4]:
                    print ("Please only enter integer values between 1 and 4.")
                else:
                    valid = True
            except ValueError:
                print("Please only enter integer values between 1 and 4.")
        if choice == 1:
            encodedString = encodeFile(huffmanList)
            printString = str(input("would you like to print the encoded string to the screen? type 'y' if yes any other character if no: "))
            if printString.lower() == "y": 
                print("The encoded string is: " + str(encodedString)[10:-2])
            byteAvoidance = (8-(len(encodedString)%8))
            print(saveEncodedString(encodedString))
        elif choice == 2:
            huffmanList = selectEncodingTree(huffmanList)
        elif choice == 3:
            decodedString = decode(huffmanList)
            if decodedString == None:
                pass
            else:
                print("The decoded string is: " + decodedString)
        elif choice == 4:
            running = False

main()




