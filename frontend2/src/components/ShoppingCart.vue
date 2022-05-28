<template>
    <div class="container">
        <div id="div-title">
            <p id="title">Shopping Cart</p>
        </div>
        <table class="table">
            <tr>
                <th id="columns">Products</th>
                <th id="columns">Bought</th>
            </tr>

            <tr v-for="(product, index) in products" :key="index" >
                <th v-if="product.bought === false">{{ product.name }}</th>
                <th v-else style="text-decoration: line-through;">{{ product.name }}</th>
                <th><input type="checkbox" name="bought" id="bought-checkbox" v-on:change="isBought(product.id)" v-model="product.bought" ></th>
                <th id="delete-column"><input type="button" name="delete" id="delete-btn" v-on:click="deleteProduct(product.id)"></th>
            </tr>
        </table>

        <div id="div-add-product">
            <p id="text-add-product">Add product:</p>
            <input type="text" name="add-product" id="add-product" placeholder="Product" v-model="newName">
            <input type="button" name="btn-add-product" id="btn-add-product" value="Add" v-on:click="addProduct">
        </div>
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
                const payload = {
    		        bought: !product.bought
    	        };
                console.log('Aggiornamento: ',product);
                await axios.put(`/api/product/bought/${productID}`, payload)
                .then(response => {console.log(response);
                });
                this.getProducts();
            }},


        async addProduct(){
            const payload = {
                name: this.newName
            }
            await axios.put('/api/product/add', payload)
            .then(response => {console.log(response);
            }),
            this.getProducts();
        },

        async deleteProduct(productID){
            let product = this.products.find(product=>product.id===productID);
            if(product){
                await axios.delete(`/api/product/delete/${productID}`)
                .then(response => {console.log(response);
                });
                this.getProducts();
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
    background: rgb(46,51,56);
    background: -moz-linear-gradient(0deg, rgba(46,51,56,1) 0%, rgba(60,73,84,1) 100%);
    background: -webkit-linear-gradient(0deg, rgba(46,51,56,1) 0%, rgba(60,73,84,1) 100%);
    background: linear-gradient(0deg, rgb(43, 50, 56) 0%, rgb(56, 68, 79) 100%);
    filter: progid:DXImageTransform.Microsoft.gradient(startColorstr="#2e3338",endColorstr="#3c4954",GradientType=1);
    box-shadow: rgba(0, 0, 0, 0.5) 0px 7px 29px 0px;  
    color: white;
}


.table{
    margin-top: 10%;
    text-align: center;
    border-radius: 6px;
    background: rgb(36,41,49);
    background: -moz-linear-gradient(0deg, rgba(36,41,49,1) 0%, rgba(39,47,54,1) 100%);
    background: -webkit-linear-gradient(0deg, rgba(36,41,49,1) 0%, rgba(39,47,54,1) 100%);
    background: linear-gradient(0deg, rgb(30, 34, 41) 0%, rgb(44, 53, 62) 100%);
    filter: progid:DXImageTransform.Microsoft.gradient(startColorstr="#242931",endColorstr="#272f36",GradientType=1);
    box-shadow: rgba(0, 0, 0, 0.4) 0px 7px 29px 0px;  

}

th{
    width: 200px;
    font-size: smaller;
    font-weight: normal;
    color: white;
}

#columns{
    font-weight: bold;

}

#div-add-product{
    background: rgb(36,41,49);
    background: -moz-linear-gradient(0deg, rgba(36,41,49,1) 0%, rgb(37, 45, 52) 100%);
    background: -webkit-linear-gradient(0deg, rgba(36,41,49,1) 0%, rgba(39,47,54,1) 100%);
    background: linear-gradient(0deg, rgb(30, 34, 41) 0%, rgb(44, 53, 62) 100%);
    filter: progid:DXImageTransform.Microsoft.gradient(startColorstr="#242931",endColorstr="#272f36",GradientType=1);
    box-shadow: rgba(0, 0, 0, 0.4) 0px 7px 29px 0px;  

    color:white;
    border-radius: 5px;
    display: flex;
    flex-direction: row;
    align-items: center;
    margin-top: 20px;
    height: 30px;
    width: 430px;
}

#text-add-product{
    font-weight: bold;
    font-size: small;
    margin-right: 20px;
    margin-left: 50px;
}

#add-product{
    margin-right: 20px;
    height: 14px;
    border: 0;
    border-radius: 4px;
    background: rgb(54, 62, 66);
    color:rgb(255, 255, 255);
    outline: none;
    text-decoration: none;;
    box-shadow: rgba(0, 0, 0, 0.4) 0px 7px 29px 0px;  

}

#add-product:hover{
    border-color: rgb(128, 169, 244);
    box-shadow: 0 0 5px rgb(120, 164, 245);
}

#btn-add-product{
    font-weight: bold;
    width: 50px;
    border-radius: 4px;
    border: 2px;
    background: rgb(46 168 42);    
    font-size: smaller;
    opacity: 0.8px;
    height: 15px;
    color: white;
    box-shadow: rgba(0, 0, 0, 0.126) 0px 7px 29px 0px;  

}

#btn-add-product:hover{
    opacity: 1;
    border-color: rgb(130, 244, 128);
    box-shadow: 0 0 5px  rgb(130, 244, 128);
}

#delete-column{
    width: 20px;
}

#delete-btn{
    height: 12px;
    width: 12px;
    border-radius: 20px;
    border: 0;
    text-align: center;
    background-color: red;
    opacity: 0.8;
}

#delete-btn:hover{
    border-color: darkred;
    box-shadow: 0 0 5px red;
}
</style>