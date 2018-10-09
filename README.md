
# Voice Lexicon API

## Create S3 Bucket

## Deploy the package

## Add Permission for Polly API

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