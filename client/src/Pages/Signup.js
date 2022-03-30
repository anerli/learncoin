import React, { useState } from 'react';
import { useCookies } from 'react-cookie';
import { Link } from 'react-router-dom';
const EC = require('elliptic').ec;

const Signup = () => {
    const [cookies, setCookie, removeCookie] = useCookies(['privateKey']);
    const [privateKey, setPrivateKey] = useState('');

    const generatePrivateKey = () => {
        console.log('Generating private key...');
        const ec = new EC('ed25519');
        const key = ec.genKeyPair();
        const privateKey = key.getPrivate('hex');
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
            <h1>Sign up for LearnCoin here!</h1>
            <button id='privateKeyButton' onClick={generatePrivateKey}>Sign up</button>
            <p>There is no way to restore a forgotten key!</p>
            {privateKey !== '' && <p>This is your private key: {privateKey}</p>}
            {privateKey !== '' && 
            <Link id = 'signinButton' to="/homepage">
                <button>Login using this private key</button>
            </Link>}

        </div>
    );
};

export default Signup;