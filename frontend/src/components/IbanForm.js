import "../App.css";
import axiosInstance from "../axiosApi";
import { useState, useEffect } from "react";

function IbanForm() {
  const input_field = document.getElementById("iban_input_field");

  const [IBAN, setIBAN] = useState("");
  const [message, setMessage] = useState();

  const handleChange = (e) => {
    // set the value of IBAN and also trigger the post request
    e.preventDefault();
    setIBAN(e.target.value);
  };

  const sendIBAN = async (commit = false) => {
    let payload = {
      iban: IBAN,
      commit: commit,
    };

    try {
      let response = await axiosInstance.post("/ibans/", payload);
      console.log(response);
      if (commit) {
        input_field.value = "";
        setMessage("Validation OK. Your IBAN was saved to the database.");
        return;
      }
      response.data.is_valid
        ? setMessage("Your IBAN is valid")
        : setMessage("Your IBAN is invalid");
    } catch (error) {
      console.log(error);
      error.code !== "ERR_NETWORK" && error.code !== "ERR_BAD_RESPONSE"
        ? setMessage(error.response.data.errors[0])
        : setMessage("Network unavailable, try again later");
    }
  };

  const doNothing = (e) => {
    // stop form submission by pressing enter
    e.preventDefault();
  };

  useEffect(() => {
    // every time the iban changes, send a request to check the validity on the fly
    sendIBAN();
  }, [IBAN]);

  return (
    <div className="iban_form">
      <form onSubmit={doNothing}>
        <label>
          Please enter your IBAN number
          <input
            id="iban_input_field"
            name="iban"
            className="iban_field"
            type="text"
            onChange={(e) => handleChange(e)}
            maxLength={34}
          />
        </label>
      </form>
      <p>{message}</p>
      <button className="submitButton" onClick={() => sendIBAN(true)}>
        Validate
      </button>
    </div>
  );
}

export default IbanForm;
