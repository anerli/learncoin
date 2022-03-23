import {Link} from "react-router-dom";

function Redirect1() {
  return (
    <div>
      <div className="redirect">
        <Link to="/blockchain">
          <img
            className="redirect_decal"
            src="https://drive.google.com/uc?export=download&id=1T8ab5ZD5OxG1STCtTYadP2SRsjXSUCUW"
          />
        </Link>
      </div>
    </div>
  );
}

export default Redirect1;