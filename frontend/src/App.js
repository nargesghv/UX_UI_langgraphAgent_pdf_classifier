import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [file, setFile] = useState(null);
  const [classification, setClassification] = useState(null);
  const [error, setError] = useState(null);

  const handleUpload = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    try {
      const res = await axios.post('http://localhost:8000/upload', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      setClassification(res.data.classification);
      setError(null);
    } catch (err) {
      setError('Failed to classify document');
      setClassification(null);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center p-4">
      <h1 className="text-2xl font-bold mb-4">LangGraph Document Classifier</h1>
      <input type="file" accept=".pdf,.docx" onChange={(e) => setFile(e.target.files[0])} />
      <button
        onClick={handleUpload}
        className="mt-4 px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
      >
        Upload & Classify
      </button>
      {classification && (
        <p className="mt-4 text-green-600 font-semibold">Classification: {classification}</p>
      )}
      {error && (
        <p className="mt-4 text-red-500 font-semibold">{error}</p>
      )}
    </div>
  );
}

export default App;
