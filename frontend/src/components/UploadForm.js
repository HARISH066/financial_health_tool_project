import React, { useState } from "react";
import { analyzeCSV } from "../api";

export default function UploadForm({ onResult }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return alert("Please select a CSV file");
    setLoading(true);
    const data = await analyzeCSV(file);
    onResult(data);
    setLoading(false);
  };

  return (
  <div className="upload-card">
    <label className="upload-box">
      <input
        type="file"
        accept=".csv,.xlsx"
        hidden
        onChange={(e) => setFile(e.target.files[0])}
      />
      <div className="upload-content">
        <span className="upload-icon">📂</span>
        <span>{file ? file.name : "Click to upload CSV / Excel file"}</span>
      </div>
    </label>

    <button
      className={`analyze-btn ${loading ? "loading" : ""}`}
      onClick={handleUpload}
      disabled={loading}
    >
      {loading ? "Analyzing..." : "Analyze Financials"}
    </button>
  </div>
);
}
