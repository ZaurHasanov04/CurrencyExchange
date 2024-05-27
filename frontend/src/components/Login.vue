<template>

<v-container>
      <v-row class="mb-3 mt-5">
        <v-col cols="4"></v-col>
        <v-col cols="4">
          <v-card ref="form" lazy-validation class="text-center">
            <v-card-title> Login Form </v-card-title>
            <v-card-text>
              <v-text-field
                v-model="User.username"
                label="Username"
                outlined
                required
              ></v-text-field>
  
              <v-text-field
                v-model="User.password"
                :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                :type="show1 ? 'text' : 'password'"
                
                label="Password"
                counter
                @click:append="show1 = !show1"
                outlined
              ></v-text-field>
              <v-btn
                color="success"
                :disabled="
                  !User.username || !User.password
                "
                @click="login"
              >
                Submit
              </v-btn>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col cols="4"></v-col>
      </v-row>
    </v-container>


</template>


<script>
import axios from "axios";

export default {
    name : "LoginPage",

    data(){
        return{
            show1 : false,
            User:{
                username:"",
                password:""
            },
            url: "http://127.0.0.1:8000/login/"

        }
        

    },
    methods:{
        login(){
            var data ={
                username: this.User.username,
                password: this.User.password,
            };

            axios.post(this.url, data).then((response) =>{
                console.log(response)
                this.$router.push({name:'index'})
            })
            .catch(error =>{
                console.log(error.response)
                console.log('Error', error.response.data)
            })
        }
    }
}

</script>