import { LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid } from "recharts";

export default function ForecastChart({ forecast }) {
  return (
    <div>
      <h3>Cash Flow Forecast</h3>
      <LineChart width={400} height={250} data={forecast}>
        <XAxis dataKey="month" />
        <YAxis />
        <Tooltip />
        <CartesianGrid stroke="#ccc" />
        <Line type="monotone" dataKey="expected_cash_flow" />
      </LineChart>
    </div>
  );
}
