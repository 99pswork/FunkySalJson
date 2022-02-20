import json

for i in range(3,2501):
    with open(str(i) + '.json') as infile:
        data = json.load(infile)
        data['image'] = data['image'].replace('NewUriToReplace', 'QmUqDZHWNXWFAYSiuAF6UbLxxiZKMwg2cdyg54heox4BPG')
        
    with open(str(i) + '.json', 'w') as outfile:
        json.dump(data, outfile)
