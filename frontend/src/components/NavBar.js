import { Link } from "react-router-dom";

const Navbar = (props) => {
  return (
    <div>
      <Link push="true" to="/">
        <button>Validator</button>
      </Link>
      <Link push="true" to="/ibans">
        <button>IBAN List</button>
      </Link>
    </div>
  );
};

export default Navbar;
