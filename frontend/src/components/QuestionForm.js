// src/components/QuestionForm.js
import React, { useState } from 'react';
import axios from 'axios';
import styled from 'styled-components';

const FormWrapper = styled.div`
  padding: 20px;
`;

const Input = styled.input`
  margin-bottom: 15px;
  padding: 10px;
  width: 100%;
  border-radius: 5px;
  border: 1px solid #ccc;
`;

const Button = styled.button`
  padding: 10px;
  background-color: #007bff;
  border: none;
  border-radius: 5px;
  color: white;
  cursor: pointer;

  &:hover {
    background-color: #0056b3;
  }
`;

function QuestionForm() {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');

  const handleSubmit = async () => {
    const data = { question, answer };
    await axios.post('http://localhost:5001/admin/add', data);
    alert('Q&A Added Successfully');
  };

  return (
    <FormWrapper>
      <h2>Add Q&A</h2>
      <Input
        type="text"
        placeholder="Question"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />
      <Input
        type="text"
        placeholder="Answer"
        value={answer}
        onChange={(e) => setAnswer(e.target.value)}
      />
      <Button onClick={handleSubmit}>Submit</Button>
    </FormWrapper>
  );
}

export default QuestionForm;
