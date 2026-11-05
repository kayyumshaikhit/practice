import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Upload = () => {
  const [file, setFile] = useState(null); // Initialize as null for safety
  const handleChange = (e) => setFile(e.target.files[0]);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) {
      alert("Please select a file first!");
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      // 1. Await the response fully
      const response = await axios.post(`http://localhost:8000/`, formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });
      
      alert("Upload successful!");
      navigate("/"); // 2. ONLY navigate back once the upload is completed!
    } catch (error) {
      console.error("Upload execution dropped:", error);
      if (error.response) {
        alert("Server validation failure: " + JSON.stringify(error.response.data));
      } else {
        alert("Network communication connection broke.");
      }
    }
  }

  return (
    <>
      <form method="POST" onSubmit={handleSubmit}>
        <input type="file" name='file' onChange={handleChange} />
        <button type="submit">Upload</button>
      </form>
    </>
  );
}

export default Upload;
