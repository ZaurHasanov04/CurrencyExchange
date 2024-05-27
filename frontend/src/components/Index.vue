<template>

<v-container>
  <v-row class="mt-3 ml-3" >
    <v-col col="2">
      <v-sheet class="d-flex">
        <v-col col = "1" ><router-link :to="{'path': '/signup'}">Register</router-link></v-col>
        <v-col col="1"><router-link :to="{'path': '/login'}">Login</router-link></v-col>
      </v-sheet>
    </v-col>
  </v-row>
</v-container>



    <v-container>
      <v-row class="mt-3">
        <v-col col="12" align="center" >
            <v-text-field
          v-model="searchQuery"
          label="Search"
          @input = HandleSearch
          placeholder="Code or Name"
          ></v-text-field> 
        </v-col>
      </v-row>  <!--This search field-->
      
      <v-sheet class="d-flex" >
        <v-col col="6" >
          <v-sheet class ="d-flex">
            <v-text-field
          v-model="fromAmount"
          @input = 'handleAmountChange'
          label="From Exchange"
          placeholder="Value"
          
          ></v-text-field> 
          <v-select
            v-model="fromCurrency"
            label="Select"
            :items="currencies"
            item-title="code"
            item-value="value"
            return-object=""
          ></v-select>
          </v-sheet>
        </v-col>
        <v-col col="6" >
          <v-sheet class ="d-flex">
            <v-text-field
          v-model="toAmount"
          @input = 'handleAmountChange'
          label="To Exchange"
          placeholder="Value"
          ></v-text-field> 
          <v-select
          v-model="toCurrency"
        label="Select"
        :items="currencies"
        item-title="code"
        item-value="value"
        return-object=""
      ></v-select>
          </v-sheet>
        </v-col>
        
      </v-sheet>
        
    </v-container>


    

    <table style="width:100%; margin-top: 30px;">
        <tr>
            <th>Code</th>
            <th>Name</th>
            <th>Nominal</th>
            <th>Value</th>
        </tr>
        <template v-if="searchQuery" >
            <tr v-for="currency in filteredCurrencies" v-bind:key="currency.id">
                <td>{{ currency.code }}</td>
                <td>{{ currency.name }}</td>
                <td>{{ currency.nominal }}</td>
                <td>{{ currency.value }}</td>
            </tr>
        </template>
        <template v-else>
            <tr v-for="currency in currencies" v-bind:key="currency.id">
                <td>{{ currency.code }}</td>
                <td>{{ currency.name }}</td>
                <td>{{ currency.nominal }}</td>
                <td>{{ currency.value }}</td>
            </tr>
        </template>
    
    </table>
   




</template>



<script>
import axios from "axios";
import debounce from 'lodash/debounce'; 

// import { useRouter } from 'vue-router';

export default {
  data(){
    return {
        currencies: [], // Keeps Data which fething api
        filteredCurrencies:[], //Keeps filter and searched data which I used Handle Search
        searchQuery: '', //selected from search input
        fromCurrency: '', // Selected from currency
        toCurrency: '', // Selected to currency
        fromAmount: '', // Amount in "from" currency
        toAmount: '',
        CurrentDate: '', 
        numberValidateRule:[
        v => !!v || 'Value is required',
        v => /^\d*\.?\d{0,4}$/.test(v) || 'Invalid number format'
      ]
    }
  },
  mounted(){
    this.getCurrency();
    this.GetCurrentDate()
  },
  methods:{
    async getCurrency(){
        try{
            const response = await axios.get('http://127.0.0.1:8000/currency/api')
            this.currencies = response.data;
        }catch(error){
            console.error('Dont find')
        }
    },
    


    async HandleSearch(){
        debounce(() => {
        if (this.searchQuery) {
          this.filteredCurrencies = this.currencies.filter(currency =>
            currency.name.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
            currency.code.toLowerCase().includes(this.searchQuery.toLowerCase())
            // Add more conditions as needed for other fields
          );
        } 
        // else {
        
        //   this.filteredUsers = []; // Clear filtered currencies when search query is empty
        // }
      }, 300)();
    },


    async isNumberOrDecimal(input){
        const numberPattern = /^-?\d+(\.\d{1,4})?$/;

        return numberPattern.test(input)
    },


    async handleAmountChange() {
      // Validate input as number or decimal number
      if(this.isNumberOrDecimal(this.fromAmount)){
        // console.log(this.fromCurrency)
        this.convertCurrency()
      }else{
        this.fromAmount=''
      }
    },


    async convertCurrency() {
      if (this.fromCurrency.code && this.toCurrency.code && this.fromCurrency.code !== this.toCurrency.code) {
        // Fetch currency conversion rates
        const fromCurrencyRate = this.currencies.find(currency => currency.code === this.fromCurrency.code).value;
        
        const toCurrencyRate = this.currencies.find(currency => currency.code === this.toCurrency.code).value;
        // Perform conversion
        console.log(this.fromAmount)
        this.toAmount = ((parseFloat(this.fromAmount).toFixed(4) * fromCurrencyRate) / toCurrencyRate).toFixed(4)
        
      } else {
        // Reset amounts if currencies are not selected or are the same
        this.fromAmount = '';
        this.toAmount = '';
      }
    },
    // async swapCurrencies() {
    //   const temp = this.fromCurrency; //not working yet
    //   this.fromCurrency = this.toCurrency;
    //   this.toCurrency = temp;
    // },
    
    GetCurrentDate(){
      const date = new Date();
      // Format the date as needed
      const formattedDate = `${date.getDate()}-${date.getMonth() + 1}-${date.getFullYear()}`;
      this.CurrentDate = formattedDate;
  },
  goToSignUp() {
      // Prevent default navigation behavior
     
      this.$router.push('/signup');
    }
  },
  
  name: 'PageIndex',
  props: {
    msg: String
  }
}
</script>


<style>

.central{
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    border: 1px solid black;
    height: 800px;
    width: 800px;
    
}

.central-header{
    color: black;
    font-size: 16px;
}


.search input[type='search']{
    border-radius: 1px;
    width: 500px;
    height: 40px;
}

.currency-converter {
  display: flex;
  align-items: center;
  margin:30px 0px 30px 0px;
  gap: 150px;
  width: 100%;
}

.currency-converter > div {
  margin-right: 10px;
  width: 300px;
}

.myselectbox{
  position: relative;

}

.myselectbox select {
  position: absolute;
  right: 60px;
  top: -21px;
  width: 20%;
  height: 20px;
  border: 1px solid black;
}

.selected{
  color: black;
}
table, th, td {
  border:1px solid black;
}

table{
    border-spacing: 0px;
}



</style>