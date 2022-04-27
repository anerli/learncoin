import React from 'react';
import {Link} from 'react-router-dom';

let valid = false;

function checkLogin(formid) {
    console.log("submitted: ", document.getElementById("key").value);

    if(document.getElementById("key").value !== ""){
        valid = true;
    }

    if(valid){
        document.getElementById(formid).submit();
    }
    else{
        alert("Invalid Private Key");
    }
};

const Login = () => {
    return (
        <div>
            <a href="#">
            <img src="learncoin.png" className="logo" alt="LearnCoin Logo" height="30" width="170"/>
            </a>
        <div className="login_modal">
            <h4>Login</h4>
            <form id="myform" action="/homepage">
                <input type="text" placeholder="#" id="key" className="login_text"/>
                <input type="button" value="Submit" onClick={() => checkLogin('myform')}/>
            </form>
        </div>
        <h3 className="nokey">No key? &nbsp;
          <Link to="/signup">Sign Up</Link> &nbsp;
          or &nbsp;
          <Link to="/homepage">Guest Login</Link> &nbsp;
        </h3>
        <img src="login_bg.jpg" className="login_bg" alt="login button"></img>
        </div>
        
        
    )
};

export default Login;