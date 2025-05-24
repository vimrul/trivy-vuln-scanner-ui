import React from 'react'
import { Routes, Route, Navigate } from 'react-router-dom'
import { useAuth } from './context/AuthContext'
import LoginPage from './routes/LoginPage'
import ProjectList from './routes/ProjectList'
import ProjectDetail from './routes/ProjectDetail'
import HistoryPage from './routes/HistoryPage'

const App: React.FC = () => {
  const { token } = useAuth()

  return (
    <Routes>
      {/* if already logged in, redirect “/” → “/projects” */}
      <Route
        path="/"
        element={token ? <Navigate to="/projects" /> : <LoginPage />}
      />

      {/* protected routes */}
      <Route
        path="/projects"
        element={token ? <ProjectList /> : <Navigate to="/" />}
      />
      <Route
        path="/projects/:id"
        element={token ? <ProjectDetail /> : <Navigate to="/" />}
      />
      <Route
        path="/history"
        element={token ? <HistoryPage /> : <Navigate to="/" />}
      />
    </Routes>
  )
}

export default App
