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
            <btn><img className="send_btn" onClick={triggerTransaction} src="https://drive.google.com/uc?export=download&id=1sfdEiJeWUXHutNSO_maOCMU0L0z07rRK" alt="send icon"/></btn>
        </div>
    );
}
 export default Send;