from lxml import etree

from urban_journey.ujml.root_ujml_node import UjmlNode
from ..ujml_element import UjmlElement


# Public
def from_string(ujml_string, file_name="<ujml_input>"):
    parser = etree.XMLParser()
    lookup = etree.ElementDefaultClassLookup(element=UjmlElement)
    parser.set_element_class_lookup(lookup)
    root_elem = etree.fromstring(ujml_string, parser)
    ujml_node = UjmlNode(root_elem, file_name)
    return ujml_node