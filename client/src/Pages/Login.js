import React, {useState} from 'react';
import {Link} from 'react-router-dom';
import {useCookies} from "react-cookie";
import * as ed from "@noble/ed25519";

const Login = () => {
    const [cookies, setCookie] = useCookies(['privateKey']);
    // Do NOT remove items from useState tuples
    const [publicKey, setPublicKey] = useState('');

    const checkLogin = async (formid) =>  {
        const hexPrivateKey = document.getElementById("key").value;
        console.log("submitted: ", hexPrivateKey);

        let valid;
        try {
          let publicKey = await ed.getPublicKey(hexPrivateKey);
          let hexPublicKey = ed.utils.bytesToHex(publicKey);
          console.log(hexPublicKey)
          setPublicKey(hexPublicKey);
          setCookie('privateKey', hexPrivateKey, { path: '/' });
          valid = true;
        } catch (err){
          console.log("Error", err.message);
          valid = false;
        }

        if(valid){
            document.getElementById(formid).submit();
        }
        else{
            alert("Invalid Private Key");
        }
    };

    return (
        <div>
            <Link to='/'>BACK</Link>
            <a href="#">
            <img src="learncoin.png" className="logo" alt="LearnCoin Logo" height="30" width="170"/>
            </a>
        <div className="login_modal">
            <h4>Login</h4>
            <form id="myform" action="/homepage">
                <input type="text" placeholder="Your 64-Digit Hexidecimal Private Key" id="key" className="login_text"/>
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