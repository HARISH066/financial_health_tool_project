import React from "react";
import InfoHeader from "./InfoHeader";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from "recharts";

const CashFlowLine = ({ forecast }) => {
  return (
    <div className="chart-card">
      <InfoHeader
        title="Cash Flow Forecast"
        info="Projected future cash inflow based on current financial performance."
      />

      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={forecast}>
          <XAxis dataKey="month" />
          <YAxis tickFormatter={(v) => `₹${Math.round(v / 1000)}K`} />
          <Tooltip
            formatter={(value) => [
              `₹${Math.round(value).toLocaleString("en-IN")}`,
              "Expected Cash Flow"
            ]}
          />
          <Line
            type="monotone"
            dataKey="expected_cash_flow"
            stroke="#22c55e"
            strokeWidth={3}
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
};

export default CashFlowLine;
