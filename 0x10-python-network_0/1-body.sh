#!/bin/bash
# Get the body of the URL response
[ "$(curl -s -o /dev/null -w "%{http_code}" "$1")" = "200" ] && curl -s "$1"
