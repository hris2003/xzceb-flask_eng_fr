''' Module to translate text between french and english'''

import os
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version="2022-10-15",
    authenticator=authenticator
)

language_translator.set_service_url(url)

language_translator.set_disable_ssl_verification(True)

def english_to_french(english_text):
    """Return the french translation of the english_text"""
    try:
        translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
        return translation["translations"][0]["translation"]
    except ApiException as ex:
        print("english_to_french fails with status code " + str(ex.code) + ": " + ex.message)
        return None

def french_to_english(french_text):
    """Return the english translation of the french_text"""
    try:
        translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
        return translation["translations"][0]["translation"]
    except ApiException as ex:
        print("french_to_english fails with status code " + str(ex.code) + ": " + ex.message)
        return None
