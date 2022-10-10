import xml.etree.ElementTree as ET

from .validator import validator


def xmlparser(path_to_xml):
    tree = ET.parse(path_to_xml)
    first_name_list = tree.findall('user/users/user/first_name')
    last_name_list = tree.findall('user/users/user/last_name')

    first_and_last_name = []

    for i in range(len(first_name_list)):
        if validator(first_name_list[i].text) != False and validator(last_name_list[i].text) != False and \
                validator(first_name_list[i].text) != '' and validator(last_name_list[i].text) != '':
            first_and_last_name.append(validator(first_name_list[i].text) + " " + validator(last_name_list[i].text))

    return first_and_last_name
