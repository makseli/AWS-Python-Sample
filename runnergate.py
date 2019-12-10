#!/usr/bin/env python3

import sys
import getopt
import helper
from ec2 import Ec2


if len(sys.argv) < 2:
    exit("please add a parameter! \nec2 out")

method_name = helper.set_val_safe(sys.argv, 1, True)

callable_methods = ['list-all', 'list-nodes']

if method_name not in callable_methods:
    exit("please enter a correct available method & parameters! \ngate close")

general = Ec2

if method_name == 'list-all':

    instance_list = general().list_nodes()

    if len(instance_list) < 1:
        exit("No instance\nec2 out")

    for nodes in instance_list["Reservations"]:
        for instance in nodes["Instances"]:
            print(instance['InstanceId'], instance['PrivateIpAddress'])


elif method_name == 'list-nodes':

    customer_id = ''
    try:
        opts, gnl = getopt.getopt(sys.argv[2:], "i:", ['customer-id='])

        for opt, arg in opts:
            if opt in ('-i', '--customer-id'):
                customer_id = arg
    except getopt.error as exc:
        exit("wrong sub parameters \ngate close")

    if customer_id == '':
        exit("wrong sub parameters \ngate close")

    instance_list = Ec2().list_nodes_with_customer_id(customer_id)

    if len(instance_list) < 1:
        exit("No instance\nec2 out")

    for nodes in instance_list["Reservations"]:
        for instance in nodes["Instances"]:
            print(instance['InstanceId'])

else:
    exit("please enter a correct available method & parameters! \ngate close.")
