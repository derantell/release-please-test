const express = require("express");

const app = express();
const PORT = process.env.PORT || 3000;

app.use((req, res, next) => {
  console.log(`${new Date().toISOString()} ${req.method} ${req.url}`);
  next();
});

app.get("/health", (req, res) => {
  res.json({ status: "ok", version: "0.2.0" });
});

app.get("/api/items", (req, res) => {
  res.json([
    { index: 1, name: "Item A" },
    { index: 2, name: "Item B" },
  ]);
});

app.listen(PORT, () => {
  console.log(`API server running on port ${PORT}`);
});
