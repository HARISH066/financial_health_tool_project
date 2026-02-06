export default function AIInsightsPanel({ ai }) {
  return (
    <div className="ai-panel">
      <h2>AI Financial Advisor</h2>
      <p>{ai.summary}</p>

      <div className="ai-grid">
        <div>
          <h4>Risks</h4>
          <ul>{ai.risks.map((r, i) => <li key={i}>{r}</li>)}</ul>
        </div>

        <div>
          <h4>Cost Optimization</h4>
          <ul>{ai.cost_optimization.map((c, i) => <li key={i}>{c}</li>)}</ul>
        </div>

        <div>
          <h4>Financial Products</h4>
          <ul>{ai.financial_products.map((p, i) => <li key={i}>{p}</li>)}</ul>
        </div>

        <div>
          <h4>Next Steps</h4>
          <ul>{ai.next_steps.map((s, i) => <li key={i}>{s}</li>)}</ul>
        </div>
      </div>
    </div>
  );
}
