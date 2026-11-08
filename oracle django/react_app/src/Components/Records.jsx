import React from 'react'
import axios from 'axios';
import {useState,useEffect} from 'react';
import { Link } from 'react-router-dom';
import api from '../api';

const Records = () => {
    const [data,setData] = useState([]);
    useEffect(()=>{
         api.get(`/getall/`)
        .then(response=>setData(response.data))
        .catch(error=>console.error(error))
    },[])
    
    const getFileName = (e)=>{
        return e.split('/').pop();
    }

  return (
    <table border={1}>
        <thead>
            <tr>
                <th>ID</th>
                <th>FILE NAME</th>
                <th>VIDEO</th>
                <th>Delete</th>
            </tr>
        </thead>
        <tbody>
            {data.map(m=>(
                <tr key={m.id}>
                    <td>{m.id}</td>
                    <td>{getFileName(m.file)}</td>
                    <td>
                        {/* <video width="320" height="240" controls>
                            <source src={`http://localhost:8000/getfile/${m.id}/`} type="video/mp4"/>
                        </video> */}
                        <button>
                            <Link to={`/video/${m.id}/`}>play</Link>
                        </button>
                    </td>
                    <td>
                        <button>
                            <Link to={`/deletefile/${m.id}/`}>Delete</Link>
                        </button>
                    </td>
                </tr>
            ))}
        </tbody>
    </table>
  )
}

export default Records
