// frontend/src/context/AuthContext.tsx
import React, { createContext, useContext, useState, useEffect } from 'react'

interface AuthContextType {
  token: string | null
  setToken: (t: string) => void
}

const AuthContext = createContext<AuthContextType>({
  token: null,
  setToken: () => {}
})

export const AuthProvider: React.FC<{children: React.ReactNode}> = ({ children }) => {
  const [token, _setToken] = useState<string | null>(null)

  useEffect(() => {
    const t = localStorage.getItem('token')
    if (t) _setToken(t)
  }, [])

  const setToken = (t: string) => {
    _setToken(t)
    localStorage.setItem('token', t)
  }

  return (
    <AuthContext.Provider value={{ token, setToken }}>
      {children}
    </AuthContext.Provider>
  )
}

export const useAuth = () => useContext(AuthContext)
