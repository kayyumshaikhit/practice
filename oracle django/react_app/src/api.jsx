import axios from 'axios';

const API_URL = 'http://15.206.79.25:8000';

export default axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});
