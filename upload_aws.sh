#!/bin/bash

rm ./*/*.zip

cd HandleForm

zip -r ./HandleForm.zip ./

aws lambda update-function-code --function-name HandleForm --zip-file fileb://./HandleForm.zip  --region us-east-1

cd ..

cd GenSound

zip -r ./GenSound.zip ./

aws lambda update-function-code --function-name GenSound --zip-file fileb://./GenSound.zip  --region us-east-1

