import re
def read_template(path):
    with open(path) as f:
        contents = f.read()
        return contents

def parse_template(text):
    x=re.sub("{.*?}","{}",text)
    y=re.findall(r"(?<=\{).+?(?=\})", text)
    return (str(x),tuple(y))


def merge(string,word):
    statment=string.format(*word)
    
    with open('assets/result.txt','w') as f:
     f.write(statment)
    return statment

print("wlcome to midlib game")

answer=[]
def start_game():
    file=read_template("assets/user.txt")
    text,value=parse_template(file)
    for item in value:
        input_user=input(f"enter {item}")
        answer.append(input_user)
    return merge(text,answer)
if __name__== "__main__":
 start_game()