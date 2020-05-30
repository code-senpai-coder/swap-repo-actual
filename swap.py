import shlex 
import time
#input : Matyas Balcar
#output : Balcar Matyas

def swap(str_par):
    
    result_swaped = ""
    str_arr = shlex.split(str_par)
    str_arr[0], str_arr[1] = str_arr[1], str_arr[0]
    for ele in str_arr:
         result_swaped += ele
         result_swaped += " "
    result = f"{result_swaped} is your swaped string"
    return result
curtime = time.time()
print(swap("Matyas Balcar"))
print(f"This function took {time.time() - curtime} seconds to finish ")
