import { Link } from "react-router-dom";
import InfoModal from "./InfoModal";

function Redirect3() {
    return (
        <div className="redirect">
            <InfoModal text="View LearnCoin's blockchain here."/>
            <Link to="/blockchain">
                <img
                    className="redirect_decal"
                    src="btn3.png"
                    alt="LearnCoin blockchain viewer and redirect"
                />
            </Link>
        </div>
    );
}

export default Redirect3;