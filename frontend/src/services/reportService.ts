import axios from 'axios';

const API = import.meta.env.VITE_API_URL ?? 'http://localhost:9001';

export async function getReports(token: string) {
  const resp = await axios.get(`${API}/reports/`, {
    headers: { Authorization: `Bearer ${token}` }
  });
  return resp.data;
}
