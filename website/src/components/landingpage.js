import React, {Component} from 'react';
import {Grid, Cell } from 'react-mdl';

class Landing extends Component {
    render() {
        return(
            <div style={{width: '100%', margin: 'auto'}}>
                <Grid className="landing-grid" >
                    <Cell col={12}>
                        <img 
                            src="http://localhost:8000/video_feed"
                            alt="some image here"
                            className="CCP-img"
                        />

                        <div className="banner-text">
                            <h1> iSecurity </h1>

                        <hr/>

                        </div>
                    </Cell>
                </Grid>



            </div>
        )
    }


}

export default Landing;