import React  from 'react';
import { useParams} from 'react-router-dom';
import api from '../api';

const Video = () => {
  const {id} = useParams();
  const API_BASE_URL = import.meta.env.VITE_API_URL
  return (
    <div>
      <video width="640" height="360" controls>
        <source src={`${API_BASE_URL}/getfile/${id}/`} type="video/mp4" />
        Your browser does not support the video tag.
      </video>
    </div>
  );
};

export default Video;
