import axios from 'axios';

const API_URL = 'http://35.154.235.107:8000';

export default axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});