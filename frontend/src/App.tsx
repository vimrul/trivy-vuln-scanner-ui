// src/App.tsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import LoginPage from './routes/LoginPage';
import ProjectList from './routes/ProjectList';
import ProjectDetail from './routes/ProjectDetail';
import HistoryPage from './routes/HistoryPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Navigate to="/login" />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/projects" element={<ProjectList />} />
        <Route path="/projects/:id" element={<ProjectDetail />} />
        <Route path="/projects/:id/history" element={<HistoryPage />} />
      </Routes>
    </Router>
  );
}

export default App;
