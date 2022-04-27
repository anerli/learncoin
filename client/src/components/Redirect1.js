import {Link} from "react-router-dom";
import InfoModal from "./InfoModal"

function Redirect1() {
  return (
    <div>
      <div className="redirect">
      <InfoModal text="The blockchain viewer is a common interface used to visualize many transactions. The list should be sortable from oldest (genesis block) to newest."/>
        <Link to="/blockchain">
          <img
            className="redirect_decal"
            src="https://drive.google.com/uc?export=download&id=1T8ab5ZD5OxG1STCtTYadP2SRsjXSUCUW"
            alt="blockchain viewer graphic"
          />
        </Link>
      </div>
    </div>
  );
}

export default Redirect1;