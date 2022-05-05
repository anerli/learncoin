import { Link } from "react-router-dom";
import InfoModal from "./InfoModal";

function Redirect4() {
    return (
        <div className="redirect">
            <InfoModal text="Login to the LearnCoin wallet here."/>
            <Link to="/login">
                <img
                    className="redirect_decal"
                    src="btn4.png"
                    alt="LearnCoin wallet graphic and redirect"
                />
            </Link>
        </div>
    );
}

export default Redirect4;