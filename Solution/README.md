# Convert a CSV stream to JSONL text (solution*)
This is the solution for challenge-dev-prod, where using python and bash the resolution of the proposed challenge was made.

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

Wait until the code compiles and the service shows `Listening at tcp://0.0.0.0:9999`

Then you can test it with:
```bash
$ docker-compose up 
```
user -d parameter case want run in background

## Running

Captures the csv data stream and append it at runtime to a json format file.

```bash
$ docker run -it --rm -v $(pwd):/usr/src/code  python-source
```
*A data.json file will be generated in the current directory.*


Transferring json file to mongodb.
```bash
$ ./insert_db.sh
```
*The data.json file will be cleaned to avoid duplication in the database.*

## Mongo-express web interface


![alt text](https://github.com/intelie/challenge-remote-access/raw/master/example%20network%20infrastructure.png "Example network infrastructure")



Code by _Matheus Monteiro_.