import "../App.css";

const IbanEntry = (props) => {
  const { url, iban, country_code, is_valid, validation_date } = props;
  return (
    <div className="iban_entry">
      <p>IBAN Nr: {iban}</p>
      <p>Validation date: {validation_date}</p>
      <p>Status: {is_valid ? "Valid" : "Invalid"}</p>
    </div>
  );
};

export default IbanEntry;
