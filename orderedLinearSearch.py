#Ordered linear search

mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
myterm = 21

def search(ordered_list, term): 
   ordered_list_size = len(ordered_list) 
   for i in range(ordered_list_size): 
      if term == ordered_list[i]: 
         print('Index of my number = ' + ' ' + str(i))
         print('Number I want to search for = ' + ' ' + str(my_term)) 
      elif ordered_list[i] > term: 
         return None 

   return None

search(my_list, my_term)
