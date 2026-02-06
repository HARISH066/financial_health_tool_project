const StatusDot = ({ color }) => {
  return (
    <span
      style={{
        display: "inline-block",
        width: "10px",
        height: "10px",
        borderRadius: "50%",
        backgroundColor: color,
        marginRight: "6px",
      }}
    />
  );
};

export default StatusDot;
