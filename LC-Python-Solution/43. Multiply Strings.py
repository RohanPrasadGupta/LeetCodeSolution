def multiply(num1,num2):
    #print(num1,num2,type(num1),type(num2),ord(num1)-48,ord(num2)-48)
    
    
    iN1 = 0
    res = [0]*(len(num1)+len(num2))
    
    for i in range(len(num1)-1,-1,-1):
        carry = 0
        iN2 = 0
        
        for j in range(len(num2)-1,-1,-1):
            #print(num1[i],num2[j])
            
            n1 = ord(num1[i])-48
            n2 = ord(num2[j])-48
            #print(n2 * n1)
            
            nSum = n1 * n2 + res[iN1+iN2] + carry
            carry = nSum//10
            res[iN1+iN2] = nSum%10
            
            iN2+=1
            
        if (carry>0):
            res[iN1+iN2] = carry
        
        iN1+=1
    
    
    i = len(res)-1
    while (i>0 and res[i]==0):
        i-=1
    
    print(res , i) 
    
    res = res[:i+1][::-1]
    print(res)
    
    print(''.join(map(str,res)))
    
    
    
    
    
    
    
    
    