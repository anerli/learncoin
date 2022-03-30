import sha256 from 'crypto-js/sha256';
import CryptoJS from 'crypto-js';
import { floatToHex } from './conversions';
const EC = require('elliptic').ec;

// ! temporary
const SERV_URL = 'http://localhost:8000';

export async function makeTransaction(sender, receiver, amount, privateKey) {
    /*
    sender: sender's public key as hex
    receiver: receiver's public key as hex
    amount: amount to send as float
    privateKey: sender's private key as hex
    */
    console.log('sender: ', sender);
    console.log('receiver: ', receiver);

    const ec = new EC('ed25519');
    const key = ec.keyFromPrivate(privateKey, 'hex');

    // convert sender, recipient hex values to bytes
    const senderBytes = CryptoJS.enc.Hex.parse(sender);
    const receiverBytes = CryptoJS.enc.Hex.parse(receiver);

    console.log('hex amount: ', floatToHex(amount));

    // convert amount float value to bytes
    const amountBytes = CryptoJS.enc.Hex.parse(floatToHex(amount));

    const hash = sha256(senderBytes + receiverBytes + amountBytes);
    const hash_hex = CryptoJS.enc.Hex.stringify(hash);

    const signature = key.sign(hash_hex);

    console.log('signature: ', signature);
    console.log('amount.toString(16): ', amount.toString(16));

    // return {
    //     sender,
    //     recipient,
    //     amount,
    //     signature: signature.toDER('hex')
    // }
    
    const response = await fetch(
      SERV_URL + '/transactions',
      {
        method: 'POST',
        mode: 'no-cors',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          sender,
          receiver,
          amount: floatToHex(amount),
          signature: signature.toDER('hex')
        })
      }
    );

    return response.json();
}