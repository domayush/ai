def fuzzy_union(A,B):
    fuzzy_Set_C=[]
    for a in A:
        for b in B:
            if(a[0]==b[0]):
                fuzzy_Set_C.append([a[0],max(a[1],b[1])])
                break
    return fuzzy_Set_C

def fuzzy_intersection(A,B):
    fuzzy_Set_C=[]
    for a in A:
        for b in B:
            if(a[0]==b[0]):
                fuzzy_Set_C.append([a[0],min(a[1],b[1])])
                break
    return fuzzy_Set_C

def fuzzy_complement(X):
    fuzzy_Set_C=[]
    for a in X:
        fuzzy_Set_C.append([a[0],round(1-a[1],3)])
    return fuzzy_Set_C

def fuzzy_difference(A,B):
    fuzzy_Set_C=[]
    for a in A:
        for b in B:
            if(a[0]==b[0]):
                fuzzy_Set_C.append([a[0],min(a[1],round(1-b[1],3))])
                break
    return fuzzy_Set_C

def fuzzy_bounded_difference(A,B):
    fuzzy_Set_C=[]
    for a in A:
        for b in B:
            if(a[0]==b[0]):
                fuzzy_Set_C.append([a[0],max(0,round(a[1]-b[1],3))])
                break
    return fuzzy_Set_C



def fuzzy_bounded_sum(A,B):
    fuzzy_Set_C=[]
    for a in A:
        for b in B:
            if(a[0]==b[0]):
                fuzzy_Set_C.append([a[0],min(round(a[1]+b[1],3),1)])
                break
    return fuzzy_Set_C

def display(X):
    for i in X:
        print(i)

fuzzy_Set_A=[["a",0.2],["b",0.3],["c",0.6],["d",0.6]]
fuzzy_Set_B=[["a",0.9],["b",0.9],["c",0.4],["d",0.5]]

A=fuzzy_Set_A
B=fuzzy_Set_B        
for i in A:
    flag=0
    for j in B:
        if(i[0]==j[0]):
            flag=1  
            break
    if(flag==0):
        B.append([i[0],0]) 

A=fuzzy_Set_B
B=fuzzy_Set_A
for i in A:
    flag=0
    for j in B:
        if(i[0]==j[0]):
            flag=1  
            break
    if(flag==0):
        B.append([i[0],0]) 

print("\nFuzzy Set A = ",fuzzy_Set_A)              
print("\nFuzzy Set B = ",fuzzy_Set_B)              
print("\n1. Union(A,B):",fuzzy_union(fuzzy_Set_A,fuzzy_Set_B))
print("\n2. Intersection(A,B):",fuzzy_intersection(fuzzy_Set_A,fuzzy_Set_B))
print("\n3. Complement(A):",fuzzy_complement(fuzzy_Set_A))
print("\n4. Complement(B):",fuzzy_complement(fuzzy_Set_B))
print("\n6. Bounded_Sum(A,B):",fuzzy_bounded_sum(fuzzy_Set_A,fuzzy_Set_B))
print("\n7. Difference(A,B):",fuzzy_difference(fuzzy_Set_A,fuzzy_Set_B))
