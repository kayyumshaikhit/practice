import React, {useState} from 'react';
import axios from 'axios';
import {useNavigate} from 'react-router-dom';

const Upload = ()=>{
const [file,setFile] = useState("");
const handleChange = (e)=>setFile(e.target.files[0]);
const navigate = useNavigate();

const handleSubmit = async(e)=>{
e.preventDefault();
const formData = new FormData();
formData.append('file',file);
await axios.post(`http://localhost:8000/`,formData,{headers:{'Content-Type':'multipart/form-data'}})
.then(response=>alert("done"))
.catch(error=>console.error(error))
navigate("/");
}

return (
<>
<form method="POST" onSubmit={handleSubmit}>
<input type="file"
name='file'
onChange={handleChange}
/>
<button type="submit">Upload</button>
</form>
</>
)
}

export default Upload;