import React, { Component } from 'react';

class Item extends Component {
    state = { 
        name: "",
        imageUrl: "",
        cost: 0.00,
        store: ""
     };

    constructor(name, imageUrl, cost, store) {
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
        return ;
    }
}
 
export default Item;