import React from 'react';
import { Switch, Route } from 'react-router-dom';

import landingpage from './landingpage';
import About from './about';
import Stream from './stream';


const Main=() => (
    <Switch>
        <Route exact path ="/" component={landingpage} />
        <Route path="/About" component={About} />
        <Route path="/Stream" component={Stream} />
    </Switch>
)

export default Main;