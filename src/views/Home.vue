<template>
  <div class="First">
    <div class="topnav">
      <router-link to="/" class="active">בית</router-link>
      <router-link to="/newgroup"> צור קבוצה</router-link>
      <router-link to="/existing">קבוצות קיימות</router-link>
      <router-link to="/contact">צור קשר</router-link>
      <router-link to="/about">מי אנחנו</router-link>
      <router-link to="/" class="logo"
        ><img src="/images\logosh.png" height="18px"
      /></router-link>
    </div>
    <div>
      <img src="/images\logowhite.png" width="30%" class="contentfp" />
      <router-link to="/existing"
        ><button class="button1">קבוצה קיימת</button></router-link
      >
      <router-link to="/newgroup"
        ><button class="button2">צור קבוצה</button></router-link
      >
    </div>
</template>

<script>
export default {
  name: "Home"
};
</script>
