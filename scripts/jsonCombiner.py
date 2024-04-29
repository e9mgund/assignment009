import json
import os


def jsoncombiner():
    dirpath = '/home/kilo/repo/assignment_repos/assignment009/test_data'
    all_data = []
    for pathh,j,files in os.walk(dirpath):
        for file in files:
            with open(os.path.join(pathh,file),'r') as inp:
                all_data.extend(json.load(inp))
    with open(os.path.join(dirpath,'combined_json.json'),'a') as out1:
        for i in all_data:
            json.dump(i,out1)
        with open(os.path.join(dirpath,'sorted_data.json'),'w') as out2:
            json.dump(sorted(all_data,key=lambda n: n['name']))



jsoncombiner()