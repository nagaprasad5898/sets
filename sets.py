'''#python sets:
#set(iterable)
Set1=set()
Set2={}
Set3={1,2.5,'String',(1,2,3)}
Set4={1,2.5,'String',(1,2,3),1,2.5,'String'}
print('Set:',Set1,'type:',type(Set1))
print('Set:',Set2,'type:',type(Set2))
print('Set:',Set3,'type:',type(Set3))
print('Set:',Set4,'type:',type(Set4))
#Set5={1,'String',[1,2,3],{1,2}}
#Set5={1,'String',[1,2,3],{1,2}}'''
#operators
'''S1={1,2,'a'}
S2={1,2,3,4,5,'a','b'}
print('Set1:',S1)
print('Set2:',S2)
#+
#print(S1+S2)
#*
#print(S1*2)
#indexing|slicing
#print(S1[2])
#membership operators
for i in S1:
    print(i)'''
'''#union(*other_sets)
S1={1,2,'a'}
S2={1,2,3,4,'b','a'}
S3={2,7}
print('S1|S2:',S1|S2)
print('union of S1 and S2:',S1.union(S2))
print('S1|S2|S3:',S1|S2|S3)
print('union of S1,S2 and S3:',S1.union(S2,S3))
print('union of S1:',S1.union())'''
'''#|= => update(*other_sets)
S1={1,2,'a'}
S2={1,2,3,4,'b','a'}
S3={2,7}
S1|=S2 #S1=S1|S2
print('union S1 and S2:',S1.update(S2),S1)
print('union S1,S2 and S3:',S1.update(S2,S3),S1)
print('union S1:',S1.update(),S1)'''
'''#& =>intersection(other_sets)
S1={1,2,'a'}
S2={1,2,3,4,'b','a'}
S3={2,7}
print('S1&S2:',S1&S2)
print('intersection of S1 and S2:',S1.intersection(S2))
print('S1&S2&S3:',S1&S2&S3)
print('intersection of S1,S2 and S3:',S1.intersection(S2,S3))
print('intersection of S1:',S1.intersection())'''
'''
#& intersection_update(other_sets)
S1={1,2,'a'}
S2={1,2,3,4,'b','a'}
S3={2,7}
S1&=S2 #S1&S2
print('S1&S2:',S1&S2)
print('intersection of S1 and S2:',S1.intersection_update(S2),S1)
print('S1&S2&S3:',S1&S2&S3)
print('intersection of S1,S2 and S3:',S1.intersection_update(S2,S3),S1)
print('intersection of S1:',S1.intersection_update())
'''
'''#- =>difference(*other_sets):
S1={1,2,'a'}
S2={1,2,3,4,'b','a'}
S3={2,7}
print('S1-S2:',S1-S2)
print('difference:',S1.difference(S2))
print('S2-S1:',S2-S1)
print('difference:',S2.difference(S1))
print('S2-S1-S3:',S2-S1-S3)
print('difference:',S1.difference(S1,S3))'''

''' #- =>difference_update(*other_sets):
S1={1,2,'a'}
S2={1,2,3,4,'b','a'}
S3={2,7}
S1-=S2
print('S1-S2:',S1-S2)
print('difference:',S1.difference_update(S2),S1)
print('S2-S1:',S2-S1)
print('difference:',S2.difference_update(S1),S2)
print('S2-S1-S3:',S2-S1-S3)
print('difference:',S1.difference_update(S1,S3),S2)'''
'''#^ =>symmetric_difference(*other_sets):
S1={1,2,'a'}
S2={1,2,3,4,'b','a'}
S3={2,7}
print('S1^S2:',S1^S2)
print('symmetric_difference S1 and S2:',S1.symmetric_difference(S2))
print('S1^S2^S3:',S1^S2^S3)
##print('symmetric_difference S1,S2 and S3:',S2.symmetric_difference(S2,S3))'''
'''#^ =>symmetric_difference_update(*other_sets):
S1={1,2,'a'}
S2={1,2,3,4,'b','a'}
S3={2,7}
S1^=S2
print('S1^S2:',S1^S2)
print('symmetric_difference S1 and S2:',S1.symmetric_difference_update(S2))
print('S1^S2^S3:',S1^S2^S3)
#print('symmetric_difference S1,S2 and S3:',S2.symmetric_difference_update(S2,S3))'''
'''#<=issubset(other_set)
S1={1,2,'a'}
S2={1,2,3,4,'b','a'}
print(S1<=S2)
print(S1.issubset(S2))'''
'''#<=issuperset(other_set)
S1={1,2,'a'}
S2={1,2,3,4,'b','a'}
print(S2>=S1)
print(S2.issuperset(S1))
print(S1>=S2)
print(S1.issuperset(S2))'''
'''#remove(element)
A={'a','b'}
result=A.remove('b')
print('A=',A)
print('result=',result)'''
'''#discard(element)
A={'a','b'}
result=A.discard('b')
print('A=',A)
print('result=',result)'''
'''#pop():
A={'a','b','c'}
result=A.pop()
print('A=',A)
print('result=',result)'''
'''#clear():
A={'a','b','c'}
result=A.clear()
print('A=',A)
print('result=',result)
#copy():
A={'a','b','c'}
B=A
C=A.copy()
result=A.add(1)
print('A=',A)
print('B=',B)
print('C=',C)
print('result=',result)'''
'''#Built in methods:
#min(),max(),len(),del()
A={1,2,3,4}
B={'a','b','c','d'}
C={1,2,3,4,'a','b','c','d'}
print(len(A))
print(len(B))
print(len(C))
print(min(A))
print(min(B))
#print(min(C))
print(max(A))
print(max(B))
#print(max(C))

del A
print(A)'''
#Frozenset:
A={1,2,3,4}
B={'a','b','c','d'}
A_FS=frozenset(A)
B_FS=frozenset(B)
print(A_FS,B_FS)
print(type(A_FS))
print(type(B_FS))














