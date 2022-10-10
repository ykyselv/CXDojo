import csv
import datetime
from .models import User
from .validator import validator
from .xmlparser import xmlparser


def data_collector(path_to_csv, path_to_xml):
    file = open(path_to_csv)
    reader = csv.reader(file)
    rows = []

    for row in reader:
        rows.append(row)

    xml_list = xmlparser(path_to_xml)
    collected_info = {}

    for r in rows:
        if validator(r[0]) != False and validator(r[0]) != False and \
                validator(r[0]) != '' and validator(r[0]) != '':
            for el in xml_list:

                if validator(r[0]).split('.')[-1] != '' and (validator(r[0]).split('.')[-1].title()) in el:
                    collected_info['username'] = validator(r[0])
                    collected_info['password'] = validator(r[1]).split('.')[-1]
                    collected_info['date_joined'] = datetime.datetime.utcfromtimestamp(
                        int(validator(r[2]).split('.')[-1]))

                    collected_info['first_name'] = el.split(' ')[0]
                    collected_info['last_name'] = el.split(' ')[1]
                    User.objects.create_user(username=collected_info['username'], password=collected_info['password'],
                                             first_name=collected_info['first_name'],
                                             last_name=collected_info['last_name'],
                                             date_joined=collected_info['date_joined'])
