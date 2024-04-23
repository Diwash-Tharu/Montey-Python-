def data_entry():
    """This function is used to caclulate the average speed of the bird that is recorded in the europe and UK and show the result in 
    kilometer and miles"""
    data_s = []

    print("\n\t\t Swallow Speed Analysis: Version 1.0") 
    while True:
        user = input("\n Enter the next reading: ")
        if "U" in user  or "u" in user: # this check whether thres is U in the given data or not
            c = float(user[1:]) # this  slicing function is used for removing  first apphebet and cverting into float  
            data_s.append(c) #adding the conterted  float into the empty list at last
            print("Reading saved")
        elif "E"  in user or "e" in user:
            c = float(user[1:])   # this  slicing function is used for removing  first apphebet and cverting into float
            ab = c/1.61 # converting km into miles
            data_s.append(ab) #adding the conterted  float into the empty list at last 
            print("Reading saved")
        elif user == (""): 
            break
        else:
            print("worng Input")
            continue
    function_2(data_s) # passin the values into other function

def function_2(data_s): # calling the values into the function 
    """This function will convert miles into  km and km into mile"""
    if len(data_s) >= 1 : # checking whether the count number is greather thean 1 or not     
        print("\n Result Summery")
        sum = 0        
        for  i in range(len(data_s)): #this will loop whill all the end of the data 
            sum = sum + data_s[i]  # the looped data is than added one by one
        km_avg = sum/len(data_s) 
        km_max = max(data_s) 
        km_min = min(data_s)

        mile_Avg = km_avg*1.61
        mile_max = km_max*1.61
        mile_min = km_min*1.61
        print("%d reading analysed"%(len(data_s))  if len(data_s)>=1 else "%d readings analysed"%(len(data_s)))# -1 is done because inital 1 and added again 1  so  - 1 is done   
        print("Max speed: {:.1f} MPH {:.1f} KPH".format(mile_max,km_max))
        print("Min speed: {:.1f} MPH {:.1f} KPH".format(mile_min,km_min))
        print("Avg speed: {:.1f} MPH {:.1f} KPH".format(mile_Avg,km_avg)) 
    else:
        print("No readings entered. Nothing to do.")    
data_entry()