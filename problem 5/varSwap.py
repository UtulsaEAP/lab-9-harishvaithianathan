def swap_values(user_val1, user_val2, user_val3, user_val4):   
   user_val1, user_val2 = user_val2, user_val1
   user_val3, user_val4 = user_val4, user_val3

   return user_val1, user_val2, user_val3, user_val4

if __name__ == '__main__':   
   user_val1 = int(input())
   user_val2 = int(input())
   user_val3 = int(input())
   user_val4 = int(input())
   #store output for every input here
   swap_val1, swap_val2, swap_val3, swap_val4 = swap_values(user_val1, user_val2, user_val3, user_val4)
   print(swap_val1, swap_val2, swap_val3, swap_val4)

 