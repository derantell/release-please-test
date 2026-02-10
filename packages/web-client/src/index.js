function render(root) {
  root.innerHTML = `
    <div>
      <h1>Monorepo Web Client</h1>
      <p>Version 0.1.0</p>
    </div>
  `;
}

if (typeof document !== "undefined") {
  render(document.getElementById("app"));
}

module.exports = { render };
