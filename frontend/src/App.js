import React, { useLayoutEffect } from "react";
import IbanForm from "./components/IbanForm";
import IbanList from "./components/IbanList";
import Navbar from "./components/NavBar";
import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  useLayoutEffect(() => {
    document.body.style.backgroundImage = "url(/img/digital_bank.jpg)";
  });

  return (
    <BrowserRouter>
      <div className="App">
        <Navbar />
        <Routes>
          <Route path="/" element={<IbanForm />}>
            {" "}
          </Route>
          <Route path="/ibans" element={<IbanList />}>
            {" "}
          </Route>
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
