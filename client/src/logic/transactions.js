import sha256 from 'crypto-js/sha256';
import CryptoJS from 'crypto-js';
import { floatToHex } from './conversions';
import * as ed from '@noble/ed25519';
//const EC = require('elliptic').ec;

// ! temporary
const SERV_URL = 'http://localhost:8000';

export async function makeTransaction(senderPrivateKey, receiverPublicKey, amount) {
    /*
    sender: sender's public key as hex
    receiver: receiver's public key as hex
    amount: amount to send as float
    */
    const senderPublicKey = ed.utils.bytesToHex(await ed.getPublicKey(senderPrivateKey));

    console.log('Making Transaction');
    console.log('sender priv: ', senderPrivateKey);
    console.log('sender pub: ', senderPublicKey);
    console.log('receiver pub: ', receiverPublicKey);
    console.log('amount: ', amount);

    // const senderBytes = CryptoJS.enc.Hex.parse(senderPublicKey);
    // const receiverBytes = CryptoJS.enc.Hex.parse(receiverPublicKey);
    const amountBytes = CryptoJS.enc.Hex.parse(floatToHex(amount));

    //const combined = senderBytes + receiverBytes;
    const combinedHex = senderPublicKey + receiverPublicKey;

    console.log('combined hex: ', combinedHex);

    // !tmp: dont include amt in hash
    //const hash = sha256(senderBytes + receiverBytes);// + amountBytes);
    
    const hash = sha256(combinedHex);

    const hashHex = CryptoJS.enc.Hex.stringify(hash);

    console.log('hash hex: ', hashHex);

    const signature = ed.utils.bytesToHex(await ed.sign(hashHex, senderPrivateKey));

    console.log('signature: ', signature);

    console.log('valid? ', await ed.verify(signature, hashHex, senderPublicKey))

    // const signature = key.sign(hash_hex);

    // console.log('signature: ', signature);
    // console.log('amount.toString(16): ', amount.toString(16));
    
    const response = await fetch(
      SERV_URL + '/transactions',
      {
        method: 'POST',
        mode: 'no-cors',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          sender: senderPublicKey,
          receiver: receiverPublicKey,
          amount: floatToHex(amount),
          signature: signature
        })
      }
    );

    // return response.json();
}

// export async function makeTransaction(sender, receiver, amount, privateKey) {
//     /*
//     sender: sender's public key as hex
//     receiver: receiver's public key as hex
//     amount: amount to send as float
//     privateKey: sender's private key as hex
//     */
//     console.log('sender: ', sender);
//     console.log('receiver: ', receiver);

//     const ec = new EC('ed25519');
//     const key = ec.keyFromPrivate(privateKey, 'hex');

//     // convert sender, recipient hex values to bytes
//     const senderBytes = CryptoJS.enc.Hex.parse(sender);
//     const receiverBytes = CryptoJS.enc.Hex.parse(receiver);

//     console.log('hex amount: ', floatToHex(amount));

//     // convert amount float value to bytes
//     const amountBytes = CryptoJS.enc.Hex.parse(floatToHex(amount));

//     const hash = sha256(senderBytes + receiverBytes + amountBytes);
//     const hash_hex = CryptoJS.enc.Hex.stringify(hash);

//     const signature = key.sign(hash_hex);

//     console.log('signature: ', signature);
//     console.log('amount.toString(16): ', amount.toString(16));

//     // return {
//     //     sender,
//     //     recipient,
//     //     amount,
//     //     signature: signature.toDER('hex')
//     // }
    
//     const response = await fetch(
//       SERV_URL + '/transactions',
//       {
//         method: 'POST',
//         mode: 'no-cors',
//         headers: {
//           'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({
//           sender,
//           receiver,
//           amount: floatToHex(amount),
//           signature: signature.toDER('hex')
//         })
//       }
//     );

//     return response.json();
// }