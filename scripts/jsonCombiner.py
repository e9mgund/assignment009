import json
import os


def jsoncombiner():
    for i,j,k in os.walk('/home/kilo/repo/assignment_repos/assignment009/test_data'):
        for f in k:
            with open(os.path.join(i+f),'r') as file:
                print(type())



jsoncombiner()