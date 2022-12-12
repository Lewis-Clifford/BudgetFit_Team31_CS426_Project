import React from 'react'
import {Nav, IconM, Menu, NavLink, Btn, Btnl, Item, Img} from './Navbar';
import {VscThreeBars} from 'react-icons/vsc'

const Navbar = ({toggle}) => {
  return (
    <>
    <Nav>
            <NavLink to = '/'><Img/></NavLink>
            <IconM onClick = {toggle}>
                <VscThreeBars />
            </IconM>
          <Menu>
              <Item to = "/shop" >Shop</Item>
              <Item to = "/diet">Diet</Item>
              <Item to = "/exercise">Exercise</Item>
              <Item to = "/about">About</Item>
              <Btn>
              <Btnl to="/login">Login</Btnl>
              </Btn>
            </Menu>
            
        
    </Nav>
    </>
  );
};

export default Navbar