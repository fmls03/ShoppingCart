<template>
    <div class="container">
        <div id="div-title">
            <p id="title">Carrello della spesa</p>
        </div>
        <table class="table">
            <tr>
                <th id="columns">Prodotto</th>
                <th id="columns">Comprato</th>
            </tr>

            <tr v-for="(product, index) in products" :key="index" >
                <th v-bind:class="{ 'isBought': isActive, 'notBought': !isActive}">{{ product.nome }}</th>                    
                <th><input type="checkbox" name="comprato" id="comprato" v-on:change="isBought(product)"
                ></th>
            </tr>
        </table>
    </div>
</template>


<script>
import axios from 'axios';

export default {
    name : 'ShoppingCart',
    data() {
        return {
            isActive: false,
            textDec: 'bought',
            products: []
        };
    },
    methods: {
        async getProducts() {
            let response = await axios.get('http://localhost:5000/');
            this.products = response.data;
            console.log(products)
            .catch((error) => {
            console.error(error);
        });
        },
        isBought(product){
            this.isActive = !this.isActive;
            this.product.comprato = !this.product.comprato
            
        }
    },
    created() {
        this.getProducts();
        

    },
};


</script>

<style>

.container{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
#div-title{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 220px;
    height: 30px;
    border-radius: 5px;
    background-color: rgb(100, 100, 100, 0.4);
    font-weight: bold;
}

#text-title{
    color: black;
}

.table{
    margin-top: 10%;
    text-align: center;
    background-color: rgb(150, 150, 150, 0.6);
    border-radius: 6px;
}

th{
    width: 200px;
    font-size: smaller;
    font-weight: normal;
}

#columns{
    border-bottom:1px solid rgba(0, 0, 0, 0.328);
    font-weight: bold;

}

.isBought{
    text-decoration: line-through;
}

.notBought{
    text-decoration: none;
}


</style>