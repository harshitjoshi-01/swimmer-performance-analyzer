import statistics
FOLDER = "swimdata/"

def get_swim_data(fn):
    #opens the file and gives the detaila about the name of the file eg; swimmer's name ,age,dist,stroke
    swimmer , age , dist , stroke = fn.removesuffix(".txt").split("-")
    with open(FOLDER + fn) as file:
        data = file.readlines()
        
    times = data[0].strip().split(",")#strips the \n and split the list by commas
    converted =[]#created a list to store the count of time in the file
    #for loops through each anbd every value inside the file and stroes it inside the converted list
    for t in times:
        if ":" in t:
            min_part , rest = t.split(":")
            sec , hundredth = rest.split(".")
        else:
            min = 0
            sec , hundredth = t.split(".")
        total_time = int(min_part)*60*100 + int(sec)*100 + int(hundredth)
        converted.append(total_time)#at the end of each looping this adds vakue to the list 

    avg_100th= statistics.mean(converted) #statistics.mean(converted)used to find average of the total time
    averagetime_inseconds = round((statistics.mean(converted))/100 , 2) #100th of sec converted back into seconds

   # min_sec , hundredths = str(round((statistics.mean(converted))/100 , 2)).split("."){alternate of the .2f method }
    min_sec , hundredths = str(round((statistics.mean(converted))/100 , 2)).split(".")

    min_sec = int(min_sec)
    minutes = int(min_sec) // 60 #divides the min_sec value by 60 and the quotient is taken as min and remainder in taken as remaining seconds
    seconds = min_sec - minutes*60 #gives the remaining seconds after  previous aboven calculation 
    average_time = str(minutes) + ":" + str(seconds) + "." + str(hundredths)    #gives the str values as time shown in the file 
    return swimmer , age , dist , stroke , times , avg_100th , averagetime_inseconds ,   average_time




