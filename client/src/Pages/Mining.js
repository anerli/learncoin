import { Link } from 'react-router-dom';

const Mining = () => {
    return (
        <div>
            <Link to='/homepage'>BACK</Link>
            <h1 align='center'>Mining 101!</h1>
            <br/>
            <h2>What is mining a cryptocurrency?</h2>
            <p className='mining'>
                &emsp; When mining a cryptocurrency, you are exchanging some of your computer's power in order to secure transactions with the cryptocurrency.
                In return for your computers computational power, you are rewarded with some of the crypto being mined!
                Many cryptos will then let you make transactions with other users.
                All transactions get encrypted for security and passed to all other miners on the cryptocurrency's network.
            </p>
            <h2>So you'd like to mine LearnCoin… Here's how you get started.</h2>
            <p className='mining'>
                First, you will need to set up the LearnCoin codebase which can be found <a href='https://git.ece.iastate.edu/lie/learncoin'>here</a>.
                <br/><br/>
                After the learn coin codebase is set up, you will need to navigate to the learncoin/server directory in your terminal: <br/>
                &emsp; 1) Find where you saved the codebase in your file explorer. <br/>
                &emsp; 2) Right click on the folder and choose 'Open in terminal'. <br/>
                &emsp; 3) Type 'cd server' to enter the server folder.
                <br/>
                From here, you should be able to see a file called server.py (type 'ls' to see everything inside the current folder).
                <br/><br/>
                Type 'Python3 server.py --neighbors coms-402-sd-23.class.las.iastate.edu --mine' to start mining!
                <br/><br/>
                'Python3 server.py' starts the LearnCoin server. <br/>
                '--neighors coms-402-sd-23.class.las.iastate.edu' is a tag that connects your computer to the LearnCoin network through one of the University servers that is constantly running LearnCoin.
                If this does not work, try one of the other servers by changing 23 to any other number from 23-27. <br/>
                '--mine' is a tag that tells your LearnCoin server to start mining.
            </p>
        </div>
    )
};

export default Mining;