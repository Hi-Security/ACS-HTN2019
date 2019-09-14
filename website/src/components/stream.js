import React, {Component} from 'react';
import './stream.css';

class Stream extends Component {
    render() {
        return(
            <div className="Stream">
            <h1 className="s">
                    Stream
            </h1>
            <img src="http://localhost:8000/video_feed"></img>
            </div>
            
        )
    }


}

export default Stream;