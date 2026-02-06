import React from "react";
import InfoHeader from "./InfoHeader";
import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  ResponsiveContainer,
  Legend
} from "recharts";

import { formatINR } from "../utils/format";


const ProfitPie = ({ metrics }) => {
  const data = [
    { name: "Profit", value: Math.round(metrics.profit) },
    { name: "Expenses", value: Math.round(metrics.expenses) }
  ];

  const COLORS = ["#22c55e", "#ef4444"];

  return (
    <div className="chart-card">
      <InfoHeader
        title="Profit Distribution"
        info="Shows how revenue is split between expenses and net profit."
      />

      <ResponsiveContainer width="100%" height={300}>
        <PieChart>
          <Pie
            data={data}
            dataKey="value"
            outerRadius={100}
            label={({ name, value }) => `${name}: ₹${formatINR(value)}`}

          >
            {data.map((_, i) => (
              <Cell key={i} fill={COLORS[i]} />
            ))}
          </Pie>
          <Tooltip />
          <Legend />
        </PieChart>
      </ResponsiveContainer>
    </div>
  );
};

export default ProfitPie;
