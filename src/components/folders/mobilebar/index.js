import React from 'react';
import {Data, X, XClose, Navigate, Menu, DataLink, ButtonNavigate, ButtonLink} from './mobilebar'

const MobileBar = ({isOpen, toggle}) => {
  return (
    <Data isOpen={isOpen} onClick={toggle}>
        <X onClick={toggle}>
            <XClose/>
        </X>
        <Navigate>
            <Menu>
                <DataLink to = "/shop" onClick={toggle}>Shop</DataLink>
                <DataLink to = "/diet" onClick={toggle}>Diet</DataLink>
                <DataLink to = "/exercise" onClick={toggle}>Exercise</DataLink>
                <DataLink to = "/about" onClick={toggle}>About</DataLink>
            </Menu>
            <ButtonNavigate>
                <ButtonLink to = "/login">Login</ButtonLink>
            </ButtonNavigate>
        </Navigate>
    </Data>
  )
}

export default MobileBar