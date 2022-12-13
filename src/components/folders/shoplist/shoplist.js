import React, { Component } from 'react';
import Bread from '../../../components/bread.png';
import Eggs from '../../../components/eggs.jpeg';
import Eggs2 from '../../../components/egg2.png';
import Poptarts from '../../../components/poptarts.png';
import Milk from '../../../components/milk.png';
import Beef from '../../../components/beef.png';
import Bacon from '../../../components/bacon.png';
import { useState } from 'react';
import './shoplist.css';

function ShopList()  {
    
    
    const [list, setList] = useState([
       /* {name: "Nature's Own 100% Whole Wheat Bread", store: "Smith's", price: 4.49, imageUrl: {Bread}},
        {name: "Nature's Own 100% Whole Wheat Bread", store: "Walmart", price: 3.88, imageUrl: {Bread}}*/
    ]);

    const addBread = () => {
        setList([
        {id: 1, name: "Nature's Own 100% Whole Wheat Bread", store: "Walmart", price: 3.34, imageUrl: {Bread}},
        ...list
    ]);   
    }

    const addEggs = () => {
        setList([
        {id: 2, name: "Great Value Large White Eggs, 12", store: "Walmart", price: 4.64, imageUrl: {Eggs}},
        ...list
    ]);   
    }

    const addEggs2 = () => {
        setList([
        {id: 7, name: "Oakdell Egg Farms Cage Free Large Brown Omege-3 Eggs, 12", store: "Smith's", price: 3.39, imageUrl: {Eggs2}},
        ...list
    ]);   
    }

    const addMilk = () => {
        setList([
        {id: 3, name: "Great Value Whole Milk, 1 Gal", store: "Walmart", price: 3.36, imageUrl: {Milk}},
        ...list
    ]);   
    }

    const addBeef = () => {
        setList([
        {id: 4, name: "All Natural, 73% Lean/27% Fat, Ground Beef, Roll, 1lbs", store: "Walmart", price: 3.76, imageUrl: {Beef}},
        ...list
    ]);   
    }

    const addBacon = () => {
        setList([
        {id: 5, name: "Great Value Sliced Hickory Smoked Original Bacon, 16 oz", store: "Walmart", price: 4.48, imageUrl: {Bacon}},
        ...list
    ]);   
    }

    const addPoptarts = () => {
        setList([
        {id: 6, name: "Pop-Tarts Toaster Pastries, Frosted S'mores, 16 Count", store: "Walmart", price: 4.68, imageUrl: {Poptarts}},
        ...list
    ]);   
    }
    
    const priceSum = (list) => {
        let sum = 0;
        for (let i = 0; i < list.length; i++){
            sum += list[i].price;
        }
        return sum.toFixed(2);
    }

    const storeRec = (list) => {
        let walmart = false;
        if (list.length === 0) return "None"
        for (let i = 0; i < list.length; i++){
            if (list[i].store === "Walmart") walmart = true;
        }
        
        return (walmart === true) ? "Walmart" : "Smith's";
    }

    const avgPrice = (list) => {
        let prevAvg = 19.65;
        let sum = 0;
        for(let i = 0; i < list.length; i++){
            sum += list[i].price;
        }
        
        let avg1 = ((sum + prevAvg)/2);
        if(list.length === 0) return prevAvg;
        return avg1.toFixed(2);
    }

    return (
        <div className="grid-container">
            <div className="grid-item">
            <table>
                <tr>
                    <th>Item Name</th>
                    <th>Recommended Store</th>
                    <th>Price</th>
                    
                </tr>
                {list.map((val,key) => {
                    return (
                        <tr key={key}>
                            <td>{val.name}</td>
                            <td>{val.store}</td>
                            <td>${val.price}</td>
                           
                            <td><button onClick={() => {
                                setList(list.filter(a => a.id !== val.id)
                                );
                            }}>Remove</button></td>
                        </tr>
                    )
                })}      
                <tfoot>
                    <tr>
                        <td>Total Price:</td>
                        <td>${priceSum(list)}</td>
                    </tr>    
                </tfoot>   
            </table>
            <h4>Click on an item to add it to your list.</h4>
            </div>
            
                <div className="grid-item">
                    <button1 onClick={() => {
                        addBread();
                    }}><img src={Bread} alt="" height={100} width={100}/></button1>
                    <h5>Nature's Own Whole Wheat Bread</h5>
               
                    <button1 onClick={() => {
                        addEggs();
                    }}><img src={Eggs} alt="" height={100} width= {100}/></button1>
                    <h5>Great Value Large Eggs, 12</h5>
               
                
                    <button1 onClick={() => {
                        addEggs2();
                    }}><img src={Eggs2} alt="" height={100} width= {100}/></button1>
                    <h5>Oakdell Large Eggs, 12</h5>
                </div>
                <div className="grid-item">
                    <button1 onClick={() => {
                        addPoptarts();
                    }}><img src={Poptarts} alt="" height={100} width= {100}/></button1>
                    <h5>Smore's Poptarts</h5>

                    <button1 onClick={() => {
                        addMilk();
                    }}><img src={Milk} alt="" height={100} width= {100}/></button1>
                    <h5>Great Value Whole Milk, 1 Gal</h5>

                    <button1 onClick={() => {
                        addBeef();
                    }}><img src={Beef} alt="" height={100} width= {100}/></button1>
                    <h5>Ground Beef, 73% Lean</h5>

                    <button1 onClick={() => {
                        addBacon();
                    }}><img src={Bacon} alt="" height={100} width= {100}/></button1>
                    <h5>Great Value Bacon, 16 oz</h5>
                </div>
            <h1>Your Shopping List Cost: ${priceSum(list)}</h1>
            <h1>Your Recommended Store: {storeRec(list)}</h1>
            <h1>Your Average Spending: ${avgPrice(list)}</h1>
        </div>
    );
    

} 

export default ShopList