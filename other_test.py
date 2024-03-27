import json
from typing import Dict, List, TypedDict
import pprint

class MyDict(TypedDict):
    Name: str
    Amount: int
    Speed: bool


# with open('utilities/uno.json') as f:
#     data = json.load(f)

my_dict: List[MyDict] = [
{
    "Name": "1-9",
    "Amount": 3,
    "Speed": False
},
{
    "Name": "0",
    "Amount": 1,
    "Speed": False
},
{
    "Name": "1-9",
    "Amount": 1,
    "Speed": True
}
]

final_list = []
# my_dict = data['4_Color_Uno']
for x in my_dict:
    if x['Name'] == '1-9':
        for index in range(0, 9):
            for color in ['Red', 'Blue', 'Green', 'Yellow']:
                for _ in range(0, x['Amount']):
                    var = {
                        "Name": '1-9',
                        "Number": index + 1,
                        "Color": color,
                        "Speed": x['Speed']
                    }
                    final_list.append(var)
    elif x['Name'] == '0':
        for color in ['Red', 'Blue', 'Green', 'Yellow']:
            for _ in range(0, x['Amount']):
                var = {
                    "Name": '0',
                    "Number": '0',
                    "Color": color,
                    "Speed": x['Speed']
                }
                final_list.append(var)
    else:
        print(f'----------------------------------------------------------------')
        print(f'{x=}')
        print('----------------------------------------------------------------')

pprint.pprint(final_list)
pprint.pprint(len(final_list))
with open('utilities/uno_data_test.json', 'w') as f:
    json.dump(final_list, f, indent=4)