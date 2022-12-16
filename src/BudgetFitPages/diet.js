import React from 'react'
import { motion } from "framer-motion"
import MobileBar from "../components/folders/mobilebar";
import Navbar from '../components/folders/navigationbar/index';
import HomeSection from '../components/folders/homesection'
import '../components/folders/diet/dietsection.css'

const DietPage = () => {
  return (
    <div>
    
    <div className="centered-div">
        <div class="container">
            <div class="box ">
                <div class="cus-pad ">
                    <div class="cus-main">
                        <h3 class="center1">What are your seconday diet goals?</h3>
                        <h6 class="center1">*Choose unlimited from Part 2, besides last option</h6>
                        <br />
                        <h3 class="center1">Part 1</h3>
                        <form>
                            <input type="radio" id="keto" name="diet_type" value="keto-diet" />
                                <label for="keto">Keto Diet (Low-no carbohydrates)</label>
                                <br/>
                            <input type="radio" id="veget" name="diet_type" value="veget-diet" />
                                <label for="keto">Vegetarian Diet (No meat)</label>
                                <br/>
                            <input type="radio" id="vegab" name="diet_type" value="vegan-diet" />
                                <label for="keto">Vegan Diet (No meat or dairy)</label>
                                <br/>
                            <input type="radio" id="carni" name="diet_type" value="carni-diet" />
                                <label for="keto">Carnivore Diet (Strictly animal based)</label>
                                <br/>
                            <input type="radio" id="paleo" name="diet_type" value="paleo-diet" />
                                <label for="keto">Paleo Diet (Strictly whole foods, avoid processed)</label>
                                <br/>
                            <input type="radio" id="none" name="diet_type" value="no-diet" />
                                <label for="keto">I <strong>do not</strong> plan on eating any of these diets</label>
                                <br />
                                <br />
                                <br />
                                <br />
                            <button type="submit" class="btn btn-primary custom-btn"> FINISH </button>
                        </form>
                    </div>
                    <h3 class="center1">Need help?</h3>
                </div>
            </div>
        </div>
    </div>
    </div>
  )
}

export default DietPage
