import React  from 'react';
import { useParams} from 'react-router-dom';

const Video = () => {
  const {id} = useParams();
  return (
    <div>
      <video width="640" height="360" controls>
        <source src={`http://localhost:8000/getfile/${id}/`} type="video/mp4" />
        Your browser does not support the video tag.
      </video>
    </div>
  );
};

export default Video;
