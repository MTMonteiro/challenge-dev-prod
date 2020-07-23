#!/bin/bash
#
# Matheus Monteiro
# matheus9.8@hotmail.com
#

user_db="root"
passwd_db="root!p4sswd" 
datab="data_collect"

# import json file 
docker exec  -ti mongo-container mongoimport -u$user_db -p$passwd_db \
--authenticationDatabase admin --db $datab --collection data \
--type json --file /usr/src/code/data.json --jsonArray

# Check insertion
[ "$?" -eq "0" ] && echo "Data successfully inserted !!!" || echo "Failure during insertion"

# clean json file 
echo "[]" > ./data.json
