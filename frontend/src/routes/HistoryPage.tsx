// src/routes/HistoryPage.tsx
import React from 'react';
import { useAuth } from '../context/AuthContext';
import { getReports } from '../services/reportService';

export default function HistoryPage() {
  const { token } = useAuth();
  // you’ll probably fetch history here...
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Scan History</h1>
      <p>Your past scan reports will show up here.</p>
    </div>
  );
}
