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
        json.dump(all_data,out1,indent=4)
        with open(os.path.join(dirpath,'sorted_data.json'),'w') as out2:
            json.dump(sorted(all_data,key=lambda n: n['name']),out2,indent=4)



jsoncombiner()