import logo from './logo.svg';
import './App.css';
import React from 'react';


function App() {

  const downloadile = () => {
    const options = {method: "GET"};
    fetch("http://127.0.0.1:5000/", options).then(response => response.json()).then(result => {alert(result)})
  }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
      <button onClick={downloadile}>
        Hello!
      </button>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
