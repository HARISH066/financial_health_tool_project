export default function CreditCard({ credit }) {
  return (
    <div>
      <h3>Creditworthiness</h3>
      <p>Status: {credit.loan_eligibility}</p>
      <ul>
        {credit.risk_flags.map((flag, i) => (
          <li key={i}>{flag}</li>
        ))}
      </ul>
    </div>
  );
}
