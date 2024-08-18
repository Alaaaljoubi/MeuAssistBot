// src/api/api.js
import axios from 'axios';

const API_URL = 'http://localhost:5001';

export const login = (credentials) => axios.post(`${API_URL}/admin/login`, credentials);
export const logout = () => axios.post(`${API_URL}/admin/logout`);
export const addQA = (data) => axios.post(`${API_URL}/admin/add`, data);
export const updateQA = (data) => axios.put(`${API_URL}/admin/update`, data);
export const deleteQA = (data) => axios.delete(`${API_URL}/admin/delete`, { data });
