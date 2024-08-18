import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import styled, { ThemeProvider } from 'styled-components';
import AdminLogin from './components/AdminLogin';
import AdminPage from './pages/AdminPage';
import HomePage from './pages/HomePage';

// Define the light and dark themes
const lightTheme = {
  background: '#ffffff',
  color: '#333333',
  buttonBackground: '#A62B2F',
  buttonColor: '#ffffff',
  toggleBackground: '#333333',
  inputBackground: '#F1F1F1',
};

const darkTheme = {
  background: '#333333',
  color: '#F1F1F1',
  buttonBackground: '#A62B2F',
  buttonColor: '#ffffff',
  toggleBackground: '#A62B2F',
  inputBackground: '#555555',
};

const AppWrapper = styled.div`
  min-height: 100vh;
  background-color: ${({ theme }) => theme.background};
  color: ${({ theme }) => theme.color};
  transition: background-color 0.3s, color 0.3s;
`;

function App() {
  const [theme, setTheme] = useState(lightTheme);

  const toggleTheme = () => {
    setTheme(theme === lightTheme ? darkTheme : lightTheme);
  };

  return (
    <ThemeProvider theme={theme}>
      <AppWrapper>
        <Router>
          <Routes>
            <Route path="/login" element={<AdminLogin toggleTheme={toggleTheme} />} />
            <Route path="/admin" element={<AdminPage toggleTheme={toggleTheme} />} />
            <Route path="/" element={<HomePage toggleTheme={toggleTheme} />} />
          </Routes>
        </Router>
      </AppWrapper>
    </ThemeProvider>
  );
}

export default App;
