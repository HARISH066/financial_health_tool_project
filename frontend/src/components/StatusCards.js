import React from "react";
import InfoHeader from "./InfoHeader";
import StatusDot from "./StatusDot";
import "./StatusCards.css";

/* ---------- Color Helpers ---------- */

const getEligibilityColor = (status) => {
  if (!status) return "#9ca3af"; // gray fallback
  if (status.toLowerCase().includes("eligible") && !status.toLowerCase().includes("conditionally"))
    return "#22c55e"; // green
  if (status.toLowerCase().includes("conditionally"))
    return "#eab308"; // yellow
  return "#ef4444"; // red
};

const getBenchmarkColor = (status) => {
  if (!status) return "#9ca3af";
  if (status.toLowerCase().includes("above") || status.toLowerCase().includes("healthy"))
    return "#22c55e"; // green
  if (status.toLowerCase().includes("average"))
    return "#eab308"; // yellow
  return "#ef4444"; // red
};

/* ---------- Component ---------- */

const StatusCards = ({ credit, benchmark }) => {
  return (
    <div className="status-grid">

      {/* ================= CREDIT ELIGIBILITY ================= */}
      <div className="status-card">
        <InfoHeader
          title="Credit Eligibility"
          info="Indicates whether the business qualifies for loans based on financial health, cash flow, and risk indicators."
        />

        <div className="status-row">
          <StatusDot color={getEligibilityColor(credit.loan_eligibility)} />
          <span className="status-text">
            {credit.loan_eligibility}
          </span>
        </div>

        {credit.risk_flags && credit.risk_flags.length > 0 && (
          <ul className="risk-list">
            {credit.risk_flags.map((flag, index) => (
              <li key={index}>• {flag}</li>
            ))}
          </ul>
        )}
      </div>

      {/* ================= INDUSTRY BENCHMARK ================= */}
      <div className="status-card">
        <InfoHeader
          title="Industry Benchmark"
          info="Compares your business performance against industry averages to identify strengths and weaknesses."
        />

        <div className="benchmark-section">
          <div className="status-row">
            <StatusDot color={getBenchmarkColor(benchmark.profit_margin_status)} />
            <span className="status-text">
              Profit Margin: <strong>{benchmark.profit_margin_status}</strong>
            </span>
          </div>

          <div className="status-row">
            <StatusDot color={getBenchmarkColor(benchmark.cash_flow_status)} />
            <span className="status-text">
              Cash Flow: <strong>{benchmark.cash_flow_status}</strong>
            </span>
          </div>
        </div>
      </div>

    </div>
  );
};

export default StatusCards;
