import "./App.css";
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import React from 'react';
import Navbar from './components/navbar/index';
import HomePage from './BudgetFitPages/home'
import ShopPage from "./BudgetFitPages/shop";
import DietPage from "./BudgetFitPages/diet";
import ExercisePage from "./BudgetFitPages/exercise";
import AboutPage from "./BudgetFitPages/about";
import LoginPage from "./BudgetFitPages/login";



function App() {
  return (
    <Router>
        <Navbar/>
        <Routes>
          <Route path="/" element ={<HomePage/>}/>
          <Route path="/shop" element ={<ShopPage/>}/>
          <Route path="/diet" element ={<DietPage/>}/>
          <Route path="/exercise" element ={<ExercisePage/>}/>
          <Route path="/about" element ={<AboutPage/>}/>
          <Route path="/login" element ={<LoginPage/>}/>
        </Routes>
        </Router>

  );
}

export default App;
