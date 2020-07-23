#!/usr/bin/python3
#
# Matheus Monteiro
# matheus9.8@hotmail.com
#
import sys 
import os
import re
import json
import dateutil.parser as dp

port_running="9999"

pregex = re.compile(r'([0-9]{4}-.*),(\d+),(.*\d.\d+),"\(a\=(\d+),b=(\w+)-(\w+)::(\w+);c=(\w+)\)')
d = {}

# get ip gateway 
ip_gw=os.popen("""hostname -I | awk '{print$1}'| awk -F\. \
                '{print$1"."$2"."$3".1"}'""").read().rstrip('\n')


for line in os.popen(f"nc {ip_gw} {port_running}"):
    try:
        row = pregex.findall(line)
        timestamp = dp.parse(row[0][0]).strftime('%s')
        d['timestamp'] = timestamp
        d['index'] = row[0][1]
        d['signalwave'] = row[0][2] 
        d['metadata'] = {'a':row[0][3], 'b':[row[0][4], row[0][5], row[0][6]]}
        d['c'] = row[0][7]

        print(json.dumps(d))

        try:
            with open("./data.json", "r+") as jsonfile:
                listdic = json.load(jsonfile)
                listdic.append(d)
                jsonfile.seek(0)
                json.dump(listdic, jsonfile, indent=2)

        except FileNotFoundError:
            with open("./data.json", "w+") as jsonfile:
                listdic = []
                listdic.append(d)
                json.dump(listdic, jsonfile, indent=2)
    
    except KeyboardInterrupt:
        break

print("Bye")
sys.exit()
