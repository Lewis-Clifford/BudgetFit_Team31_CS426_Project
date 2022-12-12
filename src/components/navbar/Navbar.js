import styled from  'styled-components';
import { Link as LinkRouter } from 'react-router-dom';;


export const Nav = styled.nav`
  background: #b0c4de	;
  height: 100px;
  display: flex;
  justify-content: space-between;
  padding: 0.5rem calc((50vw - 1000px) / 2);
  z-index: 10;
  font-family: Georgia;

  @media screen and (max-width: 960px) {
    transition: 0.8s all ease;
  }
`


export const Navlogo = styled(LinkRouter)`
justify-self: flex-start;
cursor: pointer;
font-size: 1.5rem;
align-items: center;
margin-left: 24px;
font-weight: bold;
text-decoration: none;
`

export const IconM = styled.div`
display: none;

 @media screen and (max-width: 767px) {
  display: block;
  position: absolute;
  top: 0;
  right: 0;
  transform: translate(-100%, 75%);
  font-size: 2.5em;
  cursor: pointer;
 }
`

export const Menu = styled.div`
display: flex;
align-items: center;
margin-right -24px;

@media screen and (max-width: 767px) {
  display: none; 
}
`

export const NavLink = styled(LinkRouter)`
color: #000;
display: flex;
align-items: center;
text-decoration: none;
padding: 0 1rem;
height: 100%;
cursor: pointer;
font-size: 28px;
margin-right: 24px;
&:active {
  color: #c9e265
}
`

export const Item = styled(LinkRouter)`

color: #000;
display: flex;
align-items: center;
text-decoration: none;
padding: 0 1rem;
height: 100%;
cursor: pointer;
font-size: 28px;
margin-right: 24px;
&:active {
  color: #c9e265
}
&:hover {
  border-bottom: 3px solid #c9e265;
}
`

export const Btn = styled.nav`
display: flex;
align-items: center;
margin-right: 24px;

@media screen and (max-width: 767px) {
  display: none;
}
`

export const Btnl = styled(LinkRouter)`
border-radius: 40px;
background: #c9e265;
white-space: nowrap;
padding: 16px 40px;
color: #000;
font-size: 20px;
border:;
cursor: pointer;
transition: all 0.2s ease-in-out;
text-decoration: none;

&:hover {
  transition: all 0.6 ease-in-out;
  background: white;
  color: darkblue;
}
`