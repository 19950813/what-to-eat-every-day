import json
import random

with open('test.json', 'r') as  f:
    print('今日随机菜单为 {s}'.format(s = random.choice(json.load(f))))