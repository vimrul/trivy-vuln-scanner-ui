import React, { useEffect, useState } from 'react';
import { useAuth } from '../context/AuthContext';
import { getProjects } from '../services/projectService';
import ProjectCard from '../components/ProjectCard';

const ProjectList = () => {
  const { token } = useAuth();
  const [projects, setProjects] = useState<any[]>([]);

  useEffect(() => {
    if (!token) return;
    getProjects(token)
      .then(setProjects)
      .catch(console.error);
  }, [token]);

  return (
    <div className="p-8 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {projects.map(p => (
        <ProjectCard key={p.id} project={p} />
      ))}
    </div>
  );
};

export default ProjectList;
