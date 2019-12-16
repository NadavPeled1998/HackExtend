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
  padding: 12px 16px;
  text-decoration: none;
  font-size: 17px;
  -webkit-transition-duration: 0.4s; /* Safari */
  transition-duration: 0.4s;
}
.topnav a.logo {
  float: left;
  margin-right: -100%;
}
.topnav a.logo:hover {
  padding-bottom: 0.75%;
}

/* Change the color of links on hover */
.topnav a:hover {
  /* padding-bottom:19.5px;*/
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
.topnav span {
  margin-left: 3.5%;
  margin-top: 20%;
  color: #426811;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
  cursor: pointer;
}
.topnav span:hover {
  background-color: #ddd;
  color: black;
  padding-bottom: 21px;
}
.topnav .signLink {
  float: left;
  display: inline-block;
  margin-left: 3.5%;
  cursor: pointer;
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
  cursor: pointer;
  text-decoration: none;
  display: inline-block;
  font-size: 18px;
  border-radius: 8px;
  padding: 15px 32px;
  font-family: "Varela Round", sans-serif;

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
  margin-right: -1%;
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
  margin-top: 20%;
  font-size: 65px;
  color: white;
}
.members {
  text-align: center;
  color: white;
}
.memebersh {
  text-align: center;
  color: white;
}
.result {
  text-align: center;
  margin-top: 5%;
  margin-bottom: 2.5%;
  margin-left: 32.5%;
  margin-right: 32.5%;
  padding-top: 2.5%;
  padding-bottom: 2%;
  background-color: rgba(0, 0, 0, 0.15);
  color: white;
  font-size: 50px;
}
.result1 {
  margin-bottom: 10%;
  direction: rtl;
}
.error {
  border: 5px solid red;
}
.sign {
  display: inline-block;
  text-align: center;
  background-color: #f9fcf0; /*;rgba(255,255,255,0.75);*/
  border-radius: 20px;
  margin-right: 35%;
  margin-bottom: 1.5%;
  font-size: 60px;
}
.sign p {
  margin-bottom: 30%;
  display: block;
}
.sign label {
  font-size: 40px;
  display: block;
  margin-top: 25%;
  margin-bottom: 25%;
}
.sign input {
  font-size: 20px;
  margin-right: 20%; /*
  background-color: #ffff;*/
  display: block;
}
.signin .forgot {
  float: right;
  margin-left: 20%;
  margin-bottom: 1%;
  font-size: 13px;
  font-family: "Varela Round", sans-serif;
  cursor: pointer;
}
.login .forgot {
  font-size: 13px;
  font-family: "Varela Round", sans-serif;
  margin-top: 10%;
  cursor: pointer;
}
.sign button {
  margin-right: 75%;
  margin-left: -5%;
  margin-top: 7.5%;
}
.signin {
  padding-bottom: 2.5%;
  padding-right: 5%;
  padding-left: 7.5%;
}
.login {
  margin-right: 35%;
  margin-top: 2.5%;
  padding-right: 1.5%;
  padding-left: 7%;
  padding-bottom: 1.5%;
}
.login button {
  margin-top: 10%;
}
.comment {
  direction: rtl;
  font-family: "Varela Round", sans-serif;
  float: right;
  margin-top: 5%;
  margin-bottom: 10%;
  font-size: 15px;
  margin-right: 20%;
  margin-left: -10%;
}
.system {
  font-size: 75px;
  margin-bottom: 10%;
}
.email {
  color: red;
  margin-right: 15%;
  font-size: 15px;
  font-family: "Varela Round", sans-serif;
}
.Mlogin {
  color: red;
  font-size: 15px;
  font-family: "Varela Round", sans-serif;
}
</style>
