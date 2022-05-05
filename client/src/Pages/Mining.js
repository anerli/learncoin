import { Link } from 'react-router-dom';

const Mining = () => {
    return (
        <div>
            <Link to='/'>BACK</Link>
            <h1 align='center'>Mining LearnCoin!</h1>
            <br/>
            <h2>So you'd like to mine LearnCoin… Here's how you get started.</h2>
            <p className='mining'>
                This page will guide you through the process of setting up a LearnCoin server node. This is somewhat technical, so some experience
                with Python and your operating system's shell is recommended but not required.<br/><br/>

                Note: Setting up a server is not necessary to start a LearnCoin wallet and make transactions! To do that, just click <a href='/login'>here</a>! <br/>
                Note: If you would like to understand more about what mining actually means, please see the <a href='/learning'>Crypto 101</a> page! <br/>
            </p>
            <h2>Requirements</h2>
            <p className='mining'>
              - Python 3.6 or above. You can download Python <a target="blank" href="https://www.python.org/">here</a>. For the remainder of this guide, we assume Python is installed and on your PATH. <br/>
              - Pip, Python's package manager. This comes installed with Python. <br/>
              - Git, the version manager. More information regarding how to install git can be found <a target="blank" href="https://git-scm.com/">here</a>.
            </p>

            <h2>Video Version</h2>
            <p className='mining'>
              If you would prefer a video tutorial:
            </p>
            <iframe width="1024" height="580"
            src="https://www.youtube.com/embed/xnv272ybcoQ">
            </iframe>

            <h2>Setup</h2>
            <p className='mining'>

                First, you will need to clone the LearnCoin codebase which can be found <a target="blank" href='https://git.ece.iastate.edu/lie/learncoin'>here</a>.<br/>
                
                Command:<br/> 
                &emsp; `git clone https://git.ece.iastate.edu/lie/learncoin.git`

                <br/><br/>

                In the `server` directory, the `server.py` files is the main entry point for running the LearnCoin server.<br/>
                However, first you need to make sure all Python dependencies are installed:<br/>
                Command (assuming you are in the server directory):<br/>
                &emsp; `pip install -r requirements.txt`<br/><br/>

                Now you can run the server script simply with:<br/>
                &emsp; `python server.py`<br/>
                (assuming `python` is the command for your Python 3 installation).<br/><br/>

                You should see the server boot up, and you will get a few server logs.<br/>
                However, there are several arguments that can be passed for extended functionality.<br/>
                The most important of which might be the `-n` argument, which allows you to pass a neighbor node URL, so that you can connect
                to an existing network.<br/><br/>
                LearnCoin servers are hosted at `coms-402-sd-23.class.las.iastate.edu` and run on port 80, so to start a server and connected to this network, use the command:<br/>
                &emsp; `python server.py -n coms-402-sd-23.class.las.iastate.edu:80`<br/><br/>

                Additionally `--mine` is an argument that tells your LearnCoin server to start mining, as opposed to just receiving and verifying transactions. 
                So if you actually want to mine, make sure to pass this argument! <br/><br/>

                The argument `-k [key]` will allow you to enter a specific private key instead of generating a new one for you. That way you can use
                an existing private key from the wallet interface to have your rewards sent to!<br/><br/>

                Use `python server.py -h` to get additional information on other arguments.<br/><br/>

                Happy mining!
            </p>
        </div>
    )
};

export default Mining;