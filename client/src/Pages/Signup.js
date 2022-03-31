import React, { useState } from 'react';
import { useCookies } from 'react-cookie';
import { Link } from 'react-router-dom';
import { makeTransaction } from "../logic/transactions";
const EC = require('elliptic').ec;



const Signup = () => {
    const [cookies, setCookie, removeCookie] = useCookies(['privateKey']);
    const [privateKey, setPrivateKey] = useState('');

    const testMakeTransaction = () => {
      console.log('cookies: ', cookies);
        let privateKey = cookies.privateKey;//cookies.get('privateKey');
        const ec = new EC('ed25519');
        console.log('privateKey: ', privateKey);
        const key = ec.keyFromPrivate(privateKey, 'hex');
        console.log('key: ', key);
        const publicKey = key.getPublic('hex');
        console.log('publicKey: ', publicKey);
        makeTransaction(privateKey, publicKey, 3.14, key)
            .then(res => console.log(res))
            .catch(err => console.log(err));
    }

    const generatePrivateKey = () => {
        console.log('Generating private key...');
        const ec = new EC('ed25519');
        const key = ec.genKeyPair();
        const privateKey = key.getPrivate('hex');
        console.log('generated privateKey: ', privateKey);
        setPrivateKey(privateKey);
        setCookie('privateKey', privateKey, { path: '/' });

        // How you would get the key back, e.g. loading it from the cookie hex value to sign something,
        // or to load it from the cookie to generate the public key
        /*
        let key_again = ec.keyFromPrivate(privateKey, 'hex');
        console.log(key_again);
        */
        
        // Other example
        /*
        let ec = new EC('ed25519');
        console.log(ec);
        let key = ec.genKeyPair();
        console.log(key);
        let privateKey = key.getPrivate('hex');
        console.log("privateKey", privateKey);
        let publicKey = key.getPublic('hex');
        console.log("publicKey", publicKey);
        */
        
        // Signature example
        /*
        var msgHash = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ];
        var signature = key.sign(msgHash);
        */
    };

    return (
        <div>
            <a href="#">
            <img src="learncoin.png" className="logo" alt="LearnCoin Logo" height="30" width="170"/>
            </a>
            <button onClick={testMakeTransaction}>Test Transaction</button>
            <div className="login_modal">
            <h4>Register</h4>
            <button className="signup_btn" id='privateKeyButton' onClick={generatePrivateKey}>Sign up</button>
            <h5>There is no way to restore a forgotten key!</h5>
            {privateKey !== '' && <p>This is your private key: {privateKey}</p>}
            {privateKey !== '' && 
            <Link id = 'signinButton' to="/homepage">
                <button>Login using this private key</button>
            </Link>}
            </div>
            <img src="login_bg.jpg" className="login_bg"></img>
        </div>
    );
};

export default Signup;