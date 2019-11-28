<template>
  <div class="First">
  <h1>שמירות</h1>
<p> ברוכים הבאים לאתר שהולך להוריד ממכם דאגה אחת פחות</p> 
<p> לא עוד ריבים על מי ישמור מתי</p>
<p> לא עוד שריפת שעות שינה וזמן בשביל לחשב כל אחד ואחד מתי הוא צריך לשמור </p>
<p> כל מה שאתם צריכים לעשות זה לכתוב את השמות של החברים שלכם,</p>
<p>  לבחור את השעות שבהם אתם הולכים לשמור וכל שאר העבודה עלינו</p>
<ul>
    <li><router-link to="/exist" >קבוצה קיימת</router-link></li> 
    <li><router-link to="/newteam">צור קבוצה חדשה</router-link></li>
</ul>
  </div>
</template>

<script>
export default {
  name: "Firstpage"
};
</script>
<style>
  body{
  background-image: url("../assets/background4.jpg"); 
  background-repeat: no-repeat;
  background-size: cover;
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

/* Change the link color to #111 (black) on hover */
li a:hover {
  background-color: #111;
}
</style>
