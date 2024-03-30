import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState(null);
  const [error, setError] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async () => {
    if (!file) {
      setError("Please select an audio file.");
      return;
    }
  
    const formData = new FormData();
    formData.append('upload_file', file);
  
    setLoading(true);
    setError(null);
  
    try {
      const response = await axios.post(
        'https://dialogdive-video-talk-transcriber-x4jnugzgma-uc.a.run.app/analyze/',
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data',
            'accept': 'application/json'
          }
        }
      );
  
      setResults(response.data.result);
    } catch (error) {
      setError("An error occurred. Please try again later");
    }
  
    setLoading(false);
  };  

  return (
    <div className="App">
      <h1>Audio Sentiment Analysis</h1>
      <input type="file" accept="*/mpeg, */wav, */mp4" onChange={handleFileChange} />
      <button onClick={handleSubmit}>Analyze</button>

      {loading && <p>Loading...</p>}
      {error && <p>Error: {error}</p>}

      {results && (
        <div className="results-box">
          <h2>Analysis Results:</h2>
          {results.split('\n').map((line, index) => (
            <p key={index}>{line}</p>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;
