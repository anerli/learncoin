import React, { useState } from 'react';
import { useCookies } from 'react-cookie';
import { makeTransaction } from "../logic/transactions";

function Send(props) {
    const [cookies] = useCookies(['privateKey']);
    const [errorMsg, setErrorMsg] = useState('');

    // function logWalletData() {
    //     console.log("amt: " + document.getElementById('amount').value);
    //     console.log("receiver: " + document.getElementById('receiver').value); 
    // }
    const triggerTransaction = async () => {
      const amount = parseFloat(document.getElementById('amount').value);
      const receiverPublicKey = document.getElementById('receiver').value;
      
      // TODO: handle guest mode
      const privateKey = cookies.privateKey;
      let resp = await makeTransaction(privateKey, receiverPublicKey, amount);
      console.log('resp:');
      console.log(resp);

      if (resp.status !== 200) {
        let msg = await resp.text();
        console.log(msg);
        //alert(msg);
        setErrorMsg('Error: ' + msg);
      } else {
        setErrorMsg('');
      }

      //alert("Transaction Pending");

      props.sendCallback();
    }

    return (
        <div>
            <p style={{color: 'red'}}>{errorMsg}</p>
            <button className="send_btn" onClick={triggerTransaction}>SEND</button>
        </div>
    );
}
 export default Send;