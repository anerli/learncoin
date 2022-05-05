import {Link} from "react-router-dom";
import InfoModal from "./InfoModal";

function Redirect2() {
    return (
      <div>
        <div className="redirect">
        <InfoModal text="Learn how to mine LearnCoin on your own server here."/>
          <Link to="/mining">
            <img
              className="redirect_decal"
              src="btn2.png"
              alt="LearnCoin mining graphic and redirect"
            />
          </Link>
        </div>
      </div>
    );
  }
  
  export default Redirect2;