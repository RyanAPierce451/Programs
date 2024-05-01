"""
************
PROGRAMMER:     RYAN A PIERCE
DATE:           FEBRUARY 16, 2023
ASSIGNMENT:     HOMEWORK #3: PROCESS LOG FILE DATA

ALGORITHM:      LOOKS FOR ALL THE ERROR CODES IN A LOGFILE AND THEN WRITES THOSE ERRORS OUT
                TO INDIVIDUAL ERROR FILES SO THAT THEY CAN BE HANDLED BY THE APPROPRIATE IT SUPPORT TEAM. 
************
"""

# define a function to remove duplicates from a file
def remove_duplicates(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    
    # remove duplicates from lines
    lines = list(set(lines))

    # open file in write mode and write unique line
    with open(file_name, "w") as file:
        for line in lines:
            file.write(line)

# sets the name of the log file
logfile = "logfile.txt"

# initializes empty lists for file records, status codes, and file errors
Filecontainer = []
StatusCode = []
FileError = []
Errors = []
ClientErrors = []
ServerErrors = []

# defines a range of error codes and converts them to strings with spaces on either side
e = (list(range(400,600)))
request = ['GET ', 'HEAD ', 'POST ']
errorcode = []
for i in range (len(e)):
    errorcode += [" " + str(e[i]) + " "]

# opens the log file and read all the lines
with open(logfile) as file:
    Logsheet = file.readlines()

    # iterates through the lines and extract the part of the record that comes after the timestamp
    for i in range(len(Logsheet)):
        if '] "' in Logsheet[i]:
            C = "]"
            RecordEnd = str(Logsheet[i]).split(C,1)[1]
            Filecontainer += [RecordEnd]

# iterates through the file records and remove the HTTP method (GET, HEAD, POST) and any trailing data
for i in range(len(Filecontainer)):
    if " HTT" in Filecontainer[i]:
        C = " HTT"
        RecordEnd = str(Logsheet[i]).split(C,1)[0]
        Filecontainer[i] = RecordEnd
    for j in range(len(request)):
        if request[j] in Filecontainer[i]:
            C = request[j]
            RecordEnd = str(Filecontainer[i]).split(C,1)[1]
            Filecontainer[i] = RecordEnd

# iterates through the log file lines and extract any error codes and the corresponding file records
for i in range(len(Logsheet)):
    for j in range (len(errorcode)):
        if errorcode[j] in Logsheet[i]:
            StatusCode += [str(errorcode[j]).strip()]
            FileError += [str(Filecontainer[i]).strip()]

# iterates through the extracted status codes and file records and create error messages
for i in range(len(StatusCode)):
    Errors += ["Status Code: " + StatusCode[i] + "   File: " + FileError[i]]

# iterates through the error messages and separate client errors (status codes <= 499) from server errors (status codes >= 500)
for i in range(len(Errors)):
    if int(StatusCode[i]) <= 499:
        ClientErrors += [Errors[i]]
    elif int(StatusCode[i]) >= 500:
        ServerErrors += [Errors[i]]

# opens a file for writing and write out the client error messages
with open("Client_Errors.txt", "w") as file:
    for i in range(len(ClientErrors)):
        file.write(str(ClientErrors[i])+"\n")

# open a file for writing and write out the server error messages
with open("Server_Errors.txt", "w") as file:
    for i in range(len(ServerErrors)):
        file.write(str(ServerErrors[i])+"\n")

# remove duplicates from the client error file
remove_duplicates("Client_Errors.txt")

# remove duplicates from the server error file
remove_duplicates("Server_Errors.txt")