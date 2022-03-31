import React, { useState } from 'react';
import { useCookies } from 'react-cookie';
import { Link } from 'react-router-dom';
import { makeTransaction } from "../logic/transactions";
import * as ed from '@noble/ed25519';
//const EC = require('elliptic').ec;



const Signup = () => {
    const [cookies, setCookie, removeCookie] = useCookies(['privateKey']);
    const [privateKey, setPrivateKey] = useState('');

    const testMakeTransaction = async () => {
        //const ec = new EC('ed25519');
        // let k = ec.genKeyPair();
        // console.log(k);
        // console.log(k.getPrivate('hex'));
        // //console.log(k.getPublic('hex'));
        // let pub = k.getPublic();
        // console.log('pub: ', pub);
        // console.log(pub.encode('hex'));
        //let k = ec.keyFromPublic('86a6ebcc659e5f5eefc095847b825684a2afb7fb4191cb8e3731fbdeef917849', 'hex');
        // let k = ec.keyFromPublic('04791b32552792dc08f6781692b78321a6f66652b70b3160b21248db6218ebed5530b70e4686d4b59991b6219989ba247b9a93284fef91561fa0bd9079846c3a7f', 'hex');
        // console.log('K: ', k);

        // const privateKey = ed.utils.randomPrivateKey();
        // console.log('privateKey', ed.utils.bytesToHex(privateKey));
        // ed.getPublicKey(privateKey).then((pubkey) => console.log('pubkey: ', ed.utils.bytesToHex(pubkey)));

        /*
        console.log('cookies: ', cookies);
        let privateKey = cookies.privateKey;//cookies.get('privateKey');
        
        console.log('privateKey: ', privateKey);
        const key = ec.keyFromPrivate(privateKey, 'hex');
        console.log('key: ', key);
        const publicKey = key.getPublic('hex');
        console.log('publicKey: ', publicKey);
        makeTransaction(privateKey, publicKey, 3.14, key)
            .then(res => console.log(res))
            .catch(err => console.log(err));
        */
        const privateKey = cookies.privateKey;
        // Sending to yourself? ig?
        const receiverPublicKey = ed.utils.bytesToHex(await ed.getPublicKey(privateKey));

        console.log('priv: ', privateKey);
        //console.log('pub: ', publicKey);
        await makeTransaction(privateKey, receiverPublicKey, 3.14);
    }
    

    const generatePrivateKey = () => {
        console.log('Generating private key...');
        // const ec = new EC('ed25519');
        // const key = ec.genKeyPair();
        // const privateKey = key.getPrivate('hex');

        const privKey = ed.utils.randomPrivateKey();
        const privKeyHex = ed.utils.bytesToHex(privKey);

        console.log('generated privateKey: ', privKeyHex);
        setPrivateKey(privKeyHex);
        setCookie('privateKey', privKeyHex, { path: '/' });

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