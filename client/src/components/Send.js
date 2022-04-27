import { useCookies } from 'react-cookie';
import { makeTransaction } from "../logic/transactions";

function Send() {
    const [cookies, setCookie] = useCookies(['privateKey']);
    // function logWalletData() {
    //     console.log("amt: " + document.getElementById('amount').value);
    //     console.log("receiver: " + document.getElementById('receiver').value); 
    // }

    const triggerTransaction = async () => {
      const amount = parseFloat(document.getElementById('amount').value);
      const receiverPublicKey = document.getElementById('receiver').value;
      
      // TODO: handle guest mode
      const privateKey = cookies.privateKey;
      await makeTransaction(privateKey, receiverPublicKey, amount);
    }

    return (
        <div>
            <button className="send_btn" onClick={triggerTransaction}>SEND</button>
        </div>
    );
}
 export default Send;