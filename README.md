# Wrench

## Challenge Description

Think of this challenge like a bolt and go build a wrench.

Here's your blueprint:

    1. Connect to the server on strfjebijc.qualifier.hackabit.com:54321 and get your challenge input.
    2. Add up all the decimal integers and only the decminal integers, no hex numbers or strings count
    3. Send that result back within 3 seconds to get the flag

## Challenge Information

Points: 125

## Solution

We start off by connecting to the server using

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the target host and port
sock.connect(('strfjebijc.qualifier.hackabit.com', 54321))

#initialize and declare sumOfNumbers to equal 0 in preparation for adding the integers found within the data
sumOfNumbers =0
```

After this adding up all the numbers is a rather simple while loop with a try/except as shown below

'''python
##collect a portion of the data from sock
data = sock.recv(10000).decode()

#loop through until there is no longer a '\n' in data and the data does not include 'total:' which should be right before the last bit of data is entered
while '\n' in data and data.find('total:') == -1:
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
    
    ##get new data to continue adding new numbers and to prevent an infinite loop in the while loop
    data = sock.recv(10000).decode()
'''

This will add up all the numbers until there is no longer a /n character and "total" is not included (as I found through testing that this will be included right before the flag).

We now just need to run the contents of the loop one more time because it won't register the last line of data (the one without the newline)

'''python
#seperate the lines in data into a list using the splitlines method, e.g. "hello\nwhy are you here?\n" becomes [{"hello"}, {"why are you here?"}]
lineList = data.splitlines()

#loop through the list created through the previous splitlines method, essentially checking each line of the data to see if it is an integer
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

'''

Once we've done this we can get our input by sending the sumOfNumbers that we've been curating to the target host

'''python

#convert the sumOfNumbers to a string so that it can be converted into byte form/encoded in the send request
strNumber2 = str(sumOfNumbers)

#send the sumOfNumbers after using .encode() to turn it into byte form
sock.send(strNumber2.encode())

'''

Now all that's left is to once more retrieve data from the host to get our flag then print it

'''python

##print the data that will be added after sending the encoded strNumbers2
print(sock.recv(10000).decode())

'''

# Flag

flag{i_feel_the_need_the_need_for_speed}