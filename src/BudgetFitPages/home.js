import React, {useState} from 'react'
import MobileBar from "../components/navbar/mobilebar";
import Navbar from '../components/navbar/navigationbar/index';

const HomePage = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggle = () => {
    setIsOpen(!isOpen)
  };

  return (
    <>
      <MobileBar isOpen ={isOpen} toggle ={toggle}/>
      <Navbar toggle={toggle}/>
      </>
  );
};

export default HomePage