#!/bin/bash

COMMAND=${1?Error: no command given}

cd scripts

if [[ $COMMAND = "newdb" ]]
    then 
        sh newdb.sh
elif [[ $COMMAND = "init" ]]
    then 
        sh init.sh
elif [[ $COMMAND = "start" ]]
    then 
        sh start.sh
elif [[ $COMMAND = "stop" ]]
    then 
        sh stop.sh
elif [[ $COMMAND = "commands" ]]
    then 
        sh commands.sh
else
    sh commands.sh
fi
