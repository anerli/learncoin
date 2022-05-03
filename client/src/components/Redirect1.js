import {Link} from "react-router-dom";
import InfoModal from "./InfoModal"

function Redirect1() {
  return (
    <div>
      <div className="redirect">
      <InfoModal text="Find definitions for all cryptocurrency terminology and concepts here."/>
        <Link to="/learning">
          <img
            className="redirect_decal"
            src="https://drive.google.com/uc?export=download&id=1T8ab5ZD5OxG1STCtTYadP2SRsjXSUCUW"
            alt="Crypto learning graphic and redirect"
          />
        </Link>
      </div>
    </div>
  );
}

export default Redirect1;