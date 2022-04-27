import React from 'react';
import Send from "../components/Send";
import InfoModal from './InfoModal';

function Module(props) {

    return (
        <div>
            <h2 className="card_title">{props.text}</h2>
<<<<<<< HEAD
            <div class="float-container">
            <div class="float-child">
                <InfoModal text="This is your Wallet. Here, you can create transactions that will be broadcasted to the blockchain."/>
=======
        
            <div className="float-container">
            <div className="float-child">
>>>>>>> 09899306c1be7a16d8200d5ee95bf6c7175273aa
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
<<<<<<< HEAD
=======
            <div className="float-child">
            <div className="info_modal" title="So basically this is a thing that we can do... and so like the reason...">
                <img src="https://drive.google.com/uc?export=download&id=1A1ZS6cN2rRB2mDvqjICdxECrD8GxOA4R" alt="Question mark"/>
            </div>
            </div>

>>>>>>> 09899306c1be7a16d8200d5ee95bf6c7175273aa
            </div>
        
        
        </div>
    );
}

export default Module;