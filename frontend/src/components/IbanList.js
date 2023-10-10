import "../App.css";
import axiosInstance from "../axiosApi";
import { useState, useEffect } from "react";

import IbanEntry from "./IbanEntry";

function IbanList() {
  const [ibans, setIbans] = useState([]);
  useEffect(() => {
    axiosInstance
      .get("/ibans/")
      .then((response) => {
        setIbans(response.data.results);
      })
      .catch((err) => {
        console.log(err);
      });
  }, []);

  switch (ibans.length > 0) {
    case true:
      return (
        <section>
          {ibans.map((iban) => {
            return <IbanEntry key={iban.url} {...iban} />;
          })}
        </section>
      );

    case false:
      return (
        <section>
          <div className="iban_entry">
            <p>No IBAN numbers to display</p>
          </div>
        </section>
      );
  }
}

export default IbanList;
