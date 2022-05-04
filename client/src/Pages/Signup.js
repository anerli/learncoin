import React, { useState } from 'react';
import { useCookies } from 'react-cookie';
import { Link } from 'react-router-dom';
import { makeTransaction } from "../logic/transactions";
import * as ed from '@noble/ed25519';

const Signup = () => {
    const [cookies, setCookie] = useCookies(['privateKey']);
    const [privateKey, setPrivateKey] = useState('');

    const generatePrivateKey = () => {
        console.log('Generating private key...');

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
            <div>
                <Link to='/login'>BACK</Link>
            </div>
            <div>
                <a href="#">
                <img src="learncoin.png" className="logo" alt="LearnCoin Logo" height="30" width="170"/>
                </a>
                <div className="login_modal">
                <h4>Register</h4>
                <button className="signup_btn" id='privateKeyButton' onClick={generatePrivateKey}>Sign up</button>
                <h5>There is no way to restore a forgotten key!</h5>
                {privateKey !== '' && <h4 id='privateKey'>This is your private key: {privateKey}</h4>}
                {privateKey !== '' && 
                <Link id = 'signinButton' to="/homepage">
                    <button className='login_btn'>Login using this private key</button>
                </Link>}
                </div>
                <img src="login_bg.jpg" className="login_bg" alt="login button"></img>
            </div>
        </div>
    );
};

export default Signup;