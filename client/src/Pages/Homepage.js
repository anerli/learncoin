import TransactionForm from "../components/TransactionForm";
import Balance from "../components/Balance";

import React, { useState, useEffect } from 'react';
import { useCookies } from 'react-cookie';
import * as ed from '@noble/ed25519';
import InfoModal from "../components/InfoModal";
import {Link} from "react-router-dom";

const Homepage = () => {
    const [cookies] = useCookies(['privateKey']);
    const [publicKey, setPublicKey] = useState('');
    const [balance, setBalance] = useState(0.0);

    const fetchBalance = async () => {
      console.log("fetching balance")
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
      console.log(data);
      // FIXME: Probably not good to reload whole page, should separate into balance component
      setBalance(data.balance);
    }

    // useEffect(() => {
    //   fetchBalance();
    // }, [publicKey]);

    useEffect(() => {
      const interval = setInterval(() => {
        fetchBalance();
      }, 5000);
      return () => clearInterval(interval);
    }, [publicKey]);
    

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
            <Link to='/'>LOG OUT</Link>
            <h1> LearnCoin </h1>
            <Balance text={balance.toFixed(4) + " LC"}/>
            <InfoModal className='pub_key_text' text="Your public key is how other users can identify you in transactions."/>
            {publicKey !== '' &&
                <h2 className='public_key'>
                Your public key: {publicKey}
            </h2>}
            <TransactionForm fetchBalanceCallback={fetchBalance}/>
        </div>
    );
}

export default Homepage;
