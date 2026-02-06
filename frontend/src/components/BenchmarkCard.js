export default function BenchmarkCard({ benchmark }) {
  return (
    <div>
      <h3>Industry Benchmark ({benchmark.industry})</h3>
      <p>Profit Margin: {benchmark.profit_margin_status}</p>
      <p>Cash Flow: {benchmark.cash_flow_status}</p>
    </div>
  );
}
