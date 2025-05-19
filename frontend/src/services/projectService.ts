import axios from 'axios';

const API_URL = 'http://localhost:9001';

export const getProjects = async (token: string) => {
  const response = await axios.get(`${API_URL}/projects/`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return response.data;
};