const crypto = require('crypto');

let inputStyle = {
    visibility: 'hidden'
}

function createFunction() {
    console.log('clicked');
    document.getElementById('text').style.visibility = 'visible';
    crypto.generateKeyPair(
        'ed25519',
        {
            publicKeyEncoding: {
                type: 'spki',
                format: 'der'
            },
            privateKeyEncoding: {
                type: 'pkcs8',
                format: 'der'
            }
        },
        (err, publicKey, privateKey) => {
            console.log("Public key:", publicKey.toString('hex'));
            console.log("Private key:", privateKey.toString('hex'));
        }
    );
};

const Signup = () => {
    return (
        <div>
            <h1>Sign up for Learncoin here!</h1>
            <button id='button' onClick={createFunction}>Sign up</button>
            <p>There is no way to restore a forgotten key!</p>
            <p id='text' style={inputStyle}>This is your private key: </p>

        </div>
    )
};

export default Signup;