import Module from "../components/Module";
import Balance from "../components/Balance";
import Redirect1 from "../components/Redirect1";
import Redirect2 from "../components/Redirect2";

import React, { useState, useEffect } from 'react';
import { useCookies } from 'react-cookie';
import * as ed from '@noble/ed25519';
import InfoModal from "../components/InfoModal";

const Homepage = () => {
    const [cookies] = useCookies(['privateKey']);
    const [publicKey, setPublicKey] = useState('');
    const [balance, setBalance] = useState(0.0);

    const fetchBalance = async () => {
      // ! url TMP
      const SERV_URL = 'http://localhost:8000';
      const response = await fetch(
        SERV_URL + '/transactions/balance/' + publicKey,
        {
          method: 'GET',
          mode: 'cors',
        }
      );
      let data = await response.json();
      setBalance(data.balance);
    }

    // useEffect(() => {
    //   fetchBalance();
    // }, [publicKey]);

    useEffect(() => {
      const interval = setInterval(() => {
        fetchBalance();
      }, 1000);
      return () => clearInterval(interval);
    }, []);
    

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
            <Balance text={balance.toFixed(4) + " LC"}/>
            <InfoModal className='pub_key_text' text="Your public key is how other users can identify you in transactions."/>
            {publicKey !== '' &&
                <h2 className='public_key'>
                Your public key: {publicKey}
            </h2>}
            <Module/>
            <Redirect1 />
            <Redirect2 />
        </div>
    );
}

export default Homepage;
