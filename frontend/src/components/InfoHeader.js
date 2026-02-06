import InfoTooltip from "./InfoTooltip";
import "./InfoHeader.css";

export default function InfoHeader({ title, info }) {
  return (
    <div className="info-header">
      <h3>{title}</h3>
      <InfoTooltip text={info} />
    </div>
  );
}
