import axios from "axios";

// Use relative path for single deployment, or environment variable
const API_URL = process.env.REACT_APP_API_URL || "";

export const analyzeCSV = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  const response = await axios.post(
    `${API_URL}/analyze-csv`,
    formData,
    { headers: { "Content-Type": "multipart/form-data" } }
  );

  return response.data;
};
