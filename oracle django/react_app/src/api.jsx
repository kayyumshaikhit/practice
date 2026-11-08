import axios from 'axios';

const API_URL = 'http://13.207.176.253:8000';

export default axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});
