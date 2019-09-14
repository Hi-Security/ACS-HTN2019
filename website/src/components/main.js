import React from 'react';
import { Switch, Route } from 'react-router-dom';

import landingpage from './landingpage';
import About from './about';
import Stream from './stream';
import login from './login';
import Gallery from './gallery';


const Main=() => (
    <Switch>
        <Route exact path ="/" component={landingpage} />
        <Route path="/login" component={login} />
        <Route path="/about" component={About} />
        <Route path="/stream" component={Stream} />
        <Route path="/gallery" component={Gallery}/>
    </Switch>
)

export default Main;