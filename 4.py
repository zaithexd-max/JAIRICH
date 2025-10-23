Name = input("Enter your name:");
#Result = len(Name);
Result = Name.find("i")#Determine where certain character is respectively(In Index)
print("find:  ",Result);
Result = Name.rfind("g")#Determine where certain character is (In Index)(The Last appearance of the certain word)
print("r find:  ",Result);
Result = Name.capitalize()#Return the string having first char Capitalized
print("Name Cap:  ",Result);
Result = Name.upper();#Return the string having every Char capitalized
print("Upper:  ",Result);
Result = Name.lower();#Return the string having every Char lower cased
print("Lower:  ",Result);
Result = Name.isdigit();#Check if it purely contains number if it is Return true else return false
print("isDigit?:  ",Result);
Result = Name.isalpha();#Check if it purely contains alphabet if it is Return true else return false
print("isalpha?:  ",Result);
Result = Name.count("i");
print(Result);
Result = Name.replace("i","o");
print(Result);
