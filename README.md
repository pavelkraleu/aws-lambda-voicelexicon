# This service runs behind [voicelexicon.com](https://voicelexicon.com/)

---

# Post installation steps

## 1. Check that you have correct permissions

Make sure that permissions for both lambda functions look like this

![img](https://raw.githubusercontent.com/pavelkraleu/aws-lambda-voicelexicon/master/perm_img.png)

If not, scroll down and add role with following permissions

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "polly:DescribeVoices",
                "polly:GetLexicon",
                "polly:GetSpeechSynthesisTask",
                "polly:ListLexicons",
                "polly:ListSpeechSynthesisTasks",
                "polly:SynthesizeSpeech"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "InvokePermission",
            "Effect": "Allow",
            "Action": [
                "lambda:InvokeFunction"
            ],
            "Resource": "*"
        }
    ]
}
```

## 2. Edit Lambda name

You need to make sure, that backend task which is executed has correct name.

Scroll down in HandleForm lambda function and add auto generated name of GenSound lambda function

![img](https://raw.githubusercontent.com/pavelkraleu/aws-lambda-voicelexicon/master/edit_line.png)

## 3. Make sure that that your S3 bucket is publicly available 

---

# About the project

## Inspiration
Learning new vocabulary is a demanding process and it is even more daunting for those who suffer from learning disability, according to Dyslexia Center Utah 20% of the elementary school population is struggling with reading. One of the way to increase the efficiency of learning is the multi-sensory approach – to use more senses like audio. We know on our own as one of the members is learning the third language with diagnosed dyslexia. That is why we want to improve the accessibility of vocabulary in audio format and make it available on Alexa.

## What it does
Voice Lexicon creates an audio file based on providing vocabulary on the website and enables a user to play this file on any Amazon Alexa with our skill and special two-word phrase. This way, learners can seamlessly share their vocabulary with anyone around the world.

## How we built it
We used Amazon Polly text-to-speech technology to generate a multi-language audio file from your vocabulary and make it available through Voice Lexicon skill and provided phrase on any of the 50 million available Alexa devices.

## Challenges we ran into
One of the challenging things was to design the way to generate phrases that will be used for playing vocabulary. What helped us is bitcoin Wordlists of English phrases that are used as a backup of private keys. Those words are pre-sorted for such use case.

## Accomplishments that we're proud of
Being able to combine web with Alexa in a meaningful way.

## What's next for Voice Lexicon API
We can significantly improve remembrance of the phrases by structuring them with and avoiding abstract words that are harder to remember - but or know we do not know if this is a problem. Also, we would like to create our vocabulary for people who start with learning and do not have their word list yet. The biggest improvement would be creating a testing function, but there are several challenges like changing the language of input or getting the raw audio file.


Made with ❤️ by Pavel Kral. Available on the [AWS Serverless Application Repository](https://aws.amazon.com/serverless)

## License

GNU General Public License v1.0 only (GPL-1.0)