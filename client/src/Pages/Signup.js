import React, { useState } from 'react';
import { useCookies } from 'react-cookie';
import { Link } from 'react-router-dom';
const EC = require('elliptic').ec;

const Signup = () => {
    const [setCookie] = useCookies(['privateKey']);
    const [privateKey, setPrivateKey] = useState('');

    const generatePrivateKey = () => {
        console.log('Generating private key...');
        const ec = new EC('ed25519');
        const key = ec.genKeyPair();
        const privateKey = key.getPrivate('hex');
        setPrivateKey(privateKey);
        setCookie('privateKey', privateKey, { path: '/' });
    };

    return (
        <div>
            <div>
                <Link to='/'>BACK</Link>
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
                <img src="login_bg.jpg" className="login_bg"></img>
            </div>
        </div>
    );
};

export default Signup;