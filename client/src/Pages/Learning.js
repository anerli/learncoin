import { Link } from 'react-router-dom';

const Learning = () => {
    return (
        <div>
            <Link to='/'>BACK</Link>
            <h1 align='center'>Crypto 101!</h1>
            <br/>
            <h2>What is mining in cryptocurrency?</h2>
            <p className='mining'>
                &emsp; When mining a cryptocurrency, you are exchanging some of your computer's power in order to secure transactions with the cryptocurrency.
                In return for your computers computational power, you are rewarded with some of the crypto being mined!
                Many cryptos will then let you make transactions with other users.
                All transactions get encrypted for security and passed to all other miners on the cryptocurrency's network.
            </p>
        </div>
    )
};

export default Learning;