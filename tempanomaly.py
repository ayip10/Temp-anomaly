filename = input("Temperature anomaly filename:")
infile = open(filename, "r")



#prints each line in infile excluding first five, strips newlines
for i in range (5):
    infile.readline()



listyear = []
listtemp = []

for line in infile:
    line = line.rstrip("\n")
    (year, temperature)=line.split(",")
    temperature = float(temperature)
    listyear.append(int(year))
    listtemp.append(float(temperature))
 
for i in range(askuser, len(listtemp)-askuser):
    average = (sum(listtemp[i-askuser:askuser+i+1])/len(listtemp[i-askuser:askuser+1+i]))
    #print(listyear[i],"{:.4f}".format(average), sep = ",")
    outputlistyear = str(listyear[i])
    output = outputlistyear + "," + "{:.4f}".format(average) + "\n"
    outfile.write(output)
 
outfile.close()
infile.close

