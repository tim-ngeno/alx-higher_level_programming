#!/bin/bash
# Display all HTTP methods accepted by the server
curl -sI -X OPTIONS | grep "Allow" | cut -d" " -f 2-
