import { use, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'


async function AiResponse() {
    let userInput = document.getElementById('prompt').value;
    alert(userInput);
    document.getElementById('prompt').disabled = true;
    document.getElementById('prompt').value = '';

    try {
      // Send a POST request to the Flask route on port 8080
      let response = await fetch('http://localhost:8080/prompt', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ input: userInput })
      });

      response = await response.json();
      alert(JSON.stringify(response)); // Convert object to string for alert
    } catch (error) {
      alert('Error: ' + error.message);
    }
    
    document.getElementById('prompt').disabled = false;
}

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <input type="text" id="prompt" placeholder="Enter your prompt here" />
        <button onClick={AiResponse}>Send Prompt</button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
