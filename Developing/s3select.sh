#!/bin/bash


aws s3api select-object-content --bucket s3game-level6-vjv45x1gux81 --key s3select.csv.gz --expression "SELECT s3object.Answer FROM s3object WHERE Category = 'TREASURE'" --expression-type SQL --input-serialization '{"CSV": {"FileHeaderInfo": "USE", "FieldDelimiter": ";"}, "CompressionType": "GZIP"}' --output-serialization '{"CSV": {}}' /tmp/secret
