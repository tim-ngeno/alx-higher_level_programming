#!/bin/bash
# Display size in bytes of the content from a URL response
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
