import { Link } from 'react-router-dom';

const Blockchain = () => {
    return (
        <div>
            <Link to='/homepage'>BACK</Link>
            <h1>Blockchain Viewer</h1>

            <div className="chain">
                <div className="block">
                    <div className="pow"></div>
                    <button type="button"></button>
                </div>
            </div>
        </div>
    )
};

export default Blockchain;