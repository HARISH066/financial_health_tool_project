import "./InfoTooltip.css";

export default function InfoTooltip({ text }) {
  return (
    <span className="tooltip-wrapper">
      <span className="info-icon">ℹ️</span>
      <span className="tooltip-text">{text}</span>
    </span>
  );
}
