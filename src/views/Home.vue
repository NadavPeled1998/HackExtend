<template>
  <div class="First">
    <div class="topnav">
      <router-link to="/" class="active">בית</router-link>
      <router-link :to="{ name: 'newgroup', query: { id: this.id } }">
        צור קבוצה</router-link
      >
      <router-link :to="{ name: 'existing', query: { id: this.id } }"
        >קבוצות קיימות</router-link
      >
      <router-link :to="{ name: 'contact', query: { id: this.id } }"
        >צור קשר</router-link
      >
      <router-link :to="{ name: 'about', query: { id: this.id } }"
        >מי אנחנו</router-link
      >
      <router-link to="/" class="logo"
        ><img src="/images\logosh.png" height="18px"
      /></router-link>
    </div>
    <div>
      <img src="/images\logowhite.png" width="30%" class="contentfp" />
      <router-link to="/existing"
        ><button class="exist">קבוצה קיימת</button></router-link
      >
      <router-link to="/newgroup"
        ><button class="new">צור קבוצה</button></router-link
      >
    </div>
  </div>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      id: 0
    };
  },
  created() {
    this.id = this.$route.query.id;
  }
};
</script>
<style scoped>
.exist {
  margin-left: 38%;
}
.new {
  margin-left: 3%;
}
</style>
