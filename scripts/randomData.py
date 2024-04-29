import random
import os
import json


def randomizer():
    alphas, nums = [chr(i) for i in range(97,123)],[i for i in range(0,10)]
    for _ in range(15):
        data = []
        records = random.randrange(1000,39481)
        for i in range(records):
            name = "".join(random.sample(alphas,k=10))
            age = random.randrange(1,101)
            bio = "".join(random.sample(alphas,k=20))
            gender = random.choice(['Male','Female',"Other"])
            data.append({"name":name,"age":age,"bio":bio,"gender":gender})
        with open(os.path.join(os.path.abspath('test_data'),'json'+str(_)+'.json'),'w') as file:
            json.dump(data,file,indent=6)
            file.close()




randomizer()