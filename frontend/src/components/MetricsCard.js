export default function MetricsCard({ metrics, assessment }) {
  return (
    <div>
      <h3>Financial Overview<InfoTooltip text="Summary of key financial performance indicators" /></h3>
      <p>Revenue: ₹{metrics.revenue}<InfoTooltip text="Total income generated from business operations" /></p>
      <p>Expenses: ₹{metrics.expenses}<InfoTooltip text="Total operational costs" /></p>
      <p>Profit: ₹{metrics.profit}<InfoTooltip text="Net earnings after subtracting all expenses from revenue" /></p>
      <p>Profit Margin: {metrics.profit_margin}<InfoTooltip text="Profit as a percentage of revenue" /></p>
      <p>Cash Flow Ratio: {metrics.cash_flow_ratio}<InfoTooltip text="Measures a company's ability to generate cash" /></p>

      <h4>Health Score<InfoTooltip text="Overall financial health score" /></h4>
      <p>Score: {assessment.score}<InfoTooltip text="Finance score based on various indicators" /></p>
      <p>Risk: {assessment.risk}<InfoTooltip text="Level of financial risk identified" /></p>
    </div>
  );
}
