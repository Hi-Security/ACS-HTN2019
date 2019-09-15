import React, { Component } from 'react';
import './App.css';
import { Layout, Header, Navigation, Drawer, Content } from 'react-mdl';
import Main from './components/main';
import { Link } from 'react-router-dom';

class App extends Component {
  render() {
    return (
      <div className="demo-big-content">
    <Layout>
    
        <Header className="header-color" title=" " scroll>
        <img className = "logo" src="https://i.imgur.com/aZkQSkn.png"></img>
            <Navigation>
                <Link to="/">Home</Link>
                <Link to="/transcript">Transcript</Link>
                <Link to="/gallery"> Gallery </Link>
                <Link to="/">Signup</Link>
                <Link to="/login"> Login </Link>
            </Navigation>
        </Header>
        
        <Drawer title="Available Streams">
            <Navigation>
              <Link to="/stream">Stream 1</Link>
              <Link to="/stream2">Stream 2</Link>
              <Link to="/">Stream 3</Link>
              <a href="/">Stream 4</a>
            </Navigation>
        </Drawer>
        <Content>
            <div className="page-content" />
            <Main></Main>
        </Content>
    </Layout>
</div>
    );
  }
}

export default App;
