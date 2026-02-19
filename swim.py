import statistics
FOLDER = "swimdata/"
with open(FOLDER + "Abi-10-50m-Back.txt","r") as file:
    data = file.readlines()
    
for line in data:
    line =  line.strip()
print(line)

time = line.split(",")
hundredth =[]
for t in time:
    sec , rest =t.split(".")
    total_time = int(sec)*100 + int(rest)
    hundredth.append(total_time)
print(hundredth)

#now average time in hundredth of seconds
#reading = len(hundredth)
#avg_time_taken = sum(hundredth)/reading
#print("average time in 100th of sec is:",avg_time_taken)
#print(f"average time in seconds {avg_time_taken/100:.2f}")
print("avg time taken in hundredths of seconds",statistics.mean(hundredth))
print(f"avg time taken in seconds is {(statistics.mean(hundredth))/100:.2f} sec")














    