import React, { useState } from 'react';
import Send from "../components/Send";
import InfoModal from './InfoModal';

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
      const response = await fetch(
        SERV_URL + '/transactions/pending/' + props.publicKey,
        {
          method: 'GET',
          mode: 'cors',
        }
      );
      let data = await response.json();
      console.log("Pending: ", data);
      // FIXME: Probably not good to reload whole page, should separate into balance component
      //setBalance(data.balance);
  };

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
                <InfoModal text="These are pending transactions."/>
              <div className="card">
                  <div className="card_items">
                      
                  </div>
              </div>
            </div>

          </div>

      </div>
    );
}

export default TransactionForm;