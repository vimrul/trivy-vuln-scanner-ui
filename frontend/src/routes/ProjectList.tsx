// src/routes/ProjectList.tsx
import React, { useEffect, useState, useContext } from 'react';
import { fetchProjects } from '../services/projectService';
import { AuthContext } from '../context/AuthContext';

interface Project {
  id: number;
  name: string;
  description: string;
}

const ProjectList: React.FC = () => {
  const { token } = useContext(AuthContext);
  const [projects, setProjects] = useState<Project[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const getProjects = async () => {
      try {
        const data = await fetchProjects(token);
        setProjects(data);
      } catch (error) {
        console.error('Failed to fetch projects:', error);
      } finally {
        setLoading(false);
      }
    };

    getProjects();
  }, [token]);

  if (loading) return <div>Loading projects...</div>;

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Project List</h1>
      <ul className="space-y-4">
        {projects.map((project) => (
          <li key={project.id} className="border p-4 rounded shadow">
            <h2 className="text-xl font-semibold">{project.name}</h2>
            <p className="text-gray-600">{project.description}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ProjectList;
