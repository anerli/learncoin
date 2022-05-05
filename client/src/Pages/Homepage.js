import TransactionForm from "../components/TransactionForm";
import Balance from "../components/Balance";

import React, { useState, useEffect } from 'react';
import { useCookies } from 'react-cookie';
import * as ed from '@noble/ed25519';
import InfoModal from "../components/InfoModal";
import {Link} from "react-router-dom";
//import {SRV_URL} from '../config';

const Homepage = () => {
    const [cookies, setCookie] = useCookies(['privateKey', 'node']);
    const [publicKey, setPublicKey] = useState('');
    const [balance, setBalance] = useState(0.0);
    const [privKeyHidden, setPrivKeyHidden] = useState(true);

    const fetchBalance = async () => {
      console.log("fetching balance")
      
      //console.log(cookies.node);
      const SRV_URL = "http://" + cookies.node;
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

    const updateNode = async () => {
      let host = document.getElementById('host').value;
      console.log(host);
      setCookie('node', host);
      window.location.reload();
    }

    useEffect(() => {
      const interval = setInterval(() => {
        fetchBalance();
      }, 500);
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
        if (!('node' in cookies)) {
          setCookie('node', 'coms-402-sd-23.class.las.iastate.edu'); // Default node
        }
        console.log('pub key: ', publicKey);
    });

    return (
        <div>
            <Link to='/'>LOG OUT</Link>
            <h1 style={{lineHeight:"0px"}}> LearnCoin  </h1>  

            {/* <img src="gear.png" width="30px"></img> */}
            {/* value="coms-402-sd-23.class.las.iastate.edu" */}
            <InfoModal style={{display:"block", margin: "10px"}} text="Here you can set the LearnCode server node that the wallet will communicate with to retrieve data and post transactions. 
              Some LearnCoin test servers you can try are:
              coms-402-sd-23.class.las.iastate.edu
              coms-402-sd-24.class.las.iastate.edu
              coms-402-sd-25.class.las.iastate.edu
              coms-402-sd-26.class.las.iastate.edu
              coms-402-sd-27.class.las.iastate.edu"/>
            <input style={{display:"inline", margin: "0 auto", width:"300px", textAlign: "Center"}} id="host" type="text" placeholder="Full Node Hostname / IP"></input>
            
            <button onClick={updateNode} style={{display:"inline", margin:"10px", padding:"10px"}} className="btn">Change Node Host (Current: {cookies.node})</button>
            <br/>
            <Balance text={balance.toFixed(4) + " LC"}/>
            
            <InfoModal className='pub_key_text' text="Your public key serves as your address, so this is how other users can identify you in transactions. You private key should always be kept secret, and is used for signing transactions to prove that you approved of them."/>
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
