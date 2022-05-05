import React, { useState } from 'react';
import { useCookies } from 'react-cookie';
import { makeTransaction } from "../logic/transactions";

function Send(props) {
    const [cookies] = useCookies(['privateKey', 'node']);
    const [errorMsg, setErrorMsg] = useState('');

    const triggerTransaction = async () => {
      const amount = parseFloat(document.getElementById('amount').value);
      const receiverPublicKey = document.getElementById('receiver').value;

      const privateKey = cookies.privateKey;

      const SRV_URL = "http://" + cookies.node;
      let resp = await makeTransaction(privateKey, receiverPublicKey, amount, SRV_URL);
      console.log('resp:');
      console.log(resp);

      if (resp.status !== 200) {
        let msg = await resp.text();
        console.log(msg);
        setErrorMsg('Error: ' + msg);
      } else {
        setErrorMsg('');
      }

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