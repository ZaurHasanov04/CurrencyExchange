<template>
<div class="nav">
  <router-link :to="{'path': '/signup'}">Go to Foo</router-link>
</div>


<div class="central">
    <div class="central-header">
        <p>Gunun mezennesi {{ CurrentDate }} </p>
    </div>

    <form action="GET" class="search">
        <input type="search" v-model="searchQuery" @input="HandleSearch" name="" id="">
    </form>
    
    <div class="currency-converter">
        <div>
            <input type="text" v-model="fromAmount" @input="handleAmountChange()" placeholder="Enter amount">
            <div class="input-select">
                <select v-model="fromCurrency">
                    <option v-for="currency in currencies" :value="currency.code" :key="'from_' + currency.code">{{ currency.code }} - {{ currency.name }}</option>
                </select>
            </div>
        </div>
        <div>
            <input type="text" v-model="toAmount" @input="handleAmountChange()" placeholder="Enter amount">
            <div class="input-select">
                <select v-model="toCurrency" >
                    <option v-for="currency in currencies" :value="currency.code" :key="'to_' + currency.code">{{ currency.code }} - {{ currency.name }}</option>
                </select>
            </div>
        </div>
  </div>

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

    
</div>



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
    isNumberOrDecimal(input){
        const numberPattern = /^-?\d+(\.\d{1,4})?$/;

        return numberPattern.test(input)
    },
    async handleAmountChange() {
      // Validate input as number or decimal number
      if(this.isNumberOrDecimal(this.fromAmount)){
        this.convertCurrency()
      }else{
        console.log('yalniz 4 deqiqliye qeder')
      }
    },
    async convertCurrency() {
      if (this.fromCurrency && this.toCurrency && this.fromCurrency !== this.toCurrency) {
        // Fetch currency conversion rates
        const fromCurrencyRate = this.currencies.find(currency => currency.code === this.fromCurrency).value;
        
        const toCurrencyRate = this.currencies.find(currency => currency.code === this.toCurrency).value;
        // Perform conversion

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

.input-select {
  position: relative;
}

.input-select select {
  position: absolute;
  right: 60px;
  top: -21px;
  width: 20%;
  height: 20px;
}
table, th, td {
  border:1px solid black;
}

table{
    border-spacing: 0px;
}



</style>