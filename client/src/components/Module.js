import React from 'react';

function Module(props) {

    return (
        <div>
            <h2 className="card_title">{props.text}</h2>
        
            <div class="float-container">
            <div class="float-child">
            <div className="card">
                <div className="card_items">
                    <h3>AMOUNT</h3>
                    <h3>RECEIVER</h3>
                    <img className="graphic" src="https://drive.google.com/uc?export=download&id=1f8ItY1h0uVrjcaBBtbJ7Q69fzwNSrzd9" alt="LearnCoin logo"/>
                    <input id="amount" type="text"></input>
                    <img className="graphic" src="https://drive.google.com/uc?export=download&id=1Km7Z7WEm5Ydd8i9BfNsMcMFWu4k3xRqH" alt="wallet icon"/>
                    <input id="receiver" type="text"></input>
                </div>
            </div>
            </div>
            <div className="float-child">
            <div class="info_modal" title="So basically this is a thing that we can do... and so like the reason...">
                <img src="https://drive.google.com/uc?export=download&id=1A1ZS6cN2rRB2mDvqjICdxECrD8GxOA4R"/>
            </div>
            </div>

            </div>
        
        
        </div>
    );
}

export default Module;