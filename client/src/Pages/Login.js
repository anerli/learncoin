import React, {useState} from 'react';
import {Link} from 'react-router-dom';
import {useCookies} from "react-cookie";
import * as ed from "@noble/ed25519";

const Login = () => {
    const [cookies] = useCookies(['privateKey']);
    const [publicKey, setPublicKey] = useState('');
    const [valid, setValid] = useState(false);

    const checkLogin = (formid) => {
        const privKey = document.getElementById("key").value;
        console.log("submitted: ", privKey);
        const uint8PrivKey = new TextEncoder("utf-8").encode(privKey);
        const hexPrivateKey = ed.utils.bytesToHex(uint8PrivKey);
        ed.getPublicKey(hexPrivateKey).then(
            (publicKey) => {
                let hexPublicKey = ed.utils.bytesToHex(publicKey);
                setPublicKey(hexPublicKey);
            }
        )
        setValid(!valid);

        if(valid){
            document.getElementById(formid).submit();
        }
        else{
            alert("Invalid Private Key");
        }
    };

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
        <img src="login_bg.jpg" className="login_bg"></img>
        </div>
        
        
    )
};

export default Login;