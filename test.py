import json_lines
X= []; y= []; z= [];
with open ('reviews.json', 'rb') as f:
    for item in json_lines.reader(f):
        X.append(item['text'])
        y.append(item['voted up'])
        z.append(item['early_access'])