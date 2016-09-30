import xml.etree.ElementTree as ET
root = ET.parse("sample.xml").getroot()
print "root tag : %s, root attrib : %s" %(root.tag, root.attrib)
for child in root.iter('type'):
    print child
    print child.tag, child.attrib
