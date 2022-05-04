import InfoModal from "../components/InfoModal";

function Balance(props) {
    return (
        <div>
           <div className="balance">
            {/* <InfoModal className='pub_key_text' text="Your public key is how other users can identify you in transactions."/> */}
            {/* TODO: Add info modal without making ugly */}
             {props.text}
          </div>
        </div>
    );
}

export default Balance;