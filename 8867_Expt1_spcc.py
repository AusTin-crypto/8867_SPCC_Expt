i=0
table=[]
while i != 6:
    
    print()
    print("Enter Your Choice")
    i=int(input("1-create 2-Search 3-Enter Symbol 4-Remove 5-View 6-Exit "))
    
    if i==1:
        j=input("Enter the equation:")
        tmp_list=list(j)

        for i in tmp_list:
            if i.isalpha():
                j="Symbol:"+str(i)+" | Address: "+str(id(i))+" | Type: Identifier"
                table.append(j)
            elif i.isnumeric():
                j="Symbol:"+str(i)+" | Address: "+str(id(i))+" | Type: Numeric"
                table.append(j)
            else:
                j="Symbol:"+str(i)+" | Address: "+str(id(i))+" | Type: Operator"
                table.append(j)
    
    
    elif i==2:
        e=input("Search the Identifier/Operator:")
        flag=0

        for p in range(len(table)):
            if str(e)==(table[p][7]):
                flag=1
                break
            
        if flag==1:
            print("Element is present")
        else:
            print("Element not found!")  

    elif i==3:
        j=input("Enter the equation:")
        o=list(j)
        # print(x)
        for i in o:
            if i.isalpha():
                j="Symbol:"+str(i)+" | Address: "+str(id(i))+" | Type: Identifier"
                table.append(j)
            elif i.isnumeric():
                j="Symbol:"+str(i)+" | Address: "+str(id(i))+" | Type: Numeric"
                table.append(j)
            else:
                j="Symbol:"+str(i)+" | Address: "+str(id(i))+" | Type: Operator"
                table.append(j)
    elif i==4:
        e=input("Remove the Identifier/Operator:")
        l=0
        for p in range(len(table)-1,0,-1):
            if str(e)==(table[p][7]):
                l=p
                table.remove(table[p])
                # print("Element removed!")
    elif i==5:
        for i in table:
            print(i)