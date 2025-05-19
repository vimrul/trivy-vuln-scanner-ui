import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import LoginPage from './routes/LoginPage';
import ProjectList from './routes/ProjectList';
import ProjectDetail from './routes/ProjectDetail';
import HistoryPage from './routes/HistoryPage';
import { useAuth } from './context/AuthContext';

function App() {
  const { token } = useAuth();

  return (
    <Router>
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        {token ? (
          <>
            <Route path="/" element={<Navigate to="/projects" />} />
            <Route path="/projects" element={<ProjectList />} />
            <Route path="/projects/:id" element={<ProjectDetail />} />
            <Route path="/projects/:id/history" element={<HistoryPage />} />
          </>
        ) : (
          <>
            <Route path="*" element={<Navigate to="/login" />} />
          </>
        )}
      </Routes>
    </Router>
  );
}

export default App;
