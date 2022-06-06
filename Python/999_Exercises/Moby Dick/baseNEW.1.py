#sentence = "whale hello there. Don't we all love whales? I absolutely love whales! whales are so huge!!!"
#thislist = ["whale", "Whales"]
#x = sentence[0:len(x)]
#for i in((x[0:len(x)])
    #if x == thislist:
        #int(input(x))
        #print(x)
count = 0
sentence = "whale hello there. Don't we all love whales? I absolutely love whales! whales are so huge!!!"
for i in range(0,len(sentence)):
    if sentence[i:i + 5] == "whale":
        count = count + 1
print(count)
        
        












#with open('moby.txt') as f:
#    for line in f:
#        sentence = line.strip()
#        ##YOUR CODE GOES HERE
#
#f.close()
