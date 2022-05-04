import sha256 from 'crypto-js/sha256';
import CryptoJS from 'crypto-js';
import { floatToHex } from './conversions';
import * as ed from '@noble/ed25519';
//const EC = require('elliptic').ec;
import {SRV_URL} from '../config';

function generateID() {
  // Generate a random ID, as hex
  return CryptoJS.enc.Hex.stringify(CryptoJS.lib.WordArray.random(16));
}

export async function makeTransaction(senderPrivateKey, receiverPublicKey, amount) {
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

    // const senderBytes = CryptoJS.enc.Hex.parse(senderPublicKey);
    // const receiverBytes = CryptoJS.enc.Hex.parse(receiverPublicKey);
    console.log('amount hex: ', floatToHex(amount));
    //const amountBytes = CryptoJS.enc.Hex.parse(floatToHex(amount));

    //const combined = senderBytes + receiverBytes;
    const combinedHex = id + senderPublicKey + receiverPublicKey + floatToHex(amount);

    console.log('combined hex: ', combinedHex);

    // !tmp: dont include amt in hash
    //const hash = sha256(senderBytes + receiverBytes);// + amountBytes);
    
    const hash = sha256(CryptoJS.enc.Hex.parse(combinedHex));

    const hashHex = CryptoJS.enc.Hex.stringify(hash);

    console.log('hash hex: ', hashHex);

    const signature = ed.utils.bytesToHex(await ed.sign(hashHex, senderPrivateKey));

    console.log('signature: ', signature);

    console.log('valid? ', await ed.verify(signature, hashHex, senderPublicKey))

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
        // headers: {
        //   'Content-Type': 'application/json',
        //   'Access-Control-Allow-Origin': '*'
        // },
        // body: JSON.stringify({
        //   sender: senderPublicKey,
        //   receiver: receiverPublicKey,
        //   amount: floatToHex(amount),
        //   signature: signature
        // })
      }
    );

    return response;//await response.json();
}
