import json
import sys
import jsonschema
from jsonschema import validate

jscheman = "json.schema"
jsondata = "package.json"


def loadschema(jschema):
    with open(jschema, 'r', encoding="utf-8") as f:
        schemadata = f.read()
        pschema = json.loads(schemadata)
    return pschema


# Testdata formatted as json(no errors)
data1 = {"protocolVersion": 1.0, "sentBy": "Tommy", "msgType": "Command", "commandList": "Run, along!",
         "statusCode": "I'm OK!", "parameterObj": {}, "dataObj": {}, "embeddedFileFormat": "", "embeddedFile": ""}
# Testdata formatted as json(with error in dataObj - it is formatted as a string and sentBy is missing)
data2 = {"protocolVersion": 2.0, "msgType": "Dos", "commandList": "Go away!",
         "statusCode": "I'm not OK!", "parameterObj": {}, "dataObj": "", "embeddedFileFormat": "", "embeddedFile": ""}


# Function to make a json file, it'll be called package.json
def writeToJsonFile(outputfile, data):
    with open(outputfile, 'w', encoding="utf-8") as jsonFile:
        json.dump(data, jsonFile)


# Function to read from a json file, its called package.json
def readFromJsonFile(inputfile):
    with open(inputfile, 'r', encoding="utf-8") as datafile:
        loaded = json.load(datafile)
    return loaded


# Function for validating jsondata - it returns an error if it doens't fit the schema
def validering(jsondata, schema):
    print("Validating the input data using jsonschema:")
    try:
        validate(jsondata, schema)
        sys.stdout.write("Record #{}: OK\n".format(jsondata))
    except jsonschema.exceptions.ValidationError as ve:
        sys.stderr.write("Record #{}: ERROR\n".format(jsondata))
        sys.stderr.write(str(ve) + "\n")


# Teststuff
#schema = loadschema(jscheman)
#writeToJsonFile("faultypackage.json", data2)
#writeToJsonFile("okpackage.json", data1)
#data = readFromJsonFile("okpackage.json")
#validering(readFromJsonFile("okpackage.json"), loadschema(jscheman))
#intake = readFromJsonFile("faultypackage.json")
#validering(intake, schema)