import json
import sys
import jsonschema
from jsonschema import validate

"""
Jsonschematest

Contains functions to import a jsonschema, 
read/write json files and strings and to validate those.
"""

testshcema = {
    "$schema": "AUTeam2 JSONschema",
    "title": "PayloadSchema",
    "type": "object",
    "properties": {
        "protocolVersion": {"type": "number"},
        "sentBy": {"type": "string"},
        "msgType": {"type": "string"},
        "commandList": {"type": "string"},
        "statusCode": {"type": "string"},
        "parameterObj": {"type": "object"},
        "dataObj": {"type": "object"},
        "embeddedFileFormat": {"type": "string"},
        "embeddedFile": {"type": "string"}
    },
    "required": ["protocolVersion", "sentBy", "msgType"]
}


class JsonSchemaClass():

    @staticmethod
    def load_schema(jschema):
        """
        Loads jsonschema from file

        :param jschema:
        Takes a filename as a string
        :return:
        """
        with open(jschema, 'r', encoding="utf-8") as f:
            return json.loads(f.read())

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
            sys.stdout.write("Validation OK\n")
        except jsonschema.exceptions.ValidationError as ve:
            sys.stderr.write("Record #{}: ERROR\n".format(jsondata))
            sys.stderr.write(str(ve) + "\n")


js = JsonSchemaClass()
proto = js.load_schema("json.schema")


class Message():
    # This can be sent when filled
    payload = proto["properties"]

    def unpack(self, protocolVersion, sentBy, msgType, commandList, statusCode, parameterObj, dataObj,
               embeddedFileFormat, embeddedFile):
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
