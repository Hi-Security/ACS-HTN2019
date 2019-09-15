
import speech_recognition as sr
import time
import json

import datetime

storage = []

def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached orgit
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=3)

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response


def record_words_recognized():
    start = time.time()
    print(sr.Microphone.list_microphone_names())

    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = True

    while time.time()-start < 60:
        microphone = sr.Microphone(device_index=6)
        guess = recognize_speech_from_mic(recognizer, microphone)
        if guess["error"]:
            print("ERROR: {}".format(guess["error"]))
            break
        else:
            print("You said: {}".format(guess["transcription"]))
            storage.append(guess["transcription"])
            data = {"lines": storage}
            with open('./website/src/data.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

    print(storage)



if __name__ == "__main__":
    record_words_recognized()
