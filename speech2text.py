from google.cloud import speech
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "auth.json"


def speech_to_text() -> str:
    
    # Read the local audio file
    with open("recording1.wav", "rb") as audio_file:
        content = audio_file.read()

    config = speech.RecognitionConfig(
        language_code="en",
    )
    audio = speech.RecognitionAudio(
        content=content
    )

    client = speech.SpeechClient()

    # Synchronous speech recognition request
    response = client.recognize(config=config, audio=audio)

    print_response(response)

    return response.results[0].alternatives[0].transcript


def print_response(response: speech.RecognizeResponse):
    for result in response.results:
        print_result(result)


def print_result(result: speech.SpeechRecognitionResult):
    best_alternative = result.alternatives[0]
    print("-" * 80)
    print(f"language_code: {result.language_code}")
    print(f"transcript:    {best_alternative.transcript}")
    print(f"confidence:    {best_alternative.confidence:.0%}")