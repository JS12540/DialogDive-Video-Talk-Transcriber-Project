## DialogDive-Video-Talk-Transcriber Architecture

**DialogDive-Video-Talk-Transcriber** is an project that revolutionizes the way we understand conversations by offering sentiment analysis on audio and video files. With speaker-wise breakdowns, it provides valuable insights into the emotional tone of each participant, enabling users to gain deeper understanding and actionable insights from their interactions.

### Frontend
The frontend of the DialogDive-Video-Talk-Transcriber project is built using ReactJS. ReactJS provides a powerful framework for building user interfaces with reusable components. In addition to ReactJS, basic styling is applied using CSS to enhance the visual presentation of the application.

### Backend
The backend of the project involves several components:

1. **OpenAI API for Sentiment Analysis**: This component utilizes the OpenAI API key to perform sentiment analysis on the transcribed text. The sentiment analysis helps in determining the emotional tone of the conversation.

2. **Deepgram API for Speech-to-Text Conversion**: The Deepgram API is employed to convert speech from video talks into text. Deepgram offers accurate and efficient speech recognition capabilities, enabling the system to transcribe spoken words into textual format.

3. **FastAPI for Backend**: FastAPI is used to develop the backend of the application. FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+. It provides features such as automatic validation, serialization, interactive API documentation, and more.

### Interaction Flow
1. **User Interaction**: Users interact with the frontend interface, which provides options to upload audio/video talks for transcription.

2. **Speech-to-Text Conversion**: Upon receiving the input, the frontend sends a request to the backend, which utilizes the Deepgram API to convert speech from the video into text.

3. **Text Analysis**: The transcribed text is then forwarded to the OpenAI API for sentiment analysis. The sentiment analysis process determines the sentiment or emotional tone expressed in the conversation.

4. **Results Display**: The results of sentiment analysis, along with the transcribed text, are presented back to the user through the frontend interface.

### Technologies Used
- **Frontend**: ReactJS, CSS
- **Backend**: FastAPI, OpenAI API, Deepgram API
- **Other Dependencies**: Axios for making HTTP requests, Docker for building container etc.

### Scalability and Future Improvements
- **Scalability**: The architecture is designed to handle a scalable number of concurrent users by leveraging asynchronous processing and efficient API calls.

### Security Considerations
- **API Key Management**: Proper measures should be taken to securely manage and store API keys to prevent unauthorized access and potential misuse.

### Deployment
- **Hosting**: The frontend and backend are deployed using Google Cloud Run, leveraging Docker containers for easy deployment and scalability.

### Challenges Faced
1. **Frontend Development**: Limited experience in frontend development posed a challenge during the project.
2. **Deployment to Google Cloud Run**: Deploying the frontend and backend to Google Cloud Run was a major challenge due to limited prior experience with the platform. Despite utilizing online resources, it took approximately 2 days to successfully deploy everything and ensure proper functionality.
3. **Friend Assistance**: Aakash provided valuable assistance in building Docker containers, helping to resolve errors encountered during the process

## Loom Video

[Loom Video Link](https://www.loom.com/share/c8f37be81f484a938dfbc297c684d238?sid=1fe4d0f3-530a-4fbc-938c-7c113b2f580a)


