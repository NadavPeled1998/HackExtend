<template>
  <div class="First">
  <div class="topnav">
  <router-link to="/" class="active">בית</router-link>
  <router-link to="/newteam"> צור קבוצה</router-link>
  <router-link to="/exist">קבוצות קיימות</router-link>
  <router-link to="/contact">צור קשר</router-link>
  <router-link to="/mi" >מי אנחנו</router-link>
  <router-link to="/" class="logo"><img src="/images\logosh.png" height=18px></router-link>
  </div>
  <div>
            <img src="/images\logowhite.png" width=30% class="contentfp">
            <router-link to="/exist" ><button class="button1">קבוצה קיימת</button></router-link>
            <router-link to="/newteam"><button class="button2">צור  קבוצה</button></router-link>
      </div>
  </div>
</template>

<script>
export default {
  name: "Firstpage"
};
</script>
<style>
<<<<<<< HEAD
=======
  body{
  direction: rtl;
  }
  .First{
    background-color: rgba(255,255,255,0.6);
    margin-right: 25%;
    margin-top: 4%;
    height: 400px;
    width: 680px;
  }
  p{
      color:black;
      float: right;
      clear: both;
      line-height: 1.6px;
      margin-right: 4%;
  }
  ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
}

li {
    color: white;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}
>>>>>>> 38dce50d94b4dca500418c2f9ba56464e4f7afc5

</style>
