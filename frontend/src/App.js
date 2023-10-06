import React, { useLayoutEffect } from "react";
import IbanForm from "./components/IbanForm";
import "./App.css";

function App() {
  useLayoutEffect(() => {
    document.body.style.backgroundImage = "url(/img/digital_bank.jpg)";
  });

  return (
    <div className="App">
      <IbanForm />
    </div>
  );
}

export default App;
