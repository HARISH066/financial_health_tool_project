export const formatINR = (value) => {
  if (value === null || value === undefined) return "0";
  return Math.round(value).toLocaleString("en-IN");
};
