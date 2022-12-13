import React, { Component } from 'react';
import Bread from '../bread.png';

class Item extends Component {
    state = { 
        name: "Item Name",
        imageUrl: null,
        cost: 0.00,
        store: "Store Name"
     };

    constructor(name, store, cost, imageUrl) {
        super();
        this.name = name;
        this.imageUrl = imageUrl;
        this.cost = cost;
        this.store = store;
    }
    setName(newName) {
        this.name = newName;
    }

    setImageUrL(newUrl) {
        this.imageUrl = newUrl;
    }

    setCost(newCost) {
        this.cost = newCost;
    }

    setStore(newStore) {
        this.store = newStore;
    }

    getName() {
        return this.name;
    }

    getImageUrl() {
        return this.imageUrl;
    }

    getCost() {
        return this.cost;
    }

    getStore() {
        return this.store;
    }
    render() { 
        return (
            <div>
                <text>{ this.state.name }</text>
                <img src={ this.state.imageUrl } alt={ this.state.name } />
                <text>${ this.state.cost } { this.state.store }</text>
            </div>
        );
    }
}
 
export default Item;