import React, {useState} from 'react'
import MobileBar from "../components/folders/mobilebar";
import Navbar from '../components/folders/navigationbar/index';
import HomeSection from '../components/folders/homesection';

const HomePage = ({isVisible}) => {
  const [isOpen, setIsOpen] = useState(false);

  const toggle = () => {
    setIsOpen(!isOpen)
  };

  return (
    <div>

      <MobileBar isOpen ={isOpen} toggle ={toggle}/>
      <Navbar toggle={toggle}/>
      </div>
  );
};

export default HomePage