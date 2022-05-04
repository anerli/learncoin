import { Link } from 'react-router-dom';

const Learning = () => {
    return (
        <div>
            <Link to='/'>BACK</Link>
            <h1 align='center'>Crypto 101!</h1>
            <br/>
            <h2>What is a Cryptocurrency?</h2>
            <p className='learning'>
              A cryptocurrency is a decentralized system of web servers which work to agree on a common list of transactions between different users.
              Decentralized means that no particular server is in charge of the network. We call each server in such a network a "node".
              The list of transactions simply represents each exchange of the cryptocurrency from
              one user to another. Each user has an address which identifies them, so that others know where to send the cryptocurrency. However, in order to agree on
              a common list of transactions while preventing malicious users from inserting false transactions or removing valid ones, we use two key mechanisms: digital signatures and blockchain.
            </p>

            <h2>What are Digital Signatures?</h2>
            <p className='learning'>
              Digital signatures are cryptographic mechanisms for verifying that a particular user approved of a certain action. In our case, we would like to verify that anyone
              who sends a transaction actually wanted to do so, and that it is not an attacker forging the transaction. We implement this by using what's called a keypair, which
              consists of a public and private key. The private key is never shared with anyone else, whereas the public key can be shared freely. We can "sign" any arbitrary data
              using our private key, and any other party can verify that we signed that data by checking with our public key. In our case, we would like to sign all the data
              associated with any transaction we make so that it can be proven to be legit.
            </p>

            <h2>What is a Blockchain?</h2>
            <p className='learning'>
              A blockchain is a chain of data objects, which we call blocks, binded together with cryptographic proofs. Each block can contain whatever information we want. In our case,
              we would like each block to contain some transactions. That way, combining each list of transactions for each of our blocks in the chain makes the total list of transactions.
              But how are they "chained" together? And why do we need to do this anyway?
            </p>

            <p className='learning'>
              The purpose of chaining together blocks this way is in order to prevent any one party from modifying the chain excessively, for example removing many transactions.
              Our digital signature mechanism allows us to verify that provided transactions are valid, but does not prevent nodes from removing transactions.
              Consider, for example, someone making a purchase with a cryptocurrency. They sign the transaction, and it is added to the network. 
              If the network does not have sufficient mechanisms for preventing transaction removal, then this person could distribute a fake list of transactions
              which does not include their transfer - thus gaining back the money they spent.
            </p>

            <p className='learning'>
              To prevent this, we require proof that each block is "valid". But how do we decide which blocks are valid and which aren't? We can use what's called a consensus algorithm for this,
              which is an algorithm designed to agree on something in a decentralized system. In our case, we would like to agree on which blocks are valid and which aren't.
            </p>

            <p className='learning'>
              Proof of Work is one such consensus algorithm. For this algorithm, each block needs to be "mined" by solving a cryptographic puzzle involving the block's data,
              which requires computational resources. A solution to one of these puzzles is called a "proof". Additionally, we base the puzzle on the previously mined block's data
              as well, thus forming a chain. By organizing this as a chain, the "strength" of the chain increases over time as more and more proofs are added.
              Now, we simply have nodes agree to replace their own chain with a longer one whenever a block is mined. So the longest chain is distributed amongst the nodes in the network.
              While in theory a malicious party could add false transactions to a block and if they get lucky and mine it, it could be distributed. However, if these transactions
              have invalid signatures then the other nodes will simply reject this chain. So the worst a malicious party can do is fail to include valid transactions.
              Additionally, it becomes impossible to remove blocks since for every block removed, in order to gain back the length and become the dominant chain, one would
              have to prove multiple blocks which is incredibly difficult since this requires computational power greater than the rest of the network combined.
            </p>

            <h2>What is Mining?</h2>
            <p className='mining'>
                When mining a cryptocurrency, you are exchanging some of your computer's power in order to secure transactions with the cryptocurrency.
                In return for your computation power, every time you mine a block, a special transaction is added which rewards you with some of the cryptocurrency!
                This incentivizes people to host nodes which support the network and secures the blockchain data. <br/>

                If you would like to try mining yourself on the LearnCoin network, click <a href='/mining'>here</a>!
                {/* In return for your computers computational power, you are rewarded with some of the crypto being mined!  */}

                {/* Many cryptos will then let you make transactions with other users.
                All transactions get encrypted for security and passed to all other miners on the cryptocurrency's network. */}
            </p>

            <h2>What is LearnCoin?</h2>
            <p className='learning'>
              LearnCoin is a cryptocurrency implementation meant to be as simple as possible while remaining secure. LearnCoin is written in Python, a relatively easy programming language
              to understand, and is built only using the fundamental cryptocurrency mechanisms needed for a secure system of transactions. Most cryptocurrencies are highly concerned
              with efficiency - however increasing efficiency often requires additional complicated algorithms. By removing the worry of efficiency, LearnCoin can remain
              minimal, which can allow programmers interested in learning about the inner workings of a cryptocurrency to better understand the basics.
            </p>

            <p className='learning'>
              In addition to acting as a clean codebase for interested programmers, LearnCoin also provides a <a href='/login'>simple wallet interface</a> along with information (like this page!) to
              help people understand the various mechanisms. Around this site, you will see question mark icons which you can hover over to reveal additional information about
              different components!
            </p>
        </div>
    )
};

export default Learning;