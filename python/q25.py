'''25. Write a program that validates XML/JSON formats against a schema.'''

from lxml import etree
import json
from jsonschema import validate, ValidationError, SchemaError

def validate_xml(xml_file, schema_file):
    try:
        xml_doc = etree.parse(xml_file) # XML file
        with open(schema_file, 'rb') as f:  # XSD schema in binary mode
            schema_doc = etree.XML(f.read())
        schema = etree.XMLSchema(schema_doc)
        # Validate XML file against XSD schema
        schema.assertValid(xml_doc)
        print("XML is valid against the schema.")
    except etree.XMLSyntaxError as e:
        print(f"XML Syntax Error: {e}")
    except etree.DocumentInvalid as e:
        print(f"XML is invalid: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def validate_json(json_file, schema_file):
    try:
        with open(json_file, 'r') as f: # JSON data
            json_data = json.load(f)
        with open(schema_file, 'r') as f: # JSON Schema
            schema = json.load(f)
        # Validate JSON against the schema
        validate(instance=json_data, schema=schema)
        print("JSON is valid against the schema.")
    except ValidationError as e:
        print(f"JSON validation error: {e.message}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    validate_xml("./dir/xml_file.xml", "./dir/xml_schema.xsd")
    validate_json("./dir/json_file.json", "./dir/json_schema.json")
