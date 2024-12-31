#!/bin/sh

# Unit test of container
cd csv-reader-service
python -m unittest tests/test_csv_reader.py

echo "Test1 succeeded"
