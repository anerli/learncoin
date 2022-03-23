import React, { useState } from 'react';
import { useCookies } from 'react-cookie';
const EC = require('elliptic').ec;
//import elliptic from 'elliptic'; 
//const EdDSA = require('elliptic').eddsa;
//const cookie = require('react-cookie');

let inputStyle = {
    visibility: 'hidden'
}

function createFunction() {
    console.log('clicked');
    document.getElementById('text').style.visibility = 'visible';
};



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
    }

    //generatePrivateKey();
    // https://crypto.stackexchange.com/questions/60383/what-is-the-difference-between-ecdsa-and-eddsa
    // Test
    
    // let ec = new EC('ed25519');
    // console.log(ec);
    // let key = ec.genKeyPair();
    // console.log(key);
    // let privateKey = key.getPrivate('hex');
    // console.log("privateKey", privateKey);
    // let publicKey = key.getPublic('hex');
    // console.log("publicKey", publicKey);

    // setCookie('privateKey', privateKey, { path: '/' });

    //var msgHash = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ];
    //var signature = key.sign(msgHash);

    //let key_again = ec.keyFromPublic(publicKey, 'hex');
    // How to get key back from hex
    // let key_again = ec.keyFromPrivate(privateKey, 'hex');
    // console.log(key_again);

    // E.g. if you got hex data from srv
    // nvm not a thing?
    //let key_again = ec.keyFromSecret(privateKey, 'hex');
    //let ec = new EdDSA('ed25519');
    //let key = ec.keyFromSecret('secret');
    //let key = ec.genKeyPair();
    
    //console.log(key_again);

    return (
        <div>
            <h1>Sign up for LearnCoin here!</h1>
            <button id='button' onClick={generatePrivateKey}>Sign up</button>
            <p>There is no way to restore a forgotten key!</p>
            {privateKey != '' && <p>This is your private key: {privateKey}</p>}

        </div>
    )
};

export default Signup;