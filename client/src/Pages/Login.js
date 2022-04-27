import React, {useState} from 'react';
import {Link} from 'react-router-dom';
import {useCookies} from "react-cookie";
import * as ed from "@noble/ed25519";


// Convert a hex string to a byte array
function hexToBytes(hex) {
  for (var bytes = [], c = 0; c < hex.length; c += 2)
      bytes.push(parseInt(hex.substr(c, 2), 16));
  return bytes;
}

const Login = () => {
    const [cookies, setCookie] = useCookies(['privateKey']);
    const [publicKey, setPublicKey] = useState('');
    //const [valid, setValid] = useState(false);

    const checkLogin = async (formid) =>  {
        const hexPrivateKey = document.getElementById("key").value;
        console.log("submitted: ", hexPrivateKey);
        //const uint8PrivKey = new TextEncoder("utf-8").encode(privKey);
        //const uint8PrivKey = hexToBytes(privKey);

        //const hexPrivateKey = ed.utils.bytesToHex(uint8PrivKey);
        let valid;
        try {
          let publicKey = await ed.getPublicKey(hexPrivateKey);
          let hexPublicKey = ed.utils.bytesToHex(publicKey);
          console.log(hexPublicKey)
          setPublicKey(hexPublicKey);
          setCookie('privateKey', hexPrivateKey, { path: '/' });
          //setValid(true);
          valid = true;
        } catch (err){
          console.log("Error", err.message);
          //setValid(false);
          valid = false;
        }

        //setValid(!valid);

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