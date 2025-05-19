// src/components/Navbar.tsx
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="bg-gray-800 p-4 text-white flex gap-6">
      <Link to="/">Login</Link>
      <Link to="/projects">Projects</Link>
      <Link to="/history">History</Link>
    </nav>
  );
};

export default Navbar;
