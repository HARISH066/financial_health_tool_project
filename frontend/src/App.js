import React, { useState } from "react";
import UploadForm from "./components/UploadForm";
import KpiCards from "./components/KpiCards";
import RevenueExpenseBar from "./components/RevenueExpenseBar";
import CashFlowLine from "./components/CashFlowLine";
import ProfitPie from "./components/ProfitPie";
import StatusCards from "./components/StatusCards";
import AIInsightsPanel from "./components/AIInsightsPanel";
import "./App.css";

function App() {
  const [data, setData] = useState(null);

  return (
    <div style={{ padding: "60px", background: "#f4f6f8" }}>
      <h2>SME Financial Health Dashboard</h2>

      <UploadForm onResult={setData} />

      {data && (
        <>
          <KpiCards metrics={data.metrics} assessment={data.assessment} />

          <div className="kpi-grid">
            <RevenueExpenseBar metrics={data.metrics} />
            <ProfitPie metrics={data.metrics} />
          </div>

          <CashFlowLine forecast={data.forecast} />

          <StatusCards
            credit={data.creditworthiness}
            benchmark={data.benchmark}
          />

          <AIInsightsPanel ai={data.ai_insights} />
        </>
      )}
    </div>
  );
}

export default App;
