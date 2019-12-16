<template>
  <div class="mi">
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
      <router-link :to="{ name: 'contact', query: { id: this.id } }"
        >צור קשר</router-link
      >
      <router-link to="/about" class="active">מי אנחנו</router-link>
      <span v-if="username" @click="logout">התנתק</span>
       <router-link v-if="falseuser" :to="{ name: 'home', query: { id: this.id } }" class="logo"
        ><img src="/images\logosh.png" height="18px"
      /></router-link>
      <router-link class="signLink" v-if="falseuser" to="/sign">
        הרשם/התחבר</router-link
      >
      <router-link v-if="username" :to="{ name: 'home', query: { id: this.id } }" class="logo"
        ><img src="/images\logosh.png" height="18px"
      /></router-link>
    </div>
    <div class="about">
      <h2>
        מי אנחנו?
      </h2>
      <div>
        <p>
          אנחנו אתם, חיילים שבזבזו את הזמן שלהם בליצור רשימת שמירה, בלריב
        </p>
        <p>
          מי שומר ראשון ומי שומר אחרון ותמיד להרגיש שאיכשהו נדפקת בסוף.
        </p>
      </div>
      <div class="solution">
        <p>
          אנחנו מביאים פתרון פשוט לכולם, תרשמו
        </p>
        <p>
          את השמות של החברים שלכם
        </p>
        ואנחנו כבר נדאג שכולם יהיו מרוצים, עלינו (;
      </div>
    </div>
  </div>
</template>
<script>
export default {
  //<img src="/images\mianachnu.png" width="30%" class="contentfp" />
  name: "Mi",
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
          this.falseuser= false;
          console.log(this.username);
          console.log(res.data);
        } else {
          this.username = false;
          this.falseuser= true;
          console.log(res.data);
        }
      })
      .catch(error => {
        this.username = false;
         this.falseuser= true;
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
        this.id = 0;
        this.username = false;
         this.falseuser= true;
      });
    }
  }
};
</script>
<style scoped>
.about {
  direction: rtl;
  direction: rtl;
  margin-right: 25%;
  margin-top: 5%;
  border: soild black 1px;
  color: white;
  font-size: 50px;
}
h2 {
  margin-bottom: 10%;
}
.solution {
  margin-top: 7.5%;
}
</style>
