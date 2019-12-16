<template>
  <div>
    <div class="topnav">
      <router-link :to="{ name: 'home', query: { id: this.id } }"
        >בית</router-link
      >
      <router-link to="/newgroup"> צור קבוצה</router-link>
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
       <router-link v-if="!username" :to="{ name: 'home', query: { id: this.id } }" class="logo"
        ><img src="/images\logosh.png" height="18px"
      /></router-link>
      <router-link class="signLink" v-if="!username" to="/sign">
        הרשם/התחבר</router-link
      >
      <router-link v-if="username" :to="{ name: 'home', query: { id: this.id } }" class="logo"
        ><img src="/images\logosh.png" height="18px"
      /></router-link>
    </div>
    <div v-if="falseuser" class="username">
      <div class="sign signin" v-if="Sign">
        <p>הרשם לאתר:</p>
        <label>שם משתמש:</label>
        <input type="text" @input="Check" class="Susername" />
        <div v-if="CheckUser" class="comment">
          שם המשתמש {{ Susername }} <span v-if="aviable">זמין</span
          ><span v-if="!aviable">לא זמין</span>
        </div>
        <label>דוא"ל:</label>
        <input type="email" class="Semail" />
        <label>סיסמא:</label>
        <input type="password" class="Spassword" />
        <div class="email">{{ Msign }}</div>
        <button @click="sign">הירשם</button>
        <p class="forgot" @click="aaa">
          יש לך כבר משתמש?
        </p>
      </div>
      <div class="sign login" v-if="Login">
        <p>התחבר</p>
        <label>שם משתמש:</label>
        <input type="text" class="Lusername" />
        <label>סיסמא:</label>
        <input type="password" class="Lpassword" />
        <div class="Mlogin">{{ Mlogin }}</div>
        <button @click="login">התחבר</button>

        <p class="forgot">
          <span
            class="user"
            @click="
              Sign = true;
              Login = false;
            "
            >צור משתמש חדש
          </span>
          <span class="pass">שכחתי את הסיסמא </span>
        </p>
      </div>
    </div>
    <div v-if="username" class="sign welcome">{{ user }}, ברוך הבא!</div>
  </div>
</template>
<script>
export default {
  name: "numbers",
  data() {
    return {
      username: false,
      falseuser: true,
      user: "",
      Sign: true,
      Login: false,
      id: 0,
      Msign: "",
      Mlogin: "",
      CheckUser: false
    };
  },
  mounted() {
    console.log(this.id);
    const path = `http://localhost:5000/user/${this.id}`;
    this.$http.get(path).then(res => {
      if (res.data.login == "True") {
        this.username = true;
        this.falseuser = false;
        console.log(res.data);
        this.GetGroups(this.id);
      } else {
        this.username = false;
        this.falseuser = true;
        console.log(res.data);
      }
    });
  },
  methods: {
    sign() {
      let Susername = document.querySelector(".Susername").value;
      let Semail = document.querySelector(".Semail").value;
      let Spassword = document.querySelector(".Spassword").value;
      const pay = {
        email: Semail,
        gmail: true
      };
      const payload = {
        username: Susername,
        password: Spassword,
        email: Semail
      };
      console.log(payload);
      this.CheckEmail(pay, payload);
    },
    SignIn(payload) {
      const path = `http://localhost:5000/users`;
      this.$http
        .post(path, payload)
        .then(res => {
          console.log(payload);
          console.log(res.data);
          this.id = res.data.userInfo;
          this.username = true;
          this.falseuser = false;
          this.Groups = [];
          this.teams = [];
        })
        .catch(error => {
          console.log(error);
        });
    },
    CheckEmail(pay, payload) {
      const path = `http://localhost:5000/check`;
      this.$http
        .post(path, pay)
        .then(res => {
          console.log(res.data.email);
          if (res.data.email == true) {
            this.SignIn(payload);
          } else {
            this.Msign = "המייל קיים במערכת";
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    Check() {
      let Susername = document.querySelector(".Susername").value;
      this.CheckUser = false;
      if (Susername.length > 5 && Susername.length < 13) {
        this.CheckUser = true;
        console.log(this.CheckUser);
        this.Susername = Susername;
        this.user = Susername;
        const payload = {
          username: Susername,
          name: true
        };
        console.log(payload);
        this.CheckUserName(payload);
      }
    },
    CheckUserName(payload) {
      const path = `http://localhost:5000/check`;
      this.$http
        .post(path, payload)
        .then(res => {
          this.aviable = res.data.name;
          console.log(this.aviable);
        })
        .catch(error => {
          console.log(error);
        });
    },
    login() {
      let Lusername = document.querySelector(".Lusername");
      let Lpassword = document.querySelector(".Lpassword");
      this.user = Lusername.value;
      console.log(this.user);
      const payload = {
        username: Lusername.value,
        password: Lpassword.value,
        login: "True"
      };
      console.log(payload);
      this.Log(payload);
    },
    Log(payload) {
      const path = `http://localhost:5000/login`;
      this.$http
        .post(path, payload)
        .then(res => {
          console.log(res.data);
          if (res.data.message == "not vaild username") {
            this.Mlogin = "שם משתמש לא קיים במערכת";
            console.log("hello");
          } else if (res.data.message == "wrong password") {
            this.Mlogin = "שם משתמש או סיסמא לא נכונים";
          } else {
            console.log(res);
            this.Mlogin = "";
            this.username = true;
            this.falseuser = false;
            this.id = res.data.userInfo;
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
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
<style>
.sign {
  margin-top: 5%;
  margin-left: 40%;
}
.user {
  margin-right: 10%;
  float: right;
  cursor: pointer;
}
.pass {
  margin-left: -30%;
  float: left;
  cursor: pointer;
}
.disconnect {
  text-align: center;
  color: white;
  font-size: 80px;
  margin-bottom: 3%;
  margin-top: 2.5%;
}
.welcome {
  direction: rtl;
  /*margin-left: 40%;
  padding: 200px 200px;*/
  padding: 200px;
  margin-left: 35%;
  margin-right: -20%;
}
</style>
