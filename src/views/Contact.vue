<template>
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
