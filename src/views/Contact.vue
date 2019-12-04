<template>
<<<<<<< HEAD
  <div>
    <div class="topnav">
      <router-link to="/">בית</router-link>
      <router-link to="/newgroup"> צור קבוצה</router-link>
      <router-link to="/existing">קבוצות קיימות</router-link>
      <router-link to="/contact" class="active">צור קשר</router-link>
      <router-link to="/about">מי אנחנו</router-link>
      <router-link to="/" class="logo"
        ><img src="/images\logosh.png" height="18px"
      /></router-link>
    </div>
    <div class="contact">
      <p>
        אם נתקלתם בבעיה כלשהי בשימוש באתר,
      </p>
      <p>משהו לא ברור לכם,</p>
      <p>או שסתם יש לכם כל מיני הצעות לשיפור ולשימור</p>
      <p>אתם יותר ממוזמנים לפנות אליינו למייל:</p>
      <span>peled.nadav@gmail.com</span>
    </div>
  </div>
</template>
<script>
export default {
  name: "contact"
};
</script>
<style scoped>
.contact {
  direction: rtl;
  color: white;
  font-size: 16px;
}
span {
  margin-right: 40%;
  color: blue;
  text-decoration: underline;
}
</style>
=======
<div>
<div class="topnav">
<router-link to="/">בית</router-link>
<router-link to="/newteam"> צור קבוצה</router-link>
<router-link to="/exist">קבוצות קיימות</router-link>
<router-link to="/contact" class="active">צור קשר</router-link>
<router-link to="/mi" >מי אנחנו</router-link>
<router-link to="/" class="logo"><img src="/images\logosh.png" height=18px></router-link>
</div>
<el-time-select
  v-model="value"
  :picker-options="{
    start: '00:00',
    step: '00:01',
    end: '23:59'
  }"
  placeholder="Select time">
</el-time-select>
</div>
</template>
<script>
  export default {
    data() {
      return {
        value: ''
      };
    }
  }
</script>
>>>>>>> b768921fa4cc6f34c95c093d4276eab8d248e7ee
