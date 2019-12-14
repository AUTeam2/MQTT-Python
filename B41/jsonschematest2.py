import json
import sys

import jsonschema
from jsonschema import validate

"""
Jsonschematest

Contains functions to import a jsonschema, 
read/write json files and strings and to validate those.
"""


class JsonSchemaClass:


    @classmethod
    def load_schema(cls, jschema):
        """
        Loads jsonschema from file

        :param jschema:
        Takes a filename as a string
        :return:
        """
        with open(jschema, 'r', encoding="utf-8") as f:
            cls.loaded_schema = json.loads(f.read())



    @staticmethod
    def write_jsonfile(outputfile, data):
        """
        Write "jsonly" correct json files

        :param outputfile:
        Name of the file to be as a string
        :param data:
        Data to be jsonly written in the file
        :return:
        """
        with open(outputfile, 'w', encoding="utf-8") as jsonFile:
            json.dump(data, jsonFile)

    @staticmethod
    def write_jsonstr(var):
        """
        Write "jsonly" correct json string

        :param var:
        :return:
        """
        return json.dumps(var)

    @staticmethod
    def read_jsonstr(var):
        """
        Read json-data from string

        :param var:
        :return:
        """
        return json.loads(var)

    @staticmethod
    def read_jsonfile(inputfile):
        """
        Read json-data from file

        :param inputfile:
        Json file containing data
        :return:
        """
        with open(inputfile, 'r', encoding="utf-8") as datafile:
            return json.load(datafile)

    @staticmethod
    def validating(jsondata, schema):
        """
        Validates json-data against schema

        :param jsondata:
        The variable containing json-data
        :param schema:
        The schema to compare against
        :return:
        """
        print("Validating the input data using jsonschema:")
        try:
            validate(jsondata, schema)
            sys.stdout.write("Record #{}: OK\n".format(jsondata))
        except jsonschema.exceptions.ValidationError as ve:
            sys.stderr.write("Record #{}: ERROR\n".format(jsondata))
            sys.stderr.write(str(ve) + "\n")


js = JsonSchemaClass()
js.load_schema("json.schema")

#print(js.loaded_schema['properties'])

# modtaget_str -> read_jsonstr -> validating -> så kan vi udlæse variabler

modtaget_json = {"protocolVersion": 1.0, "sentBy": "Tommy", "msgType": "Command", "commandList": "Run, along!",
              "statusCode": "I'm OK!", "parameterObj": {}, "dataObj": {}, "embeddedFileFormat": "", "embeddedFile": ""}

modtaget_str = '{"protocolVersion": 1.0, "sentBy": "dinMor", "msgType": "command", "commandList": [], "statusCode": "200", "parameterObj": {}, "dataObj": {}, "embeddedFileFormat": "", "embeddedFile": ""}'

jsobj = js.read_jsonstr(modtaget_str)


# modtaget_json skal være i JSON-format, ikke en streng
js.validating(jsobj, js.loaded_schema)

#print(jsobj["commandList"])


# Jeg har værdier -> skal pakkes ind i obj. -> skal gøres til JSON -> skal valideres -> afsendes

class Message():

    # This can be sent when filled
    payload = js.loaded_schema["properties"]

    def unpack(self, protocolVersion, sentBy, msgType, commandList, statusCode, parameterObj, dataObj, embeddedFileFormat, embeddedFile):
        self.protocolVersion = protocolVersion
        self.sentBy = sentBy
        self.msgType = msgType
        self.commandList = commandList
        self.statusCode = statusCode
        self.parameterObj = parameterObj
        self.dataObj = dataObj
        self.embeddedFileFormat = embeddedFileFormat
        self.embeddedFile = embeddedFile

    def pack(self):
        self.payload["protocolVersion"] = self.protocolVersion
        self.payload["sentBy"] = self.sentBy
        self.payload["msgType"] = self.msgType
        self.payload["commandList"] = self.commandList
        self.payload["statusCode"] = self.statusCode
        self.payload["parameterObj"] = self.parameterObj
        self.payload["dataObj"] = self.dataObj
        self.payload["embeddedFileFormat"] = self.embeddedFileFormat
        self.payload["embeddedFile"] = self.embeddedFile

msg = Message()
msg.unpack(**jsobj)

msg2 = msg

msg2.sentBy = "Marc"
msg2.embeddedFile = "blablab"
msg2.pack()

#validate
#print(msg2.payload)

jstr = js.write_jsonstr(msg2.payload)
j2str = js.read_jsonstr(jstr)

js.validating(j2str, js.loaded_schema)

# modtaget t -> t2 -> ændrer værdier -> sender

