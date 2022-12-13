import React from 'react'
import { motion } from "framer-motion"
import MobileBar from "../components/folders/mobilebar";
import Navbar from '../components/folders/navigationbar/index';
import HomeSection from '../components/folders/homesection'
import '../components/folders/exercise/exercisesection.css'

const ExercisePage = () => {
  return (
    <div>
    <MobileBar />
    <Navbar />
    <div className="centered-div">
        <div class="container">
            <div class="box ">
                <div class="cus-pad ">
                    <div class="cus-main">
                        <h3 class="center1">What are your goals diet wise?</h3>
                        <h6 class="center1">*Choose 1 option from Part 1</h6>
                        <h6 class="center1">*Choose unlimited from Part 2, besides last option</h6>
                        <br />
                        <h3 class="center1">Part 1</h3>
                        <div class="place-tile-text">
                            <span class="list-center">a. Maintain Weight</span>
                        </div>
                        <div class="clear"></div>
                        <br />
                        <div class="place-tile-text">
                            <span class="list-center">b. Gain Healthy Weight</span>
                        </div>
                        <div class="clear"></div>
                        <br />
                        <div class="place-tile-text">
                            <span class="list-center">c. Lose Healthy Weight</span>
                        </div>
                        <div class="clear"></div>
                        <br />
                        <div class="place-tile-text">
                            <span class="list-center">d. Unsure</span>
                        </div>
                        <div class="clear"></div>
                        <br />
                        <br />
                        <br />
                        <button type="submit" class="btn btn-primary custom-btn"> NEXT </button>
                    </div>
                    <h3 class="center1">Need help?</h3>
                </div>
            </div>
        </div>
    </div>
    </div>
    
  )
}

export default ExercisePage
