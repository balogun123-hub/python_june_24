'''
# Create a list of at least 5 states and capital 
# write a program that collect user option 1 - 4
# 1. Display all states and Capital to the list 
# 2. Add new state and Capital to the list 
# 3. Edit a particular state and its Capital
# 4. Delete a particular state and its Capital

'''

    
State_Capital = [ 
    {
       'State' : 'Oyo' ,
       'Capital' : 'Ibadan'
    },
    {
       'State' : 'Oyo' ,
       'Capital' : 'Ibadan'
    },
    {
       'State' : 'Oyo' ,
       'Capital' : 'Ibadan'
    },
    {
       'State' : 'Oyo' ,
       'Capital' : 'Ibadan'
    }, 
   ]


    
def main(main_list):
  
     def display(st_list): #parameter/requirement
                
          for each_item in st_list:
             # print(each_item
             pos = st_list.index(each_item)
             print(f'{pos+1}. {each.item['state']} - {each_item['capital']}')
def  add(): 
     new_state = input('Enter the name of the new state:')
     new_capital = input('Enter the name of the new Capital:')
     st_cp = {
          'state' : new_state,
          'capital' : new_Capital 
     }
def main(main_list):
     def add():
             'state' : new_state,
