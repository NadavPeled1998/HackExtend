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
      <span v-if="username" @click="logout">התנתק</span>
      <router-link
        v-if="falseuser"
        :to="{ name: 'home', query: { id: this.id } }"
        class="logo"
        ><img src="/images\logosh.png" height="18px"
      /></router-link>
      <router-link class="signLink" v-if="falseuser" to="/sign">
        הרשם/התחבר</router-link
      >
      <router-link
        v-if="username"
        :to="{ name: 'home', query: { id: this.id } }"
        class="logo"
        ><img src="/images\logosh.png" height="18px"
      /></router-link>
    </div>
    <div>
      <img src="/images\logowhite.png" width="30%" class="contentfp" />
      <router-link :to="{ name: 'existing', query: { id: this.id } }"
        ><button class="exist">קבוצה קיימת</button></router-link
      >
      <router-link :to="{ name: 'newgroup', query: { id: this.id } }"
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
      id: 0,
      username: false,
      falseuser: false
    };
  },
  created() {
    this.id = this.$route.query.id;
  },
  mounted() {
    const path = `http://localhost:5000/user/${this.id}`;
    this.$http
      .get(path)
      .then(res => {
        if (res.data.login == "True") {
          this.username = true;
          this.falseuser = false;
        } else {
          this.username = false;
          this.falseuser = true;
        }
      })
      .catch(error => {
        this.falseuser = true;
        this.username = false;
        console.log(error);
      });
  },
  methods: {
    logout() {
      const payload = {
        id: this.id
      };
      this.out(payload);
    },
    out(payload) {
      const path = `http://localhost:5000/login`;
      this.$http.post(path, payload).then(() => {
        this.username = false;
        this.falseuser = true;
      });
    }
  }
};
</script>
<style scoped>
.exist {
  margin-left: 40%;
}
.new {
  margin-left: 3%;
}
</style>
