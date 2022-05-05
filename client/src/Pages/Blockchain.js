import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useCookies } from 'react-cookie';
import {hexToFloat} from '../logic/conversions';

const Blockchain = () => {
  const [cookies, setCookie] = useCookies(['node']);
  const [blocks, setBlocks] = useState([]);


  const fetchChain = async () => {
    const SRV_URL = "http://" + cookies.node;
      console.log( SRV_URL + '/transactions/balance/');
      const response = await fetch(
        SRV_URL + '/chain/',
        {
          method: 'GET',
          mode: 'cors',
        }
      );
      let data = await response.json();
      console.log(data);
      let _blocks = data.blocks;
      _blocks.reverse();
      setBlocks(_blocks);
  }

  // useEffect(() => {
  //   fetchChain();
  // }, [blocks]);
  useEffect(() => {
    const interval = setInterval(() => {
      fetchChain();
    }, 500);
    return () => clearInterval(interval);
  }, [blocks]);

  useEffect(() => {
    if (!('node' in cookies)) {
      setCookie('node', 'coms-402-sd-23.class.las.iastate.edu'); // Default node
    }
  });


  return (<div>
    <Link to='/'>BACK</Link>
    <h1>Blockchain Viewer</h1>

    {blocks.map(
      (block, i) => (<div style={{maxWidth: "1100px",}}><div className="card" style={{padding: "16px", paddingTop:"0px"}}>
        <h1>Block {blocks.length - i - 1} {i == blocks.length - 1 && "(GENESIS BLOCK)"}</h1>
        <h2>Proof:</h2>
        <p>{block.header.proof}</p>
        <h2>Previous Block Hash:</h2>
        <p>{block.header.previous_block_hash}</p>

        <h2>Transactions:</h2>
        <div className="card" style={{height:"400px", overflowY: "scroll"}}>
          <div className="card_items" style={{}}>
              {block.transactions.map(
                (transaction) => (<div className="smolcard">
                  {transaction['id'] === '00000000000000000000000000000000' && <p>(BLOCK REWARD)</p>}
                  <p>Sender: {transaction['sender']}</p>
                  <p>Receiver: {transaction['receiver']}</p>
                  <p>Amount: {hexToFloat(transaction['amount'])} LC</p>
                </div>)
              )}
          </div>
        </div>
        
      </div>{i != blocks.length - 1 && <img src="chain.png" style={{width:"100px", display: "block", marginLeft: "auto", marginRight: "auto", marginTop:"10px"}}></img>}</div>)
    )}

  </div>);
};

export default Blockchain;