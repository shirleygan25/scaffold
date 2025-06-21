def set_flag(flag):
    # Sets flag to True no matter current value  
    flag = True
    print(f'Flag is now {flag}')
    
flag1 = True 
flag2 = False

set_flag(flag1) # Flag is now True  
set_flag(flag1) # Flag is now True - Idempotent

set_flag(flag2) # Flag is now True
