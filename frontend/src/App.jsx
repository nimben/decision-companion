import { useState } from "react";

function App() {
  const [books, setBooks] = useState("");
  const [weight, setWeight] = useState(1);
  const [result, setResult] = useState(null);

  const handleSubmit = async () => {
    const bookList = books.split(",").map(b => b.trim());

    const response = await fetch("http://127.0.0.1:8000/evaluate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        books: bookList,
        weight: Number(weight)
      })
    });

    const data = await response.json();
    setResult(data);
  };

  return (
    <div style={{ padding: "40px" }}>
      <h1>Decision Companion 📚</h1>

      <input
        type="text"
        placeholder="Enter books separated by commas"
        value={books}
        onChange={(e) => setBooks(e.target.value)}
        style={{ width: "300px", marginBottom: "10px" }}
      />

      <br />

      <input
        type="number"
        placeholder="Weight"
        value={weight}
        onChange={(e) => setWeight(e.target.value)}
      />

      <br /><br />

      <button onClick={handleSubmit}>
        Get Recommendation
      </button>

      {result && (
        <div style={{ marginTop: "20px" }}>
          <h2>Recommended Book:</h2>
          <p>{result.best_book}</p>
        </div>
      )}
    </div>
  );
}

export default App;