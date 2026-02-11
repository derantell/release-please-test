function render(root) {
  console.log("[web-client] rendering app");
  root.innerHTML = `
    <div>
      <h1>Monorepo Web Client</h1>
      <p>Version 0.1.0</p>
    </div>
  `;
  console.log("[web-client] render complete");
}

if (typeof document !== "undefined") {
  render(document.getElementById("app"));
}

module.exports = { render };
