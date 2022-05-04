import { Link } from "react-router-dom";
import InfoModal from "./InfoModal";

function Redirect4() {
    return (
        <div className="redirect">
            <InfoModal text="Login to the LearnCoin wallet here."/>
            <Link to="/login">
                <img
                    className="redirect_decal"
                    src="https://drive.google.com/uc?export=download&id=19-CaQSVoGemMhxk4fBSfr3c_VO0UGTvH"
                    alt="LearnCoin wallet graphic and redirect"
                />
            </Link>
        </div>
    );
}

export default Redirect4;