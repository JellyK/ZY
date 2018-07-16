import json

def transform(inpath, outpath):
    new_jArray = []
    for path in inpath:
        with open(path, 'r') as fp:
            jArray = json.loads(fp.read())
            length = len(new_jArray) + 1
            for i, j in enumerate(jArray):
                new_j = dict()
                j['chargeId'] = j['id']
                del j['id']
                new_j['fields'] = j
                new_j['model'] = "charge.ECharge"
                new_j['pk'] = i + length
                new_jArray.append(new_j)
    with open(outpath, 'w') as fp:
        fp.write(json.dumps(new_jArray))

if __name__ == '__main__':
    transform(['echargenet.txt', 'echargenet_third.txt'], 'echargenet.json')