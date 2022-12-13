import styled from 'styled-components'
import Logo from "../../../components/5912.jpg"


export const TexW = styled.div`
display: flex;
flex-direction: column;
align-items: center;
object-fit: contain;
color: white;
font-size: 30px;
`

export const SomeText = styled.h1`

`

export const SomeText2 = styled.p`
font-size: 20px;
color: black;
width: 70%;
text-align: left;
line-height: 40px;

`

export const Img = styled.div`
width: 90vw;
height: 40vh;
background-image: url(${Logo});
background-size: contain;
background-position: center;
background-repeat: no-repeat;
pointerEvents = none;
z-index: 2;
margin-bottom: -20px;
`

export const Wrapper = styled.div`
    display: flex;
`