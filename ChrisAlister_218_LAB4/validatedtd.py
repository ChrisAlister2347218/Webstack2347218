from lxml import etree

def validate_xml(xml_file, dtd_file):
    try:
        with open(xml_file, 'rb') as xml_data, open(dtd_file, 'rb') as dtd_data:
            xml_tree = etree.parse(xml_data)
            dtd_tree = etree.DTD(dtd_data)
            valid = dtd_tree.validate(xml_tree)
            
            if valid:
                print("XML is valid against the DTD.")
            else:
                print("XML is not valid against the DTD.")
                print(dtd_tree.error_log)
    except Exception as e:
        print("An error occurred:", e)

xml_file = "productxml.xml"
dtd_file = "products.dtd"

validate_xml(xml_file, dtd_file)
