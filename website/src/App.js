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
            <Navigation>
                <Link to="/">Home</Link>
                <Link to="/">Signup</Link>
                <Link to="/about">About</Link>
                <Link to="/login"> Login </Link>
                <Link to="/gallery"> Gallery </Link>
            </Navigation>
        </Header>
        <Drawer title="Contents (or whatever)">
            <Navigation>
              <Link to="/">Home</Link>
              <Link to="/stream">Stream</Link>
              <Link to="/about">About</Link>
              <a href="/">Link</a>
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
