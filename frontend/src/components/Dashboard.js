// src/components/Dashboard.js
import React from 'react';
import { Link } from 'react-router-dom';
import styled from 'styled-components';

const DashboardWrapper = styled.div`
  padding: 20px;
`;

const NavButton = styled(Link)`
  display: inline-block;
  margin: 10px 0;
  padding: 10px;
  background-color: #007bff;
  color: white;
  text-decoration: none;
  border-radius: 5px;

  &:hover {
    background-color: #0056b3;
  }
`;

function Dashboard() {
  return (
    <DashboardWrapper>
      <h2>Admin Dashboard</h2>
      <NavButton to="/admin/add">Add New Q&A</NavButton>
      <NavButton to="/admin/view">View Q&A</NavButton>
    </DashboardWrapper>
  );
}

export default Dashboard;
