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
    
    return (
        <div className="ShopList">
            <table>
                <tr>
                    <th>Item Name</th>
                    <th>Recommended Store</th>
                    <th>Price</th>
                    <th>Item Image</th>
                </tr>
                {list.map((val,key) => {
                    return (
                        <tr key={key}>
                            <td>{val.name}</td>
                            <td>{val.store}</td>
                            <td>${val.price}</td>
                            <td><img src={val.imageUrl} alt="" height={50} width={50}/></td>
                            <td><button onClick={() => {
                                setList(list.filter(a => a.id !== val.id)
                                );
                            }}>Remove</button></td>
                        </tr>
                    )
                })}               
            </table>
            <h4>Click on an item to add it to your list.</h4>
            <button onClick={() => {
                addBread();
            }}><img src={Bread} alt="" height={100} width={100}/></button>
            <button onClick={() => {
                addEggs();
            }}><img src={Eggs} alt="" height={100} width= {100}/></button>
            <button onClick={() => {
                addEggs2();
            }}><img src={Eggs2} alt="" height={100} width= {100}/></button>
            <button onClick={() => {
                addPoptarts();
            }}><img src={Poptarts} alt="" height={100} width= {100}/></button>
            <button onClick={() => {
                addMilk();
            }}><img src={Milk} alt="" height={100} width= {100}/></button>
            <button onClick={() => {
                addBeef();
            }}><img src={Beef} alt="" height={100} width= {100}/></button>
            <button onClick={() => {
                addBacon();
            }}><img src={Bacon} alt="" height={100} width= {100}/></button>
        </div>
    );
    

} 

export default ShopList