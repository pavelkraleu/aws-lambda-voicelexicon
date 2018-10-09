import tempfile
import boto3
from translator import Translator
import os

bucket = os.environ['BucketName']


def upload_file(file_path, file_id):

    s3 = boto3.client('s3')

    s3.upload_file(file_path, bucket, file_id + ".mp3")



def lambda_handler(event, context):

    print(event)

    words, file_id, name, lang_code_a, lang_voice_a, lang_code_b, lang_voice_b = event

    trans = Translator()

    all_files = []

    with tempfile.TemporaryDirectory() as temp_dir:

        temp_dir += "/"

        for i, word in enumerate(words):

            print(temp_dir)

            dog_us = trans.translate_word(word[0], lang_code_a, lang_voice_a)
            trans.save_response_mp3(dog_us, temp_dir+"/word_a.mp3")

            dog_de = trans.translate_word(word[1], lang_code_b, lang_voice_b, speed=80)
            trans.save_response_mp3(dog_de, temp_dir+"word_b.mp3")

            trans.join_words(temp_dir+"/word_a.mp3", temp_dir+"/word_b.mp3", temp_dir+"join_{}.mp3".format(i), gap=500)

            all_files.append(temp_dir+"join_{}.mp3".format(i))

        trans.join_multiple_sounds(all_files, temp_dir+"all.mp3", gap=500)

        upload_file(temp_dir+"all.mp3", file_id)

    return {
        "statusCode": 200,
        "body": "Done"
    }
