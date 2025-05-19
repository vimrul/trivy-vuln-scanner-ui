import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  server: {
    host: '0.0.0.0',
    port: 3000,
  },
  build: {
    outDir: 'dist',
  },
  // 👇 ADD THIS
  optimizeDeps: {
    include: ['react-router-dom'],
  },
  // 👇 ADD THIS to fix 404 issue on refresh or deep linking
  preview: {
    fallback: 'index.html',
  },
});
