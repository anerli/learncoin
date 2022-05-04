import React, { useState, useEffect } from 'react';
import Send from "../components/Send";
import InfoModal from './InfoModal';
import {hexToFloat} from '../logic/conversions';

function TransactionForm(props) {
  const [pending, setPending] = useState([]);

  const onSend = async () => {
    //props.fetchBalanceCallback();
    fetchPending();
  }

  const fetchPending = async () => {
    console.log("fetching pending")
      // ! url TMP
      const SERV_URL = 'http://localhost:8000';
      console.log("props pubkey: ", props.pubkey);
      const response = await fetch(
        SERV_URL + '/transactions/pending/' + props.pubkey,
        {
          method: 'GET',
          mode: 'cors',
        }
      );
      let data = await response.json();
      console.log("Pending: ", data);

      console.log(data['transactions']);

      setPending(data['transactions']);
      // FIXME: Probably not good to reload whole page, should separate into balance component
      //setBalance(data.balance);
  };

  useEffect(() => {
    const interval = setInterval(() => {
      fetchPending();
    }, 5000);
    return () => clearInterval(interval);
  }, [pending]);

  return (
      <div>
          <h2 className="card_title">{props.text}</h2>
          <div className="float-container">
            <div className="float-child">
                <InfoModal text="This is your Wallet. Here, you can create transactions that will be broadcasted to the blockchain."/>
              <div className="card">
                  <div className="card_items">
                    <img className="graphic" src="https://drive.google.com/uc?export=download&id=1f8ItY1h0uVrjcaBBtbJ7Q69fzwNSrzd9" alt="LearnCoin logo"/>
                    <input id="amount" type="text" placeholder="Amount of LC to Send"></input>
                    <img className="graphic" src="https://drive.google.com/uc?export=download&id=1Km7Z7WEm5Ydd8i9BfNsMcMFWu4k3xRqH" alt="wallet icon"/>
                    <input id="receiver" type="text" placeholder="Public Key of Recipient"></input>
                    <Send sendCallback={onSend}/>
                  </div>
              </div>
            </div>

            <div className="float-child">
                <InfoModal text="These are pending transactions, that is, transactions which are recorded on the block currently being mined but have not been confirmed onto the chain yet."/>
              <div className="card" style={{height:"400px", overflowY: "scroll"}}>
                <h2>Pending:</h2>
                  <div className="card_items" style={{}}>
                      {pending.map(
                        (transaction) => (<div className="smolcard">
                          {transaction['id'] == '00000000000000000000000000000000' && <p>(BLOCK REWARD)</p>}
                          {/* <p>ID: {transaction['id']}</p> */}
                          <p>Sender: {transaction['sender']}</p>
                          <p>Receiver: {transaction['receiver']}</p>
                          <p>Amount: {hexToFloat(transaction['amount'])} LC</p>
                        </div>)
                      )}
                      {/* <p>{pending.toString()}</p> */}
                  </div>
              </div>
            </div>

          </div>

      </div>
    );
}

export default TransactionForm;