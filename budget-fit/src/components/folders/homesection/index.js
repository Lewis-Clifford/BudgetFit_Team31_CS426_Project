import React from 'react'
import background from "../../../components/goat.jpeg"
import { Wrapper, Btnl, Btn, TexW, SomeText, SomeText2 } from './homesection'

const HomeSection = () => {
  return (
    <Wrapper>
    <div style={{backgroundImage: `url(${background})`, backgroundPosition: 'center',
    backgroundSize: 'cover',
    backgroundRepeat: 'no-repeat',
    width: '100vw',
    height: '100vh'}} >
    <TexW>
    <SomeText2>Save Money.</SomeText2>
    <SomeText2>Eat Clean.</SomeText2>
    <SomeText2>Get in Shape.</SomeText2>
    <SomeText2></SomeText2>
    
    <Btn>
          <Btnl to="/login">Begin</Btnl>
    </Btn>
    </TexW>
    
    </div>
    </Wrapper>
  )
}

export default HomeSection