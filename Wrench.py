import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the target host and port
sock.connect(('strfjebijc.qualifier.hackabit.com', 54321))

#initialize and declare sumOfNumbers to equal 0 in preparation for adding the integers found within the data
sumOfNumbers =0

##collect a portion of the data from sock
data = sock.recv(10000).decode()

# loop through until there is no longer a '\n' in data and the data does not include 'total:' which should be right before the last bit of data is entered
while '\n' in data and data.find('total:') == -1:
    #seperate the lines in data into a list using the splitlines method, e.g. "hello\nwhy are you here?\n" becomes [{"hello"}, {"why are you here?"}]
    lineList = data.splitlines()

    ## unnecessary testing print statement to print data 
    # print(data)

    # loop through the list created through the previous splitlines method, essentially checking each line of the data to see if it is an integer
    for x in lineList:
        #use try/except to check if the number can be converted into an integer
        try:
            #check if the number can be converted into an integer
            number = int(x)

            #if there is no ValueError and it can be converted into an integer, add it to the sum of Numbers
            sumOfNumbers += number
        
        #do nothing if the message/string can't be converted to an integer
        except ValueError:
            pass
    
    ##get new data to continue adding new numbers and to prevent an infinite loop in the while loop
    data = sock.recv(10000).decode()

##NOTE: this is a repeat of the code in the previous loop due to the fact that the while loop could miss the end of the message

#seperate the lines in data into a list using the splitlines method, e.g. "hello\nwhy are you here?\n" becomes [{"hello"}, {"why are you here?"}]
lineList = data.splitlines()

# loop through the list created through the previous splitlines method, essentially checking each line of the data to see if it is an integer
for x in lineList:
    #use try/except to check if the number can be converted into an integer
    try:
        #check if the number can be converted into an integer
        number = int(x)

        #if there is no ValueError and it can be converted into an integer, add it to the sum of Numbers
        sumOfNumbers += number
        
    #do nothing if the message/string can't be converted to an integer
    except ValueError:
        pass

# convert the sumOfNumbers to a string so that it can be converted into byte form/encoded in the send request
strNumber2 = str(sumOfNumbers)

#send the sumOfNumbers after using .encode() to turn it into byte form
sock.send(strNumber2.encode())

##print the data that will be added after sending the encoded strNumbers2
print(sock.recv(10000).decode())

#close the socket/end the connection
sock.close