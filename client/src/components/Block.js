function Block(props) {
    return (
        <div>
            <div className="block"> Proof of Work
                    <div className="pow">Hello</div>
                    <div className="more_modal" text={props.text}>
                    <img className="graphic" src="https://drive.google.com/uc?export=download&id=1bh1yecOYgaQrlQnnMnWAz5NreqeTuaiC" alt="More Info on Block"/>
                    </div>
            </div>
        </div>
    );
}
export default Block