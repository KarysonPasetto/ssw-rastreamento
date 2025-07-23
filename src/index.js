import React, { useState } from "react";
import ReactDOM from "react-dom";

function App() {
  const [cnpj, setCnpj] = useState("");
  const [nota, setNota] = useState("");
  const [resultado, setResultado] = useState(null);

  const buscar = async () => {
    const res = await fetch(`/api/rastrear?cnpj=${cnpj}&nota=${nota}`);
    const data = await res.json();
    setResultado(data.rastreamento);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Rastreamento SSW</h1>
      <input placeholder="CNPJ" value={cnpj} onChange={e => setCnpj(e.target.value)} />
      <input placeholder="Nota Fiscal" value={nota} onChange={e => setNota(e.target.value)} />
      <button onClick={buscar}>Buscar</button>
      <pre>{JSON.stringify(resultado, null, 2)}</pre>
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));
