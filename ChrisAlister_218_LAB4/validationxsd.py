from lxml import etree

def validate_xml(xml_file, xsd_file):
    try:
        with open(xml_file, 'rb') as xml_data, open(xsd_file, 'rb') as xsd_data:
            xml_tree = etree.parse(xml_data)
            xsd_tree = etree.parse(xsd_data)
            xmlschema = etree.XMLSchema(xsd_tree)
            valid = xmlschema.validate(xml_tree)
            
            if valid:
                print("XML is valid against the XSD schema.")
            else:
                print("XML is not valid against the XSD schema.")
                print(xmlschema.error_log)
    except Exception as e:
        print("An error occurred:", e)

xml_file = "product_info.xml"
xsd_file = "product_info.xsd"

validate_xml(xml_file, xsd_file)
