# Convert a CSV stream to JSONL text (solution*)
This is the solution for challenge-dev-prod, which was developed in python and bash.


## Requirements
 - Linux: Ubuntu 18+ recommended (can be a virtual machine).
 - Docker + compose: [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/), [Install Docker Compose](https://docs.docker.com/compose/install/)

*execute all commands in 'Solutions' directory*

## Setup
Compile stream-source image:
```bash
$ docker build --tag stream-source ../stream-source/.
```

To compile image docker:
```bash
$ docker build -t python-source .
```

Start the containers:
```bash
$ docker-compose up 
```
_use -d parameter in case you want to run in background_.

Wait until the code compiles and the service shows `Listening at tcp://0.0.0.0:9999`

Then you can test it with:
```bash
$ nc localhost 9999
```

## Running

Captures the csv data stream and appends it at runtime to a json format file.

```bash
$ docker run -it --rm -v $(pwd):/usr/src/code  python-source
```
_to stop use ctrl + c_.
*A data.json file will be generated in the current directory.*


Transferring json file to mongodb.

```bash
$ ./insert_db.sh
```
*The data.json file will be cleaned up in order to avoid duplication in the database.*

## Mongo-express web interface

To access an interface, simply access the address:
http://localhost/8081/ .
*The collected data will be in the collect_Data table*
![alt text](https://github.com/MTMonteiro/challenge-dev-prod/blob/main/Solution/mongo-express.png "Mongo-express")



Code by _Matheus Monteiro_.
