#!/bin/bash

curl -H "Content-Type: application/json" --data '{"bucketName" : "zenon-saavedra", "key" : "documents/CV.pdf"}' https://m12yrxb2uc.execute-api.ap-southeast-1.amazonaws.com/dev/GetPresignedUrl
