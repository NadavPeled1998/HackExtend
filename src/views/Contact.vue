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
      <router-link :to="{ name: 'home', query: { id: this.id } }" class="logo"
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
      <span>contact@shmirot.com</span>
    </div>
  </div>
</template>
<script>
export default {
  name: "contact",
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
.contact {
  direction: rtl;
  margin-right: 30%;
  margin-top: 7.5%;
  color: white;
  font-size: 40px;
  font-weight: bold;
}
span {
  margin-right: 40%;
  color: blue;
  font-family: "Varela Round", sans-serif;
  text-decoration: underline;
  font-size: 20px;
}
</style>
