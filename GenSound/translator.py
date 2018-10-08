import wave

import boto3
from pydub import AudioSegment

class Translator():

    polly_client = boto3.client('polly')


    def translate_word(self, word, language_code, voice_id, speed=100):
        response = self.polly_client.synthesize_speech(VoiceId=voice_id,
                                                       TextType="ssml",
                                                  OutputFormat='mp3',
                                                  Text="<prosody rate='{1}%' volume='+15dB'>{0}</prosody>".format(word, speed),
                                                  LanguageCode=language_code)

        return response['AudioStream'].read()

    def save_response_mp3(self, response_mp3, file_path):

        file = open(file_path, 'wb')
        file.write(response_mp3)
        file.close()

    def save_response_pcm_to_wav(self, response_pcm, file_path):

        with wave.open(file_path, 'wb') as wavfile:
            wavfile.setparams((1, 2, 16000, 0, 'NONE', 'NONE'))
            wavfile.writeframes(response_pcm)

    def join_words(self, word_a, word_b, export_path, gap=1300):

        word_a_sound = AudioSegment.from_mp3(word_a)
        word_b_sound = AudioSegment.from_mp3(word_b)

        end_sound = AudioSegment.from_mp3("sound.mp3")

        sound = word_a_sound + AudioSegment.silent(duration=gap) + word_b_sound + AudioSegment.silent(duration=gap) + end_sound

        sound.export(export_path, format="mp3", parameters=["-ac", "2", "-vol", "300"])

    def join_multiple_sounds(self, sounds, export_path, gap=1000):

        all_sounds = AudioSegment.silent(duration=1)

        for sound in sounds:

            all_sounds += AudioSegment.from_mp3(sound)
            all_sounds += AudioSegment.silent(duration=gap)

        # all_sounds

        all_sounds.export(export_path, format="mp3", parameters=["-ac", "2", "-vol", "300"])





