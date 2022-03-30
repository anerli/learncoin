import Module from "../components/Module";
import Send from "../components/Send";
import Redirect1 from "../components/Redirect1";
import Redirect2 from "../components/Redirect2";

import React, { useState } from 'react';
import { useCookies } from 'react-cookie';
const EC = require('elliptic').ec;

const Homepage = () => {
    return (
        <div>
            <h1> LearnCoin </h1>
            <h2> Your public key: </h2> 
            <Module text="WALLET" />
            <Send />
            <img
                className="banner"
                src="https://drive.google.com/uc?export=download&id=113hYCr2JAlQ4Ym5RMujNNEQa2rLCqmh3"
                alt="homepage banner"
            />
            <Redirect1 />
            <Redirect2 />
        </div>
    );
}

export default Homepage;