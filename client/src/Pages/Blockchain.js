import { Link } from 'react-router-dom';

const Blockchain = () => {
    return (
        <div>
            <Link to='/homepage'>BACK</Link>
            <h1>Blockchain Viewer</h1>

            <div className="chain">
            
            {/* BLOCK */}
            <div className="block"> Proof of Work
                    <div className="pow">053091</div>
                    <div className="more_modal" title="Hello">
                    <img className="graphic" src="https://drive.google.com/uc?export=download&id=1bh1yecOYgaQrlQnnMnWAz5NreqeTuaiC" alt="More Info on Block"/>
                    </div>
            </div>

            {/* BLOCK */}
            <div className="block"> Proof of Work
                    <div className="pow">053091</div>
                    <div className="more_modal" title="Hello">
                    <img className="graphic" src="https://drive.google.com/uc?export=download&id=1bh1yecOYgaQrlQnnMnWAz5NreqeTuaiC" alt="More Info on Block"/>
                    </div>
            </div>

            </div>
        </div>
    )
};

export default Blockchain;