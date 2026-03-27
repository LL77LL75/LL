import os
filepath = os.getcwd()
sherlock_path = os.path.join(filepath, 'sherlock.txt')
if os.path.exists(sherlock_path):
    print("File exists")
    with open("sherlock.txt","r") as file:
        content = file.read()
        print(content)
        print(f"total chatacters: {len(content)}")
        dict = {"a":0,
                "e":0,
                "i":0,
                "o":0,
                "u":0}
        for i in content:
            if i.lower() == "a":
                dict["a"] = dict["a"]+1
            if i.lower() == "e":
                dict["e"] = dict["e"]+1
            if i.lower() == "i" :
                dict["i"] = dict["i"]+1
            if i.lower() == "o":
                dict["o"] = dict["o"]+1
            if i.lower() == "u":
                dict["u"] = dict["u"]+1
        counter = dict["a"]+dict["e"]+dict["i"]+dict["o"]+dict["u"]
        print(f"there are {counter} vowels")
        percent = counter/len(content)*100
        print(f"{round(percent,2)}% of the text is vowels")
else:
    print("error:File does not exist")
with open("vowelcounts.txt","w") as file:
    file.write(f"total characters {len(content)} \n")
    file.write(f"total vowels {counter} \n")
    file.write(f"There are {str(dict["a"])} a \n")
    file.write(f"There are {str(dict["e"])} e \n")
    file.write(f"There are {str(dict["i"])} i \n")
    file.write(f"There are {str(dict["o"])} o \n")
    file.write(f"There are {str(dict["u"])} u ")