import os
import glob
import xml.etree.ElementTree as ET

i = 0
for xml_file in glob.glob('./data/trainval_annotation/instrument_*.xml'):
    targetXML = open(xml_file, 'rt', encoding='UTF8')
    tree = ET.parse(targetXML)
    root = tree.getroot()
    
#     target_tag = root.find('filename')
#     original = target_tag.text
#     modified = original.replace("jpg","jpeg")
#     target_tag.text = modified
    
    for member in root.findall('object'):
        target_tag = member[0]
        original = target_tag.text
        modified = original.replace("sneakers","instrument")
        target_tag.text = modified
    tree.write(xml_file)
    i += 1
print(i)