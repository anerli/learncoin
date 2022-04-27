import {Link} from "react-router-dom";
import InfoModal from "./InfoModal";

function Redirect2() {
    return (
      <div>
        <div className="redirect">
        <InfoModal text="This is where you can exerience mining cryptocurrecy."/>
          <Link to="/mining">
            <img
              className="redirect_decal"
              src="https://drive.google.com/uc?export=download&id=1f9XsCJ9nqDp72mQ99wDdOjiA_widhug4"
              alt="learncoin mining graphic"
            />
          </Link>
        </div>
      </div>
    );
  }
  
  export default Redirect2;