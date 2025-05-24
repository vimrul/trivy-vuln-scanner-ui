// src/routes/ProjectDetail.tsx
import React from 'react';
import { useParams } from 'react-router-dom';

export default function ProjectDetail() {
  let { id } = useParams<{ id: string }>();
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold">Project #{id}</h1>
      {/* fetch & show images, vulnerability charts, etc. */}
    </div>
  );
}
