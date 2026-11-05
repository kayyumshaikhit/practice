import React,{useEffect,useState} from 'react'
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { useParams } from 'react-router-dom';

const DeleteFile = () => {
  const {id} = useParams();
  const navigate = useNavigate();

  const handleSubmit = (e)=>{
    e.preventDefault();
    axios.delete(`http://localhost:8000/drop/${id}/`,{headers:{'Content-Type':'multipart/form-data'}})
    .then(response=>alert("dropped..."))
    .catch(error=>console.error(error))
    navigate("/")
  }

  return (
    <form  method='POST' onSubmit={handleSubmit}>
        <center>Are you wish to Drop the file?</center>
        <button type="submit">Delete</button>
    </form>
  )
}

export default DeleteFile;