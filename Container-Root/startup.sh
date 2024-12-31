#!/bin/sh

# Container startup script
cd csv-reader-service
python app/main.py

echo "Container-Root/startup.sh executed"