import React, {Component} from 'react';
import './login.css';

export default class transcript extends Component {
    constructor(props) {    super(props)
    this.file = './words.txt';
    var currentLines = require("./words.json")
    this.state = {time: Date.now(),lines: currentLines.lines  };

    console.log(currentLines);
    }

    
    render() {
        return (
        <div className="transcript">
            {this.state.lines.map(line => <div> {line} </div>)}
        </div>
        );
    }

    componentDidMount() {
        this.interval = setInterval(() => this.setState({ time: Date.now() }), 10000);
    }
    componentWillUnmount() {
        clearInterval(this.interval);
    }
    
}
