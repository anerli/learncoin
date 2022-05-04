import TransactionForm from "../components/TransactionForm";
import Balance from "../components/Balance";

import React, { useState, useEffect } from 'react';
import { useCookies } from 'react-cookie';
import * as ed from '@noble/ed25519';
import InfoModal from "../components/InfoModal";
import {Link} from "react-router-dom";
import {SRV_URL} from '../config';

const Homepage = () => {
    const [cookies, setPrivateKey] = useCookies(['privateKey']);
    const [publicKey, setPublicKey] = useState('');
    const [balance, setBalance] = useState(0.0);
    const [privKeyHidden, setPrivKeyHidden] = useState(true);

    const fetchBalance = async () => {
      console.log("fetching balance")

      console.log( SRV_URL + '/transactions/balance/');
      const response = await fetch(
        SRV_URL + '/transactions/balance/' + publicKey,
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
                Your public key: &nbsp;{publicKey} 
              </h2>
            }
            {
              'privateKey' in cookies &&
              <div>
              <h2>
                Your private key: {privKeyHidden ? '****************************************************************' : cookies.privateKey} 
              </h2>
              <button onClick={()=>{setPrivKeyHidden(!privKeyHidden)}} style={{display:"inline", margin:"0px"}} className="send_btn">{privKeyHidden ? "SHOW" : "HIDE"}</button>
              </div>
            }
            <TransactionForm fetchBalanceCallback={fetchBalance} pubkey={publicKey}/>
            
        </div>
    );
}

export default Homepage;
