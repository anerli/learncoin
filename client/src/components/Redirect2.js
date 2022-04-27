import {Link} from "react-router-dom";

function Redirect2() {
    return (
      <div>
        <div className="redirect">
        <div class="info_modal" title="A wallet interface allows for the exchange of cryptocurrency (LearnCoin). Users should specify the amount of LC to send in the left textbox. Users should also enter the private key identification number of the receiver in the right text box.">
                <img src="https://drive.google.com/uc?export=download&id=1A1ZS6cN2rRB2mDvqjICdxECrD8GxOA4R"/>
            </div>
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