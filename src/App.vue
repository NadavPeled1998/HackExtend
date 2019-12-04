<template>

  <div id="app">
    <router-view />
  </div>
</template>
<<<<<<< HEAD
<script></script>
<style>
@import url("https://fonts.googleapis.com/css?family=Dosis:400,700,800");
body {
  margin: 0 !important;
  padding: 0 !important;

  background: /*linear-gradient(rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.2)),*/ url("http://www.splitshire.com/wp-content/uploads/2014/11/SplitShire-05072.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  height: 100%;
  font-family: "asimon", "Dosis", sans-serif;
  font-weight: 400;
  font-size: 3em;
}
/* Add a black background color to the top navigation */
.topnav {
  background-color: #f9fcf0;
  overflow: hidden;
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
}

/* Add a color to the active/current link */
.topnav a.active {
  background-color: #4caf50;
  color: white;
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

.button1 {
  background-color: #4caf50; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  border-radius: 8px;
  margin-left: 38%;

  -webkit-transition-duration: 0.4s; /* Safari */
  transition-duration: 0.4s;
}
.button2 {
  background-color: #4caf50; /* Green */
  border: none;
  color: white;
  padding: 15px 40px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  border-radius: 8px;
  margin-left: 3%;
  /*margin-right:50%;*/
  -webkit-transition-duration: 0.4s; /* Safari */
  transition-duration: 0.4s;
}

.button1:hover {
  background-color: #4e8235;
  color: white;
}
.button2:hover {
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
  margin-left: 3%;
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
  padding: 10px 10px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  border-radius: 8px;
  margin-left: 3%;
  /*margin-right:50%;*/
  -webkit-transition-duration: 0.4s; /* Safari */
  transition-duration: 0.4s;
}
.timepart input[type="time"] {
  background-color: #ffff; /* Green */
  border: none;
  color: #193001;
  padding: 15px 40px;
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
.kamahav {
  float: right;
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.admatai {
  float: right;
}

.button3 {
  background-color: #4caf50; /* Green */
  border: none;
  color: white;
  padding: 15px 40px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  border-radius: 8px;
  margin-left: 3%;
  margin-top: 7%;
  /*margin-right:50%;*/
  -webkit-transition-duration: 0.4s; /* Safari */
  transition-duration: 0.4s;
}

.button3:hover {
  background-color: #4e8235;
  color: white;
}
.result {
  text-align: center;
  margin-top: 100px;
  color: white;
  font-size: 60%;
}
.button4 {
  background-color: #4caf50; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  border-radius: 8px;
  margin-left: 45%;
  margin-right: 40%;

  -webkit-transition-duration: 0.4s; /* Safari */
  transition-duration: 0.4s;
}
.button4:hover {
  background-color: #4e8235;
  color: white;
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
.button5 {
  display: inline-block;
  background-color: #4caf50; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  margin-left: 2.5px;
  margin-right: 2.5px;

  font-size: 16px;
  border-radius: 8px;

  -webkit-transition-duration: 0.4s; /* Safari */
  transition-duration: 0.4s;
}
.button5:hover {
  background-color: #4e8235;
  color: white;
}
.buttons5 {
  margin-top: 100px;
  margin-right: 5%;
  margin-left: 5%;
}
.error {
  border: 5px solid red;
}
=======
<script>

</script>
<style>
  @import url('https://fonts.googleapis.com/css?family=Dosis:400,700,800');
      body {
          margin: 0 !important;
          padding: 0 !important;

          background: linear-gradient(rgba(0,0,0,0.2),rgba(0,0,0,0.2)), url("http://www.splitshire.com/wp-content/uploads/2014/11/SplitShire-05072.jpg");
          background-repeat: no-repeat;
          background-size: cover;
          height:100vh;
          font-family: 'asimon', 'Dosis', sans-serif;
          font-weight: 400;
          font-size: 3em;
      }
      /* Add a black background color to the top navigation */
      .topnav {
        background-color: #f9fcf0;
        overflow: hidden;
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

      .topnav a.logo{
        float: left;
      }

      /* Change the color of links on hover */
      .topnav a:hover {
        background-color: #ddd;
        color: black;
      }

      /* Add a color to the active/current link */
      .topnav a.active {
        background-color: #4CAF50;
        color: white;
      }
      .contentfp{
        display: block;
        margin-top: 5%;
        margin-left: auto;
        margin-right: auto;
        width: 40%;
      }

      .anachnu{
        display: block;
        margin-top: 5%;
        margin-left: auto;
        margin-right: auto;
        width: 52%;
      }

      .button1 {
        background-color: #4CAF50; /* Green */
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        border-radius: 8px;
        margin-left: 38%;

        -webkit-transition-duration: 0.4s; /* Safari */
       transition-duration: 0.4s;
      }
      .button2 {
        background-color: #4CAF50; /* Green */
        border: none;
        color: white;
        padding: 15px 40px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        border-radius: 8px;
        margin-left: 3%;
        /*margin-right:50%;*/
        -webkit-transition-duration: 0.4s; /* Safari */
       transition-duration: 0.4s;

      }

      .button1:hover {
        background-color: #4E8235;
        color: white;
      }
      .button2:hover {
        background-color: #4E8235;
        color: white;
      }
      .ask{
      display: block;
      float: right;
      margin-top: 3%;
      margin-right: 20%;

      }
      .names{
      background-color: #e3e3e3; /* Green */
      border: none;
      color: black;
      padding: 10px 10px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 16px;
      border-radius: 8px;
      margin-left: 3%;
      /*margin-right:50%;*/
      -webkit-transition-duration: 0.4s; /* Safari */
     transition-duration: 0.4s;


      }
      .names input[type=text]{
      background-color:#ffff ; /* Green */
      border: none;
      color: #193001;
      padding: 15px 40px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 16px;
      border-radius: 8px;
      margin-top:5px;
      /*margin-right:50%;*/
      -webkit-transition-duration: 0.4s; /* Safari */
     transition-duration: 0.4s;



      }
      .timepart{
      background-color: #e3e3e3; /* Green */
      border: none;
      color: black;
      padding: 10px 10px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 16px;
      border-radius: 8px;
      margin-left: 3%;
      /*margin-right:50%;*/
      -webkit-transition-duration: 0.4s; /* Safari */
     transition-duration: 0.4s;


      }
      .timepart input[type=time]{
      background-color: #ffff; /* Green */
      border: none;
      color: #193001;
      padding: 15px 40px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 16px;
      border-radius: 8px;
      margin-left:5px;
      /*margin-right:50%;*/
      -webkit-transition-duration: 0.4s; /* Safari */
     transition-duration: 0.4s;



      }
      .kamahav{
      float:right;
      display: block;
      margin-left:auto;
      margin-right:auto;

      }
      .admatai{
      float:right;

      }

      .button3 {

        background-color: #4CAF50; /* Green */
        border: none;
        color: white;
        padding: 15px 40px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        border-radius: 8px;
        margin-left: 3%;
      margin-top: 7%;
        /*margin-right:50%;*/
        -webkit-transition-duration: 0.4s; /* Safari */
       transition-duration: 0.4s;

      }

      .button3:hover {
        background-color: #4E8235;
        color: white;
      }
      .result{
     text-align: center;
     margin-top:100px;
     color:white;
     font-size:60%;
      }
      .button4 {
        background-color: #4CAF50; /* Green */
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        border-radius: 8px;
        margin-left: 45%;
        margin-right:40%;

        -webkit-transition-duration: 0.4s; /* Safari */
       transition-duration: 0.4s;
      }
      .button4:hover {
        background-color: #4E8235;
        color: white;
      }
      .loya{
      text-align: center;
      margin-top:100px;
      color:white;

      }

>>>>>>> b768921fa4cc6f34c95c093d4276eab8d248e7ee
</style>
