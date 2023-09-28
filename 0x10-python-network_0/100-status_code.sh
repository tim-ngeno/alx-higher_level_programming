#!/bin/bash
# Display only the status code of a response
curl -sI "$1" | grep 'HTTP' | awk '{print $2}'
