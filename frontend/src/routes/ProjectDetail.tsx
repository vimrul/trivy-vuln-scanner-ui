import React from 'react';
import { useParams } from 'react-router-dom';

const ProjectDetail = () => {
  const { id } = useParams();
  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold">Project Detail: {id}</h1>
      {/* TODO: fetch images & reports for this project */}
    </div>
  );
};

export default ProjectDetail;
