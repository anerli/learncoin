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
            <h1>Login using your private key</h1>
            <form id="myform" action="/Homepage">
                <input type="text" placeholder="Enter Private Key" id="key"/>
                <input type="button" value="Submit" onClick={() => checkLogin('myform')}/>
            </form>
            <h3>Don't have a private key? &nbsp;
                <Link to="/signup">SIGNUP</Link>
            </h3>
            
        </div>
    )
};

export default Login;