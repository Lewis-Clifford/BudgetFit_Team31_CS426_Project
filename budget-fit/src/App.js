import "./App.css";

import React from 'react';
import HomePage from './BudgetFitPages/home';
import {BrowserRouter as Router} from 'react-router-dom';
import Animation from "./components/animation";
import HomeSection from "./components/folders/homesection";

function App() {
  return (
    <>
    <Router>
      <HomePage/>
      <Animation/>
    </Router>
    </>
  );
}

export default App;
