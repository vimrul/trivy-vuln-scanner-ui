import { Routes, Route, Navigate } from 'react-router-dom';
import LoginPage from './routes/LoginPage';
import ProjectList from './routes/ProjectList';
import ProjectDetail from './routes/ProjectDetail';
import HistoryPage from './routes/HistoryPage';
import { useAuth } from './context/AuthContext';

const App = () => {
  const { token } = useAuth();

  return (
    <Routes>
      <Route path="/" element={<LoginPage />} />
      {/* require login for all dashboards */}
      <Route
        path="/projects"
        element={ token ? <ProjectList /> : <Navigate to="/" /> }
      />
      <Route
        path="/projects/:id"
        element={ token ? <ProjectDetail /> : <Navigate to="/" /> }
      />
      <Route
        path="/history"
        element={ token ? <HistoryPage /> : <Navigate to="/" /> }
      />
    </Routes>
  );
};

export default App;
