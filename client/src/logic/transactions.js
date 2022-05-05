import sha256 from 'crypto-js/sha256';
import CryptoJS from 'crypto-js';
import { useCookies } from 'react-cookie';
import { floatToHex } from './conversions';
import * as ed from '@noble/ed25519';
//import {SRV_URL} from '../config';

function generateID() {
  // Generate a random ID, as hex
  return CryptoJS.enc.Hex.stringify(CryptoJS.lib.WordArray.random(16));
}

export async function makeTransaction(senderPrivateKey, receiverPublicKey, amount, SRV_URL) {
    /*
    sender: sender's public key as hex
    receiver: receiver's public key as hex
    amount: amount to send as float
    */
    const senderPublicKey = ed.utils.bytesToHex(await ed.getPublicKey(senderPrivateKey));

    const id = generateID();

    console.log('Making Transaction');
    console.log('id: ', id);
    console.log('sender priv: ', senderPrivateKey);
    console.log('sender pub: ', senderPublicKey);
    console.log('receiver pub: ', receiverPublicKey);
    console.log('amount: ', amount);

    console.log('amount hex: ', floatToHex(amount));

    const combinedHex = id + senderPublicKey + receiverPublicKey + floatToHex(amount);

    console.log('combined hex: ', combinedHex);
    
    const hash = sha256(CryptoJS.enc.Hex.parse(combinedHex));

    const hashHex = CryptoJS.enc.Hex.stringify(hash);

    console.log('hash hex: ', hashHex);

    const signature = ed.utils.bytesToHex(await ed.sign(hashHex, senderPrivateKey));

    console.log('signature: ', signature);

    console.log('valid? ', await ed.verify(signature, hashHex, senderPublicKey))

    //const SRV_URL = cookies.node;
    const response = await fetch(
      SRV_URL + '/transactions',
      {
        method: 'POST',
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          id: id,
          sender: senderPublicKey,
          receiver: receiverPublicKey,
          amount: floatToHex(amount),
          signature: signature
        })
      }
    );

    return response;
}
