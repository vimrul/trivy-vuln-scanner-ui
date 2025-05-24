import React, { useEffect, useState } from 'react';
import { useAuth } from '../context/AuthContext';
import { getReports } from '../services/reportService';

const HistoryPage = () => {
  const { token } = useAuth();
  const [reports, setReports] = useState<any[]>([]);

  useEffect(() => {
    if (!token) return;
    getReports(token).then(setReports).catch(console.error);
  }, [token]);

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">Scan History</h1>
      <pre className="bg-gray-100 p-4 rounded">
        {JSON.stringify(reports, null, 2)}
      </pre>
    </div>
  );
};

export default HistoryPage;
