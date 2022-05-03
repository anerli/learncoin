import { Link } from "react-router-dom";
import InfoModal from "./InfoModal";

function Redirect3() {
    return (
        <div className="redirect">
            <InfoModal text="View LearnCoin's blockchain here."/>
            <Link to="/blockchain">
                <img
                    className="redirect_decal"
                    src="https://drive.google.com/uc?export=download&id=1T8ab5ZD5OxG1STCtTYadP2SRsjXSUCUW"
                    alt="LearnCoin blockchain viewer and redirect"
                />
            </Link>
        </div>
    );
}

export default Redirect3;