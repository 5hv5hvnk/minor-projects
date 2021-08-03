import numpy as np
import sys
arguments = sys.argv

try : 
    sys.stdin = open(arguments[1], 'r')
    sys.stdout = open(arguments[2], 'w')
    type = arguments[3]

    n1,m1 = map(int,input().split())
    mat1 = []
    for i in range(n1):
        temp = list(map(int,input().split()))
        mat1.append(temp.copy())
    n2,m2 = map(int,input().split())
    mat2 = []
    for i in range(n2):
        temp = list(map(int,input().split()))
        mat2.append(temp.copy())
    mat1 = np.array(mat1)
    mat2 = np.array(mat2)
    
    
    if type == '1' and ((n1 != n2) or (m1 != m2)):
        print("Dot Product not posible")
        exit()
    elif type =='2' and n1 != m2:
        print("Multiplication not possible") 
        exit() 

    if type == '1':
        print(A*B)
    else : 
        print(np.matmul(A,B))
        
        

except:
        print("Wrong Format")