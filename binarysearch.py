import math

# QUESTION 1 : Alice has some cards with numbers written on them.
#She arranges the cards in decreasing order,
# and lays them out face down in a sequence on a table. 
# She challenges Bob to pick out the card containing a given number by turning over 
# as few cards as possible. Write a function to help Bob locate the card.
# ------------------solution steps------------------------------------------------------------------------------------

#1. State the problem clearly. Identify the input & output formats.
# def locate_card(cards,query):
#     pass

# 2. Come up with some example inputs & outputs. 
# Try to cover all edge cases --->








tests=[]

#-The number query occurs somewhere in the middle of the list cards.
tests.append(
    {
    'input':{
       'cards': [10,9,8,7,6,5,4,3,2,1],
       'query':7
    },
    'output':3
}
)
#-query is the first element in cards.

tests.append(
    {
    'input':{
       'cards': [10,9,8,7,6,5,4,3,2,1],
       'query':10
    },
    'output':0
}
)

#-query is the last element in cards.
tests.append(
    {
    'input':{
       'cards': [10,9,8,7,6,5,4,3,2,-2],
       'query':-2
    },
    'output':9
}
)

#-The list cards contains just one element, which is query.
tests.append(
    {
    'input':{
       'cards': [10],
       'query':10
    },
    'output':0
}
)

#-The list cards does not contain number query.
tests.append(
    {
    'input':{
       'cards': [10,9,8,7,6,5,4,3,2,-2],
       'query':0
    },
    'output':-1
}
)
#-The list cards is empty.
tests.append(
    {
    'input':{
       'cards': [],
       'query':-2
    },
    'output':-1
}
)
#-The list cards contains repeating numbers.
tests.append(
    {
    'input':{
       'cards': [10,9,8,7,7,7,5,4,3,2,-2],
       'query':9
    },
    'output':1
}
)
#-The number query occurs at more than one position in cards.
tests.append(
    {
    'input':{
       'cards': [10,9,8,7,6,5,4,3,2,-2,-2,-2],
       'query':-2
    },
    'output':9
}
)

# 3. Come up with a correct solution for the problem. State it in plain English:
# assuming input is always a descendent arranged, 
# 1- I create a variable 'position'=0
# 2- while position < list length check the number selected if == the query then return the position
# 3-if the position =length break and return -1
# 4-if the list is empty return -1



def locate_card_linear(cards,query):
    position=0
    if len(cards)==0:
        return -1
    while position<len(cards):
        if cards[position]==query:
            return position
        else:
            position+=1
            
    return -1
#now test the function created
for test in tests:
    print(locate_card_linear(**test['input'])==test['output'])
#voilaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa !!!!

#***complixity of time and space and big O notation:
# big O notation is the worest case, for more: https://devopedia.org/algorithmic-complexity#:~:text=Algorithmic%20complexity%20is%20a%20measure%20of%20how%20long,complexity%20is%20calculated%20asymptotically%20as%20n%20approaches%20infinity.

#binary search
# again the same problem:
#1.set a middle flag variable to the value of the middle element 2.evalute the element compared to the query
# 3.if query>element value recall the function to the left half else if less to the right side if == query return the position
# 4.else; it is not found then return -1 
# 5.check if the list empty
#solution----------------------------------
def locate_card_binary(cards,query):
    if len(cards)==0:
        return -1
    middle_postion=int(len(cards)/2)
    middle_flag=cards[middle_postion]

    if middle_flag == query:
        return middle_postion
    elif middle_flag<query:
            locate_card_binary(cards[0:middle_postion],query)
    else:
            locate_card_binary(cards[(middle_postion+1):],query)
        
    return -1

for test in tests:
      if locate_card_binary(**test['input'])==test['output'] == False:
         print('test:\n',locate_card_binary(**test['input']),'\n','expected:\n',test['output'])
for test in tests:
    print(locate_card_linear(**test['input'])==test['output'])
#test complixity..............................
import time

#python -m pip install -U matplotlib >>
import pip
# pip.main(["install","matplotlib"])
import matplotlib.pyplot as plt
def test_complixity():
    
    n=2
    start0=time.time()
    inputs=list()
    durations=list()
    for n in range(0,5000,1):
        
        if time.time()-start0>10.0:
            
            print('run time !')
            break
        start=time.time()
        input_n=list(range(n,0,-1))
        #function to be tested !!
        locate_card_binary(input_n,n)
        
        
        end=time.time()
        duration=f'{(end-start):.12f}'
        inputs.append(n)
        durations.append(duration)
        #print(duration,n)
    
    plt.xlabel("No. of elements")
    plt.ylabel("Time required")
    plt.plot(inputs,durations)
    # f = plt.figure()
    # f.set_figwidth(12)
    # f.set_figheight(3)
    plt.show()
    print('done')
test_complixity()

    





# plt.plot(time_n,list(input_n))
# plt.show()
# print(input_n)

# print(time_n)
