import React from 'react';

function Module(props) {

    return (
        <div>
            <h2 className="card_title">{props.text}</h2>
            <div className="card">
                <div className="card_items">
                    <h3>AMOUNT</h3>
                    <h3>RECEIVER</h3>
                    <img className="graphic" src="https://drive.google.com/uc?export=download&id=1f8ItY1h0uVrjcaBBtbJ7Q69fzwNSrzd9" />
                    <input id="amount" type="text"></input>
                    <img className="graphic" src="https://drive.google.com/uc?export=download&id=1Km7Z7WEm5Ydd8i9BfNsMcMFWu4k3xRqH" />
                    <input id="receiver" type="text"></input>
                </div>
            </div>
        </div>
    );
}

export default Module;