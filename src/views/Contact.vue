<template>
  <div>
    <div class="topnav">
      <router-link :to="{ name: 'home', query: { id: this.id } }"
        >בית</router-link
      >
      <router-link :to="{ name: 'newgroup', query: { id: this.id } }">
        צור קבוצה</router-link
      >
      <router-link :to="{ name: 'existing', query: { id: this.id } }"
        >קבוצות קיימות</router-link
      >
      <router-link to="/contact" class="active">צור קשר</router-link>
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
    <div class="contact">
      <h2>
        צור קשר
      </h2>
      <p>
        אם נתקלתם בבעיה כלשהי בשימוש באתר,
      </p>
      <p>אתם יותר ממוזמנים לפנות אלינו במייל:</p>
      <div class="span">
        contact@shmirot.com <i class="el-icon-message"></i>
      </div>
    </div>
  </div>
</template>
<script>
//import port from "../../server/Server.py";


export default {
  name: "contact",
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
    this.$http.get(path).then(res => {
      if (res.data.login == "True") {
        this.username = true;
        this.falseuser = false;
      } else {
        this.username = false;
        this.falseuser = true;
      }
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
        this.id = 0;
        this.username = false;
        this.falseuser = true;
      });
    }
  }
};
</script>
<style scoped>
.contact {
  direction: rtl;
  margin-right: 30%;
  margin-top: 5%;
  padding-bottom: 300px;
  color: white;
  font-size: 50px;
}
.span {
  margin-top: 7.5%;
  margin-right: 27.5%;
  color: white;
  font-family: "Varela Round", sans-serif;
  /*text-decoration: underline;*/
  font-size: 25px;
}
h2 {
  margin-bottom: 10%;
}
</style>
