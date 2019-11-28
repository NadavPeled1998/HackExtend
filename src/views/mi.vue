<template>
  <div class="mi">
  <div class="topnav">
  <router-link to="/">בית</router-link>
  <router-link to="/newteam"> צור קבוצה</router-link>
  <router-link to="/exist">קבוצות קיימות</router-link>
  <router-link to="/contact">צור קשר</router-link>
  <router-link to="/mi" class="active">מי אנחנו</router-link>
  <router-link to="/" class="logo"><img src="/images\logosh.png" height=18px></router-link>
  </div>
    <div>
        <img src="/images\mianachnu.png" width=30% class="contentfp">
    </div>

  </div>
</template>
<script>
export default {
  name: "Mi"
};
</script>
<style>

</style>
