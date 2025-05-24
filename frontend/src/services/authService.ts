import axios from 'axios';

const API = import.meta.env.VITE_API_URL ?? 'http://localhost:9001';

export async function login(
  username: string,
  password: string
): Promise<{ access_token: string }> {
  const params = new URLSearchParams();
  params.append('username', username);
  params.append('password', password);

  const resp = await axios.post(
    `${API}/auth/login`,
    params,
    {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    }
  );

  return resp.data;
}
