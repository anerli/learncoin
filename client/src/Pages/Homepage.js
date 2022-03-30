import Module from "../components/Module";
import Send from "../components/Send";
import Redirect1 from "../components/Redirect1";
import Redirect2 from "../components/Redirect2";

import React, { useState, useEffect } from 'react';
import { useCookies } from 'react-cookie';
const EC = require('elliptic').ec;

const Homepage = () => {
    const [cookies] = useCookies(['privateKey']);
    const [publicKey, setPublicKey] = useState('');

    useEffect(() => {
        const ec = new EC('ed25519');
        let pkey = cookies.privateKey;
        let key = ec.keyFromPrivate(pkey, 'hex');
        let hexPublicKey = key.getPublic('hex');
        setPublicKey(hexPublicKey);
        console.log('pub key: ', hexPublicKey);
    });

    return (
        <div>
            <h1> LearnCoin </h1>
            {publicKey !== '' && <h2 className='public_key'> Your public key: {publicKey}</h2>}
            <Module text="WALLET" />
            <Send />
            <img
                className="banner"
                src="https://drive.google.com/uc?export=download&id=113hYCr2JAlQ4Ym5RMujNNEQa2rLCqmh3"
                alt="homepage banner"
            />
            <Redirect1 />
            <Redirect2 />
        </div>
    );
}

export default Homepage;
