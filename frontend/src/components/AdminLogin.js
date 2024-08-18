import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import styled from 'styled-components';
import MEULogo from '../assets/MEU_logo.png';

const LoginWrapper = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background: linear-gradient(135deg, #A62B2F 0%, #764ba2 100%); /* MEU dark red with a gradient */
`;

const LoginBox = styled.div`
  padding: 40px;
  background: rgba(255, 255, 255, 0.9);
  border-radius: 15px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  width: 320px;
  text-align: center;
`;

const Logo = styled.img`
  width: 120px;
  margin-bottom: 20px;
`;

const Input = styled.input`
  margin-bottom: 20px;
  padding: 15px;
  width: 100%;
  border-radius: 25px;
  border: 1px solid #ccc;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
`;

const Button = styled.button`
  padding: 15px;
  width: 100%;
  background-color: #A62B2F; /* MEU dark red */
  border: none;
  border-radius: 25px;
  color: white;
  cursor: pointer;
  font-weight: bold;
  letter-spacing: 1px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  transition: all 0.3s ease;

  &:hover {
    background-color: #8C2227; /* Slightly darker red for hover */
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
  }
`;

function AdminLogin() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = async () => {
    try {
      const response = await axios.post('http://localhost:5001/admin/login', { email, password }, { withCredentials: true });
      if (response.status === 200) {
        navigate('/admin');
      }
    } catch (error) {
      console.error('Login error:', error);
      alert('Invalid credentials');
    }
  };

  return (
    <LoginWrapper>
      <LoginBox>
        <Logo src={MEULogo} alt="MEU Logo" />
        <h2>Admin Login</h2>
        <Input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <Input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <Button onClick={handleLogin}>Login</Button>
      </LoginBox>
    </LoginWrapper>
  );
}

export default AdminLogin;
