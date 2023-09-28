#!/bin/bash
# Display only the status code of a response
curl -so /dev/null -w "%{http_code}" "$1"
