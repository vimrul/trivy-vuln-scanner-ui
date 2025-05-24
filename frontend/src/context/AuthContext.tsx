import React, {
  createContext,
  useContext,
  useState,
  ReactNode,
  useEffect
} from 'react';

interface AuthContextType {
  token: string | null;
  setToken: (tok: string | null) => void;
}

const AuthContext = createContext<AuthContextType>({
  token: null,
  setToken: () => {}
});

export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [token, rawSetToken] = useState<string | null>(
    () => localStorage.getItem('token')
  );

  const setToken = (tok: string | null) => {
    if (tok) {
      localStorage.setItem('token', tok);
    } else {
      localStorage.removeItem('token');
    }
    rawSetToken(tok);
  };

  // keep in sync if you ever call localStorage elsewhere
  useEffect(() => {
    const stored = localStorage.getItem('token');
    if (stored && stored !== token) {
      rawSetToken(stored);
    }
  }, []);

  return (
    <AuthContext.Provider value={{ token, setToken }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
