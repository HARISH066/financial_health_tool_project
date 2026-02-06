import React from "react";
import { PieChart, Pie, Cell } from "recharts";
import InfoTooltip from "./InfoTooltip";
import { formatINR } from "../utils/format";
import "./KpiCards.css";

const FinanceScoreDonut = ({ score }) => {
  const data = [
    { name: "Score", value: score },
    { name: "Remaining", value: 100 - score }
  ];

  return (
    <PieChart width={120} height={120}>
      <Pie
        data={data}
        dataKey="value"
        cx="50%"
        cy="50%"
        innerRadius={40}
        outerRadius={55}
        startAngle={90}
        endAngle={-270}
        stroke="none"
      >
        <Cell fill="#22c55e" />
        <Cell fill="#e5e7eb" />
      </Pie>

      {/* Center text */}
      <text
        x="50%"
        y="50%"
        textAnchor="middle"
        dominantBaseline="middle"
        fontSize="16"
        fontWeight="600"
        fill="#16a34a"
      >
        {score}%
      </text>
    </PieChart>
  );
};

const KpiCards = ({ metrics, assessment }) => {
  return (
    <div className="kpi-grid">
      {/* Revenue */}
      <div className="kpi-card">
        <div className="kpi-header">
          <span>Revenue</span>
          <InfoTooltip text="Total income generated from business operations during the selected period." />
        </div>
        <h2>₹{formatINR(metrics.revenue)}</h2>
      </div>

      {/* Expenses */}
      <div className="kpi-card">
        <div className="kpi-header">
          <span>Expenses</span>
          <InfoTooltip text="Total operational costs including procurement, utilities, salaries, and overheads." />
        </div>
        <h2>₹{formatINR(metrics.expenses)}</h2>
      </div>

      {/* Profit */}
      <div className="kpi-card">
        <div className="kpi-header">
          <span>Profit</span>
          <InfoTooltip text="Net earnings after subtracting all expenses from revenue." />
        </div>
        <h2>₹{formatINR(metrics.profit)}</h2>
      </div>

      {/* Finance Score (WITH DONUT) */}
      <div className="kpi-card finance-score-card">
        <div className="kpi-header">
          <span>Finance Score</span>
          <InfoTooltip text="Overall financial health score calculated using profitability, cash flow, and risk indicators." />
        </div>

        <FinanceScoreDonut score={assessment.score} />
      </div>
    </div>
  );
};

export default KpiCards;
