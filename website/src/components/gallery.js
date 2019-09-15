import React, { Component } from 'react'
import Button from '@material-ui/core/Button';
import { styled } from '@material-ui/styles';
import ReactBnbGallery from 'react-bnb-gallery'
import './login.css';

const photos = [
  {
    photo: 'https://htn2019.blob.core.windows.net/gallery/g0.jpg',
  },
  {
    photo: 'https://htn2019.blob.core.windows.net/gallery/g1.jpg',
  },
  {
    photo: 'https://htn2019.blob.core.windows.net/gallery/g2.jpg',
  },
  {
    photo: 'https://htn2019.blob.core.windows.net/gallery/g3.jpg',
  },
  {
    photo: 'https://htn2019.blob.core.windows.net/gallery/g4.jpg',
  },
  {
    photo: 'https://htn2019.blob.core.windows.net/gallery/g5.jpg',
  },
  {
    photo: 'https://htn2019.blob.core.windows.net/gallery/g6.jpg',
  },
  {
    photo: 'https://htn2019.blob.core.windows.net/gallery/g7.jpg',
  },
  
];

const MyButton = styled(Button)({
  background: 'linear-gradient(45deg, #FE6B8B 30%, #FF8E53 90%)',
  border: 0,
  borderRadius: 200,
  boxShadow: '0 3px 5px 2px rgba(255, 105, 135, .3)',
  color: 'white',
  height: 70,
  padding: '0 30px',
});

class Gallery extends Component {
  constructor() {
    super(...arguments);
    this.state = { galleryOpened: false };
    this.toggleGallery = this.toggleGallery.bind(this);
  }

  toggleGallery() {
    this.setState(prevState => ({
      galleryOpened: !prevState.galleryOpened
    }));
  }

  render () {
    return (
      <div className="galleryButton">
      <MyButton onClick={this.toggleGallery}>Open photo gallery</MyButton>
      <ReactBnbGallery
        show={this.state.galleryOpened}
        photos={photos}
        onClose={this.toggleGallery} />
      </div>
    )
  }
}
export default Gallery;