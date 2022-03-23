let inputStyle = {
    visibility: 'hidden'
}

function createFunction() {
    console.log('clicked');
    document.getElementById('text').style.visibility = 'visible';
};

const Signup = () => {
    return (
        <div>
            <h1>Sign up for LearnCoin here!</h1>
            <button id='button' onClick={createFunction}>Sign up</button>
            <p>There is no way to restore a forgotten key!</p>
            <p id='text' style={inputStyle}>This is your private key: </p>

        </div>
    )
};

export default Signup;