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
            src="btn1.png"
            alt="Crypto learning graphic and redirect"
          />
        </Link>
      </div>
    </div>
  );
}

export default Redirect1;