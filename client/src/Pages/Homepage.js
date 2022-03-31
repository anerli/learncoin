import Module from "../components/Module";
import Send from "../components/Send";
import Redirect1 from "../components/Redirect1";
import Redirect2 from "../components/Redirect2";

import React, { useState, useEffect } from 'react';
import { useCookies } from 'react-cookie';
import * as ed from '@noble/ed25519';

const Homepage = () => {
    const [cookies] = useCookies(['privateKey']);
    const [publicKey, setPublicKey] = useState('');

    useEffect(() => {
        if ('privateKey' in cookies) {
            ed.getPublicKey(cookies.privateKey).then(
              (publicKey) => {
                let hexPublicKey = ed.utils.bytesToHex(publicKey);
                setPublicKey(hexPublicKey);
              }
            );
        }
        console.log('pub key: ', publicKey);
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
