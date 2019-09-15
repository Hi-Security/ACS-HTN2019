import React from 'react';
import Gallerys from 'react-photo-gallery';
import './login.css';
import styled, { css } from 'styled-components'

const Content = styled.div`
  height: 650px;
  width: auto;
  overflow-x: scroll;
  img {
    border-radius:10px;
}
`;

const images = [
  {
    src: 'https://htn2019.blob.core.windows.net/gallery/g0.jpg',
  },
  {
    src: 'https://htn2019.blob.core.windows.net/gallery/g1.jpg',
  },
  {
    src: 'https://htn2019.blob.core.windows.net/gallery/g2.jpg',
  },
  {
    src: 'https://htn2019.blob.core.windows.net/gallery/g3.jpg',
  },
  {
    src: 'https://htn2019.blob.core.windows.net/gallery/g4.jpg',
  },
  {
    src: 'https://htn2019.blob.core.windows.net/gallery/g5.jpg',
  },
  {
    src: 'https://htn2019.blob.core.windows.net/gallery/g6.jpg',
  },
  {
    src: 'https://htn2019.blob.core.windows.net/gallery/g7.jpg',
  },
  
];

class Gallery extends React.Component {

 render() {
   return (
     <Content>
       <Gallerys direction={'row'} margin={40} photos={images} />
     </Content>
   );
  }
 }

 export default Gallery;