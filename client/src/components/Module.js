import React from 'react';
import Send from "../components/Send";
import InfoModal from './InfoModal';

function Module(props) {

    return (
        <div>
            <h2 className="card_title">{props.text}</h2>
            <div class="float-container">
            <div class="float-child">
                <InfoModal text="This is your Wallet. Here, you can create transactions that will be broadcasted to the blockchain."/>
            <div className="card">
                <div className="card_items">
                    <img className="graphic" src="https://drive.google.com/uc?export=download&id=1f8ItY1h0uVrjcaBBtbJ7Q69fzwNSrzd9" alt="LearnCoin logo"/>
                    <input id="amount" type="text" placeholder="Amount of LC to Send"></input>
                    <img className="graphic" src="https://drive.google.com/uc?export=download&id=1Km7Z7WEm5Ydd8i9BfNsMcMFWu4k3xRqH" alt="wallet icon"/>
                    <input id="receiver" type="text" placeholder="Private Address of Recipient"></input>
                   <Send />
                </div>
            </div>
            </div>
            </div>
        
        
        </div>
    );
}

export default Module;