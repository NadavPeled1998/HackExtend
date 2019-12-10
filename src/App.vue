<template>
  <div id="app">
    <router-view />
  </div>
</template>
<script></script>
<style>
/*@import url("https://fonts.googleapis.com/css?family=Dosis:400,700,800");*/
@import url("https://fonts.googleapis.com/css?family=Amatic+SC|Varela+Round&display=swap:400,700,800");

body {
  margin: 0 !important;
  padding: 0 !important;

  background: /*linear-gradient(rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.2)),*/ url("http://www.splitshire.com/wp-content/uploads/2014/11/SplitShire-05072.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  height: 100%;
  font-family: "Amatic SC", cursive;
  font-weight: 400;
  line-height: 15px;
  font-size: 3em;
}
/* Add a black background color to the top navigation */
.topnav {
  background-color: #f9fcf0;
  overflow: hidden;
  font-family: "Varela Round", sans-serif;
}

/* Style the links inside the navigation bar */
.topnav a {
  float: right;
  color: #426811;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
  -webkit-transition-duration: 0.4s; /* Safari */
  transition-duration: 0.4s;
}

.topnav a.logo {
  float: left;
}

/* Change the color of links on hover */
.topnav a:hover {
  background-color: #ddd;
  color: black;
  padding-bottom: 19.5px;
}

/* Add a color to the active/current link */
.topnav a.active {
  background-color: #4caf50;
  color: white;
  padding-bottom: 19.5px;
}
.contentfp {
  display: block;
  margin-top: 5%;
  margin-left: auto;
  margin-right: auto;
  width: 40%;
}
.anachnu {
  display: block;
  margin-top: 5%;
  margin-left: auto;
  margin-right: auto;
  width: 52%;
}
button {
  background-color: #4caf50; /* Green */
  border: none;
  color: white;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  border-radius: 8px;
  padding: 15px 32px;
  /*font-family: 'Varela Round', sans-serif;

  -webkit-transition-duration: 0.4s; /* Safari */
  transition-duration: 0.4s;
}

button:hover {
  background-color: #4e8235;
  color: white;
}

.ask {
  display: block;
  float: right;
  margin-top: 3%;
  margin-right: 20%;
}
.names {
  background-color: #e3e3e3; /* Green */
  border: none;
  color: black;
  padding: 10px 10px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  border-radius: 8px;
  margin-left: 5%;
  margin-bottom: 2%;
  margin-right:-1%;
  /*margin-right:50%;*/
  -webkit-transition-duration: 0.4s; /* Safari */
  transition-duration: 0.4s;
}
.names input[type="text"] {
  background-color: #ffff; /* Green */
  border: none;
  color: #193001;
  padding: 15px 40px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  border-radius: 8px;
  margin-top: 5px;
  /*margin-right:50%;*/
  -webkit-transition-duration: 0.4s; /* Safari */
  transition-duration: 0.4s;
}
.timepart {
  background-color: #e3e3e3; /* Green */
  border: none;
  color: black;
  padding: 10px 18px 10px 0px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  border-radius: 8px;
  margin-left: 10%;
  /*margin-right:50%;*/
  -webkit-transition-duration: 0.4s; /* Safari */
  transition-duration: 0.4s;
}
.timepart input[type="time"] {
  background-color: #ffff; /* Green */
  border: none;
  color: #193001;
  padding: 15px 0px 15px 40px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  border-radius: 8px;
  margin-left: 5px;
  margin-bottom: 0px;
  /*margin-right:50%;*/
  -webkit-transition-duration: 0.4s; /* Safari */
  transition-duration: 0.4s;
}
.hatchala {
  font-family: "Varela Round", sans-serif;
  margin-left: 20px;
  display: inline-block;
  background-color: white;
  border-radius: 8px;
  color: black;
  padding-right: 40px;
}
.img {
  display: block;
}
.kamahav {
  float: right;
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.admatai {
  float: right;
}
.loya {
  text-align: center;
  margin-top: 100px;
  color: white;
}
.members {
  text-align: center;
  color: white;
  font-size: 50%;
}
.memebersh {
  text-align: center;
  color: white;
}
.result {
  text-align: center;
  margin-top: 100px;
  color: white;
  font-size: 60%;
}
.buttons5 {
  margin-top: 100px;
  margin-right: 5%;
  margin-left: 5%;
}
.error {
  border: 5px solid red;
}
.sign {
  display: inline-block;
  text-align: center;
  background-color: white;
  border-radius: 20px;
  margin-right: 35%;
  font-size:60px;
}
.sign p {
  margin-bottom: 40%;
  display:block;
}
.sign label {
  font-size:40px;
  display:block;
}
.sign input {
  font-size:20px;
  margin-right: 20%;
  margin-top: 20%;
  margin-bottom:10%;
  display: block;
}
.sign .forgot {
  float:right;
  margin-left:20%;
  margin-bottom: 1%;
  font-size: 13px;
  font-family: "Varela Round", sans-serif;
}
.sign button{
  margin-right: 65%;
}
.signin {
 padding-bottom: 2.5%;
 padding-right: 5%;
  padding-left: 7.5%;
}
.login {
  margin-top: 2%;
  padding-bottom: 2%;
  padding-right: 5%;
  padding-left: 10%;
}
</style>
