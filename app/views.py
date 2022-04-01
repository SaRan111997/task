from urllib import request
from django.shortcuts import render

final_out=''

final_out1=[]
length=[]

def home(request):
    
    

    return render(request,'home.html')

def submit(request):
    
    input1=request.POST.get('input1')
    input2=request.POST.get('input2')
    print(input1)
    print(input2)
    #str1 = 'HC:Unsafe condition: Access not provided in the excavation for ingress/egress'
    str1 = str(input1)
    str2 = str(input2)
    #split string
    splits = str1.split()
    #file1 = open('input2.txt', 'r')
    file1 = open(str2, 'r')
    Lines = file1.readlines()
    count = 0
    #l=[5,6,8,7,8]
    def checking(text):
        
        input1=str1.split()
        input2=text.split()
        length.append(len(list(set(input1) & set(input2))))
        if len(list(set(input1) & set(input2)))==8:
            print(input2)  
            final_out1.clear()
            final_out1.append(input2)     
    for line in Lines:
        count += 1
        checking(line)
    print(length)
    
    return render(request,'submit.html',{'data':final_out1})