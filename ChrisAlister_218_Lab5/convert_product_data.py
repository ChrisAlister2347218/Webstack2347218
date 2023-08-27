from lxml import etree
import xmlschema


schema = xmlschema.XMLSchema('product_schema.xsd')

xml_tree = etree.parse('products.xml')

if schema.is_valid(xml_tree):
    print("XML data is valid according to the schema.")
    
    xslt_tree = etree.parse('transform.xsl')
    
    transformer = etree.XSLT(xslt_tree)
    result_tree = transformer(xml_tree)
    
    with open('product_catalogue.html', 'wb') as output_file:
        output_file.write(result_tree)
    
    print("HTML output saved to 'product_catalogue.html'.")
else:
    print("XML data is not valid according to the schema.")