// src/App.tsx
import { Routes, Route } from 'react-router-dom';
import LoginPage from './routes/LoginPage';
import ProjectList from './routes/ProjectList';
import ProjectDetail from './routes/ProjectDetail';
import HistoryPage from './routes/HistoryPage';

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<LoginPage />} />
      <Route path="/projects" element={<ProjectList />} />
      <Route path="/projects/:id" element={<ProjectDetail />} />
      <Route path="/history" element={<HistoryPage />} />
    </Routes>
  );
};

export default App;
