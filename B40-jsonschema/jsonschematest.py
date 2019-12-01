import json
import sys

import jsonschema
from jsonschema import validate

"""
Jsonschematest

Contains functions to import a jsonschema, 
read/write json files and strings and to validate those.
"""


# Function to load a jsonschema
def load_schema(jschema):
    """
    Loads jsonschema from file

    :param jschema:
    Takes a filename as a string
    :return:
    """
    with open(jschema, 'r', encoding="utf-8") as f:
        return json.loads(f.read())


# Function to make a json file, it'll be called package.json
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


# Writes a json string
def write_jsonstr(var):
    """
    Write "jsonly" correct json string

    :param var:
    :return:
    """
    return json.dumps(var)


# Reads a json string
def read_jsonstr(var):
    """
    Read json-data from string

    :param var:
    :return:
    """
    return json.loads(var)


# Function to read from a json file, its called package.json
def read_jsonfile(inputfile):
    """
    Read json-data from file

    :param inputfile:
    Json file containing data
    :return:
    """
    with open(inputfile, 'r', encoding="utf-8") as datafile:
        return json.load(datafile)


# Function for validating jsondata - it returns an error if it doens't fit the schema
def validering(jsondata, schema):
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
