import React from 'react';

function Module(props) {

    return (
        <div>
            <h2 className="card_title">{props.text}</h2>
            <div className="card">
                <div className="card_items">
                    <h3>AMOUNT</h3>
                    <h3>RECEIVER</h3>
                    <input type="text"></input>
                    <input type="text"></input>
                </div>
            </div>
        </div>
    );
}

export default Module;