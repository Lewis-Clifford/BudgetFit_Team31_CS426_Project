import React from 'react'
import {Nav, IconM, Menu, NavLink, Btn, Btnl, Item} from './Navbar';
import {VscThreeBars} from 'react-icons/vsc'

const Navbar = () => {
  return (
    <>
    <Nav>
            <NavLink to = '/'><img className="BudgetFitLogo" src={`${process.env.PUBLIC_URL}/assets/images/BudgetFitLogo.png`} alt="logo" width="80" pointer-events="none"/></NavLink>
            <IconM>
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