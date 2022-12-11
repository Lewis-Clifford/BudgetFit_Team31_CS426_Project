import styled from 'styled-components';
import {CgClose} from 'react-icons/cg'
import { Link as LinkRouter } from 'react-router-dom';;

export const Data = styled.aside`
background: #474b4f;
height: 100%;
width: 100%;
display: grid;
z-index: 999;
position: fixed;
top: 0;
left: 0;
transition: all 0.5s ease-in-out;
align-items: center;

opacity: ${({ isOpen }) => (isOpen ? '100%' : '0%')};
top:${({ isOpen }) => (isOpen ? '0%' : '-100%')};
`

export const X = styled.div`
position: absolute;
top: 1rem;
right: 2.5rem;
background: transparent;
font-size: 4rem;
cursor: pointer;
`

export const XClose = styled(CgClose)`
color: white;
`

export const Navigate = styled.div`
color white;
`

export const Menu = styled.ul`
display: grid;
grid-template-columns: 1fr;
grid-template-rows: repeat(5, 160px);
text-align: center;
position:relative;
top: 55px;

`


export const DataLink = styled(LinkRouter)`
display: flex;
align-items: center;
justify-content: center;
font-size: 4rem;
text-decoration: none;
transition: 0.5s ease-in-out;
color: white;
cursor: pointer;

&:hover{
    transition: all 0.2s ease-in-out;
    background: #778899;
    opacity: 40%;
}

&:active{
    transition: all 0.1s ease-in-out;
    color: #fff;
    background: #778899;
    opacity: 70%;
}

`

export const ButtonNavigate = styled.div`
display: flex;
position: relative;
left: 25px;
top: -75px;
justify-content: center;
`

export const ButtonLink = styled(LinkRouter)`
border-radius: 50px;
background: #73b464;
white-space: nowrap;
padding: 16px 40px;
color: #fff;
font-size: 3rem;
border:;
cursor: pointer;
transition: all 0.2s ease-in-out;
text-decoration: none;

&:hover {
  transition: all 0.5 ease-in-out;
  background: white;
  color: #479761;
}
`

