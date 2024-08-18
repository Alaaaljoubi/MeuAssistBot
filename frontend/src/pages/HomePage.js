import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import styled from 'styled-components';
import axios from 'axios';  // Import axios
import MEULogo from '../assets/MEU_logo.png';

const HomeWrapper = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  padding: 20px;
  background-color: ${({ theme }) => theme.background};
  color: ${({ theme }) => theme.color};
  transition: background-color 0.3s, color 0.3s;
`;

const Logo = styled.img`
  width: 150px;
  margin-bottom: 20px;
`;

const ContentWrapper = styled.div`
  width: 100%;
  max-width: 600px;
  padding: 20px;
  background-color: ${({ theme }) => theme.inputBackground};
  border-radius: 15px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  text-align: center;
`;

const Heading = styled.h1`
  margin-bottom: 20px;
  font-family: 'Poppins', sans-serif;
  letter-spacing: 1px;
`;

const Input = styled.input`
  margin-bottom: 15px;
  padding: 15px;
  width: 100%;
  border-radius: 25px;
  border: 1px solid #ccc;
  background-color: ${({ theme }) => theme.inputBackground};
  color: ${({ theme }) => theme.color};
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s, color 0.3s;
`;

const Button = styled.button`
  padding: 15px 30px;
  width: 100%;
  background-color: ${({ theme }) => theme.buttonBackground};
  color: ${({ theme }) => theme.buttonColor};
  border: none;
  border-radius: 25px;
  cursor: pointer;
  margin-top: 10px;
  font-family: 'Poppins', sans-serif;
  font-weight: bold;
  letter-spacing: 1px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  transition: all 0.3s ease;

  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
  }
`;

const ToggleButton = styled(Button)`
  background-color: ${({ theme }) => theme.toggleBackground};
  margin-bottom: 20px;

  &:hover {
    background-color: #777;
  }
`;

const AnswerBox = styled.div`
  margin-top: 20px;
  padding: 20px;
  background-color: ${({ theme }) => theme.inputBackground};
  border-radius: 15px;
  color: ${({ theme }) => theme.color};
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
`;

const AdminButton = styled(Button)`
  margin-top: 30px;
  background-color: ${({ theme }) => theme.buttonBackground};

  &:hover {
    background-color: #0056b3;
  }
`;

function HomePage({ toggleTheme }) {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');
  const navigate = useNavigate();

  const handleAsk = async () => {
    try {
      const response = await axios.post('http://localhost:5001/kbs', { question });
      setAnswer(response.data.answer);
    } catch (error) {
      console.error('Error:', error);
      setAnswer("Sorry, I couldn't find the answer to that question.");
    }
  };

  const handleAdminLogin = () => {
    navigate('/login');
  };

  return (
    <HomeWrapper>
      <Logo src={MEULogo} alt="MEU Logo" />
      <ContentWrapper>
        <ToggleButton onClick={toggleTheme}>
          Switch Theme
        </ToggleButton>
        <Heading>Ask Your Question</Heading>
        <Input
          type="text"
          placeholder="Type your question..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />
        <Button onClick={handleAsk}>Ask</Button>
        {answer && <AnswerBox>{answer}</AnswerBox>}
        <AdminButton onClick={handleAdminLogin}>Admin Page</AdminButton>
      </ContentWrapper>
    </HomeWrapper>
  );
}

export default HomePage;
