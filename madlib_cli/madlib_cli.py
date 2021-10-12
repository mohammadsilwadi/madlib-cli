import re
def read_template(path):
    with open(path) as f:
        contents = f.read()
        return contents

def parse_template(text):
    x=re.sub("{.*?}","{}",text)
    y=re.findall(r"(?<=\{).+?(?=\})", text)
    z=tuple(y)
    return (x,z)


def merge(string,word):
    statment=string.format(*word)
    
    with open('assets/result.txt','w') as f:
     f.write(statment)
    return statment


answer=[]
def game_function():
    print("wlcome to midlib game")
    file=read_template("assets/Madlib_text.txt")
    text,value=parse_template(file)
    for i in value:
        input_user=input(f" enter {i} >>>>")
        answer.append(input_user)
    return merge(text,answer)
if __name__== "__main__":
 game_function()