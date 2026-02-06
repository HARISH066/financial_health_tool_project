export default function AIInsights({ ai }) {
  return (
    <div>
      <h3>AI Insights</h3>
      <p>{ai.summary}</p>

      <h4>Risks</h4>
      <ul>{ai.risks.map((r, i) => <li key={i}>{r}</li>)}</ul>

      <h4>Cost Optimization</h4>
      <ul>{ai.cost_optimization.map((c, i) => <li key={i}>{c}</li>)}</ul>

      <h4>Recommended Products</h4>
      <ul>{ai.financial_products.map((p, i) => <li key={i}>{p}</li>)}</ul>

      <h4>Next Steps</h4>
      <ul>{ai.next_steps.map((s, i) => <li key={i}>{s}</li>)}</ul>
    </div>
  );
}
