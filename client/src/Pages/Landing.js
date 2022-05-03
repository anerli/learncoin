import Redirect1 from "../components/Redirect1";
import Redirect2 from "../components/Redirect2";
import Redirect3 from "../components/Redirect3";
import Redirect4 from "../components/Redirect4";
import InfoModal from "../components/InfoModal";

import React from 'react';

const Landing = () => {

    return(
        <div>
            <h2 align='center'>
                Welcome to the LearnCoin website, your one stop for all things cryptocurrency!
                If you are new to cryptocurrency we recommend you start with 'Crypto 101'.
            </h2>
            <br/>
            <Redirect1 />
            <Redirect2 />
            <Redirect3 />
            <Redirect4 />
        </div>
    );
};

export default Landing;