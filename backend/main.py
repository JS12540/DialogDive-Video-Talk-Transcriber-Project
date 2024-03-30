from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
    FileSource,
)
import openai

app = FastAPI()

origins = [
        "*",
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def get_sentiment_analysis(transcription):
    """
    An asynchronous function that takes a transcription as input and sends a request to the OpenAI API for sentiment and psychological insights derived from the conversation. It then returns the response containing the sentiment or psychological insights. 
    """
    openai.api_key = 'YOUR OPENAI API KEY'

    prompt = f'''Give me Sentiment or psychological insights derived from the conversation, some insights about speakers. Strictly don’t provide summary of conversation, key words, etc. Output should be related to sentimental analysis. 
    For example: 
    Line 1: ‘Speaker_2 likes a sport. It seems he cares about his health’.\n
    Line 2:  ‘Speaker_1 pretends to be smart’. etc

    Make sure to make important points bold, also explain sentiment and pyschological ingights. Output should strictly not be more than 200 tokens. 

    \nConversation: {transcription}.
     
    \n Sentiments or Pyschological insights: '''

    print("Sending request to OpenAI API...")
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=250,
    )

    print("Received response from OpenAI API")

    return response.choices[0].text.strip()

async def transcribe_audio(file: UploadFile):
    """
    Asynchronously transcribes an audio file using the Deepgram API.

    Args:
        file (UploadFile): The audio file to be transcribed.

    Returns:
        str: The transcribed text from the audio file.

    Raises:
        HTTPException: If the Deepgram API returns a 503 status code.
        HTTPException: If an exception occurs during the transcription process.

    """
    try:
        print(f"Received file: {file.filename}")

        # Perform transcription using Deepgram
        deepgram: DeepgramClient = DeepgramClient("YOUR DEEPGRAM API KEY")

        buffer_data = file.file.read()
        print(f"Read {len(buffer_data)} bytes from file")

        payload: FileSource = {
            "buffer": buffer_data,
        }

        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
            utterances=True,
            punctuate=True
        )

        print("Sending request to Deepgram API...")
        response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)
        print("Received response from Deepgram API")


        return response['results']['channels'][0]['alternatives'][0]['transcript']

    except HTTPException as http_err:
        if http_err.status_code == 503:
            raise HTTPException(status_code=503, detail="Service Unavailable. Please try again later.")
    except Exception as e:
        print(f"Exception occured : {e}")
        raise HTTPException(status_code=500, detail=e)

@app.post("/analyze/")
async def analyze(upload_file: UploadFile = File(...)):
    """
    Analyzes an uploaded audio file by performing transcription and sentiment analysis.

    Parameters:
        upload_file (UploadFile): The audio file to be analyzed. Only audio files with extensions .wav, .mp3, .mp4, .ogg, .flac are allowed.

    Returns:
        dict: A dictionary containing the sentiment analysis result.

    Raises:
        HTTPException: If the uploaded file has an unsupported extension or if an error occurs during the analysis process.
    """
    try:
        # Check if the uploaded file has an allowed audio extension
        allowed_extensions = {'.wav', '.mp4', '.mp3', '.ogg', '.flac'}  # Add more extensions if needed
        ext = os.path.splitext(upload_file.filename)[1]
        if ext.lower() not in allowed_extensions:
            raise HTTPException(status_code=400, detail="Only audio files with extensions .wav, .mp3, .mp4 ,.ogg, .flac are allowed.")

        # Perform transcription of the audio file
        transcription = await transcribe_audio(upload_file)

        sentiment = await get_sentiment_analysis(transcription)

        return {"result": sentiment}

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Something went wrong. Please try again later.")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
