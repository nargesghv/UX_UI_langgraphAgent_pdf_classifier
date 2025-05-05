import axios from 'axios';

const API = axios.create({
  baseURL: "http://localhost:8000",
});

export const uploadFile = (file) => {
  const formData = new FormData();
  formData.append("file", file);
  return API.post("/upload", formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });
};
