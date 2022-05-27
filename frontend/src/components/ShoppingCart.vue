<template>
    <div class="container">
        <div id="div-title">
            <p id="title">Carrello della spesa</p>
        </div>
        <form @submit.prevent="submit">
        <table class="table">
            <tr>
                <th id="columns">Prodotto</th>
                <th id="columns">Comprato</th>
            </tr>

            <tr v-for="(product, index) in products" :key="index" >
                <th v-if="product.bought === false">{{ product.name }}</th>
                <th v-else style="text-decoration: line-through;">{{ product.name }}</th>
                <th><input type="checkbox" name="comprato" id="comprato" v-on:change="isBought(product.id)" v-model="product.bought" ></th>
            </tr>
        </table>

        <div id="div-add-product">
            <p id="text-add-product">Add product:</p>
            <input type="text" name="add-product" id="add-product" placeholder="Add product" v-model="newName">
            <input type="button" name="btn-add-product" id="btn-add-product" value="Add" v-on:click="addProduct">
        </div>
        </form>
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
            products: [],
            newName: ''
            
        };
    },
    methods: {
        async getProducts() {
            try{
                let response = await axios.get('/api/');
                this.products = response.data;
                console.log(this.products)
 
            }
            catch(ex){
                console.error(ex);
            }
        },
        async isBought(productID){
            this.isActive = !this.isActive;
            let product=this.products.find(product=>product.id===productID);
            if(product){
                const data = {
    		        bought: !product.bought
    	        };
                console.log('Aggiornamento: ',product);
                await axios.put(`/api/products/bought/${productID}`, data)
                .then(response => {console.log(response);
                });
                this.getProducts();
            }},
        async addProduct(){
            const data = {
                newName: this.newName
                //await axios.put('http')
            }
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

#div-add-product{
    background-color: rgb(150, 150, 150, 0.6);
    border-radius: 5px;
    display: flex;
    flex-direction: row;
    align-items: center;
    margin-top: 20px;
    height: 30px;
}

#text-add-product{
    font-weight: bold;
    font-size: small;
    margin-right: 20px;
    margin-left: 50px;
}

#add-product{
    margin-right: 20px;
    border-radius: 4px;
    background-color: aliceblue;
    color:black;
    outline: none;
    text-decoration: none;;
}

#btn-add-product{
    width: 50px;
    border-radius: 4px;
    border: 2px;
    background-color:dodgerblue;
    font-size: smaller;
    font-weight: bold;
    opacity: 0.8px;
    height: 15px;
}

#btn-add-product:hover{
    opacity: 1;
    border-color: cornflowerblue;
    box-shadow: 0 0 5px cornflowerblue;
}
</style>