function Send() {

    function logWalletData() {
        console.log("amt: " + document.getElementById('amount').value);
        console.log("receiver: " + document.getElementById('receiver').value); 
    }

    return (
        <div>
            <btn><img className="send_btn" onClick={logWalletData} src="https://drive.google.com/uc?export=download&id=1sfdEiJeWUXHutNSO_maOCMU0L0z07rRK" /></btn>
        </div>
    );
}
 export default Send;