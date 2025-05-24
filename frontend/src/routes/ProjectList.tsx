// src/routes/ProjectList.tsx
import React, { useEffect, useState } from 'react';
import { useAuth } from '../context/AuthContext';
import { getProjects } from '../services/projectService';

interface Project { id: number; name: string; description: string; }

export default function ProjectList() {
  const { token } = useAuth();
  const [projects, setProjects] = useState<Project[]>([]);

  useEffect(() => {
    if (!token) return;
    getProjects(token).then(setProjects).catch(console.error);
  }, [token]);

  if (!token) return <p>Please log in.</p>;

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Your Projects</h1>
      {projects.map((p) => (
        <div key={p.id} className="border p-4 rounded mb-2">
          <a href={`/projects/${p.id}`} className="text-blue-600">{p.name}</a>
          <p>{p.description}</p>
        </div>
      ))}
    </div>
  );
}
