import React, {Component} from 'react';
import {Grid, Cell } from 'react-mdl';

class Landing extends Component {
    render() {
        return(
            <div style={{width: '100%', margin: 'auto'}}>
                <Grid className="landing-grid" >
                    <Cell col={12}>
                        {/* <img 
                            // src="https://static.spokanecity.org/photos/2015/09/19/infill-housing-option-1/16x10/Full/infill-housing-option-1.jpg"
                            alt="some image here"
                            className="CCP-img"
                        /> */}

                        <div className="banner-text">
                            <h1> HI - Security </h1>

                        <hr/>

                        </div>
                    </Cell>
                </Grid>



            </div>
        )
    }


}

export default Landing;