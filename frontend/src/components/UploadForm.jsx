import "./FileUpload.css";

export default function FileUpload({ onFileSelect }) {
  return (
    <label className="upload-box">
      <input
        type="file"
        accept=".csv"
        hidden
        onChange={(e) => onFileSelect(e.target.files[0])}
      />
      <div className="upload-content">
        <span className="upload-icon">📁</span>
        <span>Click or Drag CSV File</span>
      </div>
    </label>
  );
}
