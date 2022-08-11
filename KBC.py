question_list = ["1.How many continents are there?",
                "2.What is the capital of India?",
                "3.NG mei kaun se course padhaya jaata hai?"]
options_list = [["1.Four", "2.Nine", "3.Seven", "4.Eight"],
               ["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],
               ["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]]
lifeline_option=["1.Four","2.Seven",
               "1.Chandigarh","2.Delhi",
               "1.Software Engineering","2.Tourism"]
solution_list=[3,4,1]
solution_lifeline=[2,2,1]
a=0
count=1
amount=0
while a<len(question_list):
    print(question_list[a])
    j=0
    while j<len(options_list[a]):
        print(options_list[a][j])
        j=j+1
    if count<=1:
        lifeline=input("enter")
        if lifeline=="yes":
            b=0
            while b<len(lifeline_option[a]):
                print(lifeline_option[a][b])
                b=b+1
            c=int(input("please choose lifeline answer"))
            if c==solution_lifeline[a]:
                amount=amount+2000
                print("you are right=",amount)
            else:
                print("you are wrong=",amount)
                break
            count=count+1
        else:   
            g=int(input("choose your answer"))
            if g==solution_list[a]:
                amount=amount+2000
                print("you are right=",amount)
            else:
                print("you are wrong=",amount)
                break
    else:
        h=int(input("please choose your answer"))
        if h==solution_list[a]:
            amount=amount+2000
            print("you are right=",amount)
        else:
            print("you  are wrong=",amount)
            break
    a=a+1