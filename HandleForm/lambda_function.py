import csv
import json
from urllib.parse import urlparse, parse_qs
import boto3


bucket = "dictionary-mp3"

def file_exists(key):

    s3 = boto3.client('s3')

    try:
        s3.head_object(Bucket=bucket, Key=key)
        return True
    except Exception:
        return False

def get_new_id():
    with open('file_ids.csv', newline='') as csvfile:
        filereader = csv.DictReader(csvfile, delimiter=',')

        for row in filereader:
            if not file_exists(row["id"] + ".mp3"):
                return row["id"], row["name"]

def lambda_handler(event, context):

    url_args = parse_qs(event["body"])

    words_a = url_args["wordsA"][0].strip().split("\r\n")
    words_b = url_args["wordsB"][0].strip().split("\r\n")

    lang_a = url_args["langSelectionA"][0].strip()
    lang_b = url_args["langSelectionB"][0].strip()

    min_words = min([len(words_a), len(words_b)])

    words_a = words_a[0:min_words]
    words_b = words_b[0:min_words]

    words = list(zip(words_a, words_b))

    if lang_a == "english":
        lang_code_a = "en-US"
        lang_voice_a = "Matthew"
    elif lang_a == "spanish":
        lang_code_a = "es-ES"
        lang_voice_a = "Miguel"
    elif lang_a == "german":
        lang_code_a = "de-DE"
        lang_voice_a = "Vicki"
    elif lang_a == "french":
        lang_code_a = "fr-FR"
        lang_voice_a = "Lea"
    else:
        lang_code_a = "en-US"
        lang_voice_a = "Matthew"


    if lang_b == "english":
        lang_code_b = "en-US"
        lang_voice_b = "Matthew"
    elif lang_b == "spanish":
        lang_code_b = "es-ES"
        lang_voice_b = "Miguel"
    elif lang_b == "german":
        lang_code_b = "de-DE"
        lang_voice_b = "Vicki"
    elif lang_a == "french":
        lang_code_b = "fr-FR"
        lang_voice_b = "Lea"
    else:
        lang_code_b = "en-US"
        lang_voice_b = "Matthew"


    file_id, name = get_new_id()

    response = boto3.client('stepfunctions').start_execution(
        stateMachineArn='arn:aws:states:us-east-1:762010787478:stateMachine:SoundGenerator',
        input=json.dumps([words, file_id, name, lang_code_a, lang_voice_a, lang_code_b, lang_voice_b])
    )

    print(response)

    return  {
        "statusCode": 302,
        "headers": {
            "Location": "http://voicelexicon.com/final-page.html?q=" + name.title()+"&id="+file_id
        }
    }
