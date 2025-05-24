import React from 'react';
import { useNavigate } from 'react-router-dom';

interface Props { project: any; }

const ProjectCard = ({ project }: Props) => {
  const nav = useNavigate();
  return (
    <div
      onClick={() => nav(`/projects/${project.id}`)}
      className="cursor-pointer border rounded p-4 shadow hover:shadow-md"
    >
      <h2 className="text-xl font-semibold">{project.name}</h2>
      <p className="text-gray-600">{project.description}</p>
    </div>
  );
};

export default ProjectCard;
