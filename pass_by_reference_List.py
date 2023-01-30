#Pass By Reference in mutable data type. For ex:- "LIST"

def Lis(L):
    print("New address of called function after clonning :- ",id(L))
    L.append(5)
    print("List after append :- ",L)
    print("Same address after calling function :- ",id(L))
    
L1 = [1,2,3,4]
print("Address of L1 List :- ",id(L1))
print("List :- ",L1)


Lis(L1[:])     #Cloning=> it helps to protect original data and after passing
                #L1 to function, the working address will change into new address
print("Original List :- ",L1)

print("END of list example.....")

#OUTPUT
"""
Address of L1 List :-  1746651575496
List :-  [1, 2, 3, 4]
New address of called function with :-  1746682690184
List after append :-  [1, 2, 3, 4, 5]
Same address after calling function :-  1746682690184
Original List :-  [1, 2, 3, 4]
END of list example.....
"""

#Pass By Reference in im-mutable data type. For ex:- "TUPLE"

def Tup(L):
    print("Same address after function called :- ",id(L))
    L = L +(5,6,7)
    print("New Tuple  after adding data",L)
    print("New address after appending",id(L))
    
L1 = (1,2,3,4)
print("Address of original tuple :-",id(L1))
print("Tuple :- ",L1)

Tup(L1)      #Here no need of cloning because it is immutable
print("Original Tuple",L1)
print("END of tuple example......")

"""
Address of original tuple :- 2307938715352
Tuple :-  (1, 2, 3, 4)
Same address after function called :-  2307938715352
New Tuple  after adding data (1, 2, 3, 4, 5, 6, 7)
New address after appending 2307938470376
Original Tuple (1, 2, 3, 4)
END of tuple example......
"""
