import { Link } from 'react-router-dom';

const Mining = () => {
    return (
        <div>
            <Link to='/homepage'>BACK</Link>
            <h1>Learn how to mine here!</h1>
            <h2>So you'd like to mine LearnCoin… Here's how you get started.</h2>
            <br></br>
After you have the learn coin codebase set up, you're going to want to navigate to the learncoin/server directory in your terminal. From here, you should be able to see a file called server.py. You're going to want to run this with the --mine tag, allowing you to mine learncoin. You'll also want to make sure to connect with another learncoin node. You can do this with the --neighbors tag. A couple of our university servers will be running and ready to connect with. The names of these servers are: coms-402-sd-23.class.las.iastate.edu. If this one doesn't work for some reason, you can change out the number 23 for any number in the range 23-27. 
So, an example of the command to run to start mining will be:
Python3 server.py --neighbors coms-402-sd-23.class.las.iastate.edu --mine

 <h2>How mining works:</h2>
 <br></br>
By mining learnCoin, what you're essentially doing is exchanging some of your own computer's power in order to secure transactions made with learnCoin. In return for your computing power, you'll be rewarded with some learnCoin! You can then use this learnCoin to make transactions with other learnCoin users, and those transactions will be encrypted and secured by all of the other miners on the learnCoin network! 
        </div>
    )
};

export default Mining;