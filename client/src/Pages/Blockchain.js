import { Link } from 'react-router-dom';
import Block from "../components/Block"

const Blockchain = () => {
    return (
        <div>
            <Link to='/homepage'>BACK</Link>
            <h1>Blockchain Viewer</h1>

            <div className="chain">
            <Block/>
            <Block/>
            <Block/>
            <Block/>
            <Block/>
            </div>
        </div>
    )
};

export default Blockchain;