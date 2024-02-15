def nfa(i,state):
    ns=state+1
    return f"{state}-->{i}-->{ns}"
def occurance(state):
    ns=state+1
    return f"{ns}-->e-->{state}"
def check(re):
    regex=re.split()
    state=0
    if "(" in re:
        regex = re.replace("(", " ( ").replace(")", " ) ").split()
        regex.remove("(")
        regex.remove(")")
    for i in regex:
        if "*" not in i and "|" not in i:
            print(nfa(i,state))
            state+=1
        elif "*" in i:
            startingnode=state
            char=i[:-1]
            ns=state+1
            print(f"{state}-->e-->{ns}")
            state+=1
            print(nfa(char,state))
            print(occurance(state))
            state+=1
            ns=state+1
            print(f"{state}-->e-->{ns}")
            print(f"{startingnode}-->e-->{ns}")
            state+=1
        elif "|" in i:
            char=i.replace("|"," ")
            var=char.split()
            startingnode=state
            for j in var:
                ns=state+1
                print(f"{startingnode}-->e-->{ns}")
                state+=1
                print(nfa(j,state))
                state+=1
            ns=state+1
            print(f"{state}-->e-->{ns}")
            state-=2
            print(f"{state}-->e-->{ns}")
re=input("enter the regular expression:")
check(re)