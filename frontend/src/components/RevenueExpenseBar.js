import React from "react";
import InfoHeader from "./InfoHeader";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  Legend
} from "recharts";

import { formatINR } from "../utils/format";




const RevenueExpenseBar = ({ metrics }) => {
  const data = [
    {
      name: "Financials",
      Revenue: metrics.revenue,
      Expenses: metrics.expenses
    }
  ];

  return (
    <div className="chart-card">
      <InfoHeader
        title="Revenue vs Expenses"
        info="Comparison between total revenue and total expenses to understand profitability at a glance."
      />

      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data}>
          <XAxis dataKey="name" />
          <YAxis
  tickFormatter={(value) => formatINR(value)}
  width={90}
/>

          <Tooltip
  formatter={(value) => formatINR(value)}
  labelFormatter={() => "Financials"}
/>

          <Legend />
          <Bar dataKey="Revenue" fill="#22c55e" />
          <Bar dataKey="Expenses" fill="#ef4444" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
};

export default RevenueExpenseBar;
