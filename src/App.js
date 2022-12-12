import "./App.css";

import React from 'react';
import HomePage from './BudgetFitPages/home';
import {BrowserRouter as Router} from 'react-router-dom';
import Animation from "./components/animation";



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
