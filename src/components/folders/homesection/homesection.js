import styled from 'styled-components';
import { Link as LinkRouter } from 'react-router-dom';

export const Wrapper = styled.div`
display: flex;
`

export const Btn = styled.div`
display: flex;



@media screen and (max-width: 767px) {


`

export const TexW = styled.div`
display: flex;
flex-direction: column;
align-items: center;
object-fit: contain;
color: white;
font-size: 30px;
margin: 50px;

`

export const Btnl = styled(LinkRouter)`
border-radius: 50px;
background: white;
white-space: nowrap;
padding: 20px 80px;
color: black;
font-size: 40px;
cursor: pointer;
transition: all 0.2s ease-in-out;
text-decoration: none;




&:hover {
  transition: all 0.5 ease-in-out;
  background: white;
  color: darkblue;
}
`

export const SomeText = styled.h1`

`


export const SomeText2 = styled.h1`

`