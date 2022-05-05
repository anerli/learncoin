function InfoModal(props) {
    return (
      <div>
      <div className="info_modal" style={props.style} title={props.text}>
          <img alt="question mark" src="qmark.png"/>
      </div>
      </div>
    );
  }
  
  export default InfoModal;