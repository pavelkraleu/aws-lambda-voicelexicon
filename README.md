
# Voice Lexicon API

## Create S3 Bucket

This bucket needs to be publicly accessible

## Deploy the package

## Create State Machine

## Update Lambda function




```
{
  "Comment": "GenSound pipeline",
  "StartAt": "GenSound",
  "States": {
    "GenSound": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:762010787478:function:GenSound",
      "End": true
    }
  }
}
```