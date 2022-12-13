import React from 'react'
import {Routes, Route, useLocation} from 'react-router-dom';
import ShopPage from "../BudgetFitPages/shop";
import DietPage from "../BudgetFitPages/diet";
import ExercisePage from "../BudgetFitPages/exercise";
import AboutPage from "../BudgetFitPages/about";
import LoginPage from "../BudgetFitPages/login";
import {AnimatePresence} from 'framer-motion';
import RealHome from '../BudgetFitPages/realhome';

function Animation() {
const location = useLocation();

  return (
    <AnimatePresence>
    <Routes location={location} key={location.pathname}>
          <Route path="/" element = {<RealHome/>}/>
          <Route path="/shop" element ={<ShopPage/>}/>
          <Route path="/diet" element ={<DietPage/>}/>
          <Route path="/exercise" element ={<ExercisePage/>}/>
          <Route path="/about" element ={<AboutPage/>}/>
          <Route path="/login" element ={<LoginPage/>}/>
        </Routes>
    </AnimatePresence>
  )
}

export default Animation