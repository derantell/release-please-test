const express = require("express");

const app = express();
const PORT = process.env.PORT || 3000;

app.get("/health", (req, res) => {
  res.json({ status: "ok", version: "0.1.0" });
});

app.get("/api/items", (req, res) => {
  res.json([
    { id: 1, name: "Item A" },
    { id: 2, name: "Item B" },
  ]);
});

app.listen(PORT, () => {
  console.log(`API server running on port ${PORT}`);
});
