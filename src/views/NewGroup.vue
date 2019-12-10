<template>
  <div class="home">
    <div class="topnav">
      <router-link :to="{ name: 'home', query: { id: this.id } }"
        >בית</router-link
      >
      <router-link to="/newgroup" class="active"> צור קבוצה</router-link>
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
    <div class="kamahav" v-if="Next">
      <p>כמה חברים יש בקבוצה?</p>
      <el-input-number
        v-model="num"
        class="input"
        @change="numbers"
        :min="2"
        :max="100"
      ></el-input-number>
    </div>
    <div class="admatai" v-show="Next">
      <p>מתי מתחילה השמירה? ועד מתייי?</p>

      <div class="timepart" :class="{ error: s || e }">
        <div class="hatchala">
          <input type="time" class="time" />
          סיום
        </div>
        <div class="hatchala">
          <input type="time" class="time" />
          התחלה
        </div>
      </div>
    </div>
    <div class="buttons" v-if="Next">
      <button @click="Allrandom" class="button">רשימה רנדומלית</button>
      <button @click="noChange" class="button">רשימה לפי הסדר</button>
    </div>
    <div v-if="Next" class="Ma">
      <p class="ma">מה השמות שלכם?</p>
      <div class="names" v-show="Next" :class="{ error: k }"></div>
    </div>
    <div v-show="results">
      <div class="result"></div>
      <div v-if="username">
        <button @click="save" v-if="!saved" class="save">
          שמור בשם
        </button>
        <button v-if="saved" class="saved">נשמר</button>
        <router-link to="/" v-if="!saved" class="DontSave"
          >אל תשמור</router-link
        >
      </div>
      <div v-if="!username">
        <p>
          בשביל לשמור את הקבוצה ולהשתמש בה שוב ושוב יש
          <button
            @click="
              Sign = true;
              log = false;
            "
          >
            להירשם לאתר
          </button>
          או
          <button
            @click="
              log = true;
              Sign = false;
            "
          >
            להתחבר למשתמש קיים
          </button>
        </p>
        <div class="sign signin" v-if="Sign">
          <p>הרשם לאתר:</p>
          <label>שם משתמש:</label>
          <input type="text" @input="Check" class="Susername" />
          <div v-if="CheckUser">
            שם המשתמש {{ Susername }} <span v-if="aviable">זמין</span
            ><span v-if="!aviable">לא זמין</span>
          </div>
          <label>דוא"ל:</label>
          <input type="email" class="Semail" />
          <label>סיסמא:</label>
          <input type="password" class="Spassword" />
          <div>{{ Msign }}</div>
          <button @click="sign">הירשם</button>
        </div>
        <div class="sign login" v-if="log">
          <p>יש לך כבר משתמש קיים?</p>
          <label>שם משתמש:</label>
          <input type="text" class="Lusername" />
          <label>סיסמא:</label>
          <input type="password" class="Lpassword" />
          <div>{{ Mlogin }}</div>
          <button @click="login">התחבר</button>
          <p class="forgot">שכחת את הסיסמא?</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "newgroup",
  data() {
    return {
      Groups: [],
      Group: {
        title: "",
        run: 1
      },
      Mlogin: "",
      Msign: "",
      num: 2,
      name: [],
      fl: [],
      index: [],
      log: false,
      Sign: false,
      Next: true,
      id: 0,
      val: 2,
      oval: 2,
      saved: false,
      negative: false,
      results: false,
      start: "",
      end: "",
      arr: [],
      hour1: [],
      minute1: [],
      k: false,
      s: false,
      e: false,
      group: "",
      run: 1,
      names: [],
      username: false,
      Susername: "",
      aviable: "",
      CheckUser: false
    };
  },
  created() {
    this.id = this.$route.query.id;
  },
  mounted() {
    console.log(this.id);
    if (this.id !== 0) {
      this.username = true;
      console.log(this.username);
    }
    console.log(this.id);
    let names = document.querySelector(".names");
    for (let i = 0; i < 2; i++) {
      let div = document.createElement("DIV");
      let x = document.createElement("INPUT");
      x.className = "name";
      x.setAttribute("type", "text");
      names.appendChild(div);
      names.appendChild(x);
    }
  },
  methods: {
    numbers() {
      let input = document.querySelectorAll(".name");
      if (input.length > this.num) {
        console.log("hello");
        //let inp = input.length
        for (let i = 0; i < this.oval; i++) {
          let inputs = document.querySelectorAll(".name");
          if (inputs.length > this.num) {
            let names = document.querySelector(".names");
            input = document.querySelectorAll(".name");
            names.removeChild(input[input.length - 1]);
          } else {
            console.log(input.length);
            console.log("shit");
            break;
          }
        }
      } else {
        console.log("hey");
        let num = this.num - input.length;
        console.log("num " + num);
        for (let i = 0; i < num; i++) {
          let names = document.querySelector(".names");
          let div = document.createElement("DIV");
          let x = document.createElement("INPUT");
          x.className = "name";
          x.setAttribute("type", "text");
          names.appendChild(div);
          names.appendChild(x);
        }
        this.oval = this.num;
      }
    },
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
      this.CheckEmail(pay, payload);
    },
    SignIn(payload) {
      const path = `http://localhost:5000/users`;
      this.$http
        .post(path, payload)
        .then(res => {
          console.log("payload");
          console.log(payload);
          console.log("res");
          console.log(res.data);
          this.id = res.data.message;
          console.log("id");
          console.log(this.id);
          this.username = true;
          this.Groups = [];
          this.teams = this.Groups;
          this.ex = true;
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
          if (res.data.email == true) {
            this.SignIn(payload);
          } else {
            this.Msign = "יש כבר משתמש עם המייל הזה";
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
        this.Susername = Susername;
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
        })
        .catch(error => {
          console.log(error);
        });
    },
    login() {
      let Lusername = document.querySelector(".Lusername");
      let Lpassword = document.querySelector(".Lpassword");
      const payload = {
        username: Lusername.value,
        password: Lpassword.value,
        get: true
      };
      console.log(payload);
      this.Log(payload);
    },
    Log(payload) {
      const path = `http://localhost:5000/groups`;
      this.$http
        .post(path, payload)
        .then(res => {
          if (res.data.message == "not vaild useranme") {
            this.Mlogin = "שם משתמש לא קיים במערכת";
            console.log("hello");
          } else if (res.data.message == "worng password") {
            this.Mlogin = "שם משתמש או סיסמא לא נכונים";
          } else {
            this.Mlogin = "";
            this.username = true;
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    MakeArray() {
      let inputs = document.querySelectorAll(".name");
      for (let i = 0; i < inputs.length; i++) {
        if (!inputs[i].value) {
          this.k = true;
          break;
        } else {
          this.k = false;
        }
      }
      console.log(this.k);
      if (!this.k) {
        const Time = document.querySelectorAll(".time");
        this.start = Time[1].value;
        this.end = Time[0].value;
        console.log(this.start);
        console.log(this.end);
        if (this.start.length < 4) {
          this.s = true;
        } else {
          this.s = false;
        }
        if (this.end.length < 4) {
          this.e = true;
        } else {
          this.e = false;
        }
        if (!this.s && !this.e) {
          console.log(inputs.length);
          for (let i = 0; i < inputs.length; i++) {
            this.arr[i] = {};
            this.arr[i].name = inputs[i].value;
            console.log(inputs[i].value);
            this.arr[i].fl = 0;
            console.log(this.arr[i]);
            this.arr[i].index = 0;
          }
          console.log(this.arr);
          this.Next = false;
          let Shour = Number(this.start.charAt(0) + this.start.charAt(1));
          let Sminute = Number(this.start.charAt(3) + this.start.charAt(4));
          let Ehour = Number(this.end.charAt(0) + this.end.charAt(1));
          let Eminute = Number(this.end.charAt(3) + this.end.charAt(4));
          let hours = Ehour - Shour;
          if (Shour > Ehour) {
            hours += 24;
          }
          if (Shour == Ehour && Sminute > Eminute) {
            hours += 24;
          }
          let minutes = Eminute - Sminute;
          let all = hours * 60 + minutes;
          let shmira = Math.round(all / this.arr.length);
          let hour2 = Math.floor(shmira / 60);
          let minute2 = shmira % 60;
          for (let i = 1; i <= this.arr.length; i++) {
            this.hour1[i - 1] = hour2 * i;
            this.minute1[i - 1] = minute2 * i;
            this.hour1[i - 1] += Shour;
            this.minute1[i - 1] += Sminute;
            if (this.minute1[i - 1] >= 60) {
              this.hour1[i - 1] += Math.floor(this.minute1[i - 1] / 60);
              this.minute1[i - 1] = this.minute1[i - 1] % 60;
            }
            if (this.hour1[i - 1] > 23) {
              this.hour1[i - 1] -= 24;
            }
          }
        }
      }
    },
    MathRandom() {
      for (let i = 0; i < this.arr.length; i++) {
        this.arr[i].random = Math.random();
      }
    },
    random() {
      console.log("random");
      console.log(this.arr);
      let randomNumbers = [];
      for (let i = 0; i < this.arr.length; i++) {
        randomNumbers.unshift(this.arr[i].random);
      }
      randomNumbers.sort();
      console.log(randomNumbers);
      console.log(this.arr);
      let randomize = [];
      for (let k = 0; k < this.arr.length; k++) {
        for (let i = 0; i < this.arr.length; i++) {
          if (this.arr[k].random == randomNumbers[i]) {
            randomize[i] = this.arr[k];
          } else {
            continue;
          }
        }
      }
      for (let i = 0; i < this.arr.length; i++) {
        if (randomize[0] === this.arr[i].id) this.arr[0].fl = 1;
        this.arr[this.arr.length - 1].fl = 1;
      }
      this.results = true;
      let result = document.querySelector(".result");
      for (let i = 0; i < this.arr.length; i++) {
        if (this.hour1[i] < 10) {
          this.hour1[i] = "0" + this.hour1[i];
        }
        if (this.minute1[i] < 10) {
          this.minute1[i] = "0" + this.minute1[i];
        }
        let div = document.createElement("DIV");
        result.appendChild(div);
        if (i == 0) {
          div.innerHTML =
            randomize[i].name +
            " " +
            this.start +
            " - " +
            this.hour1[i] +
            ":" +
            this.minute1[i];
        } else if (i == this.arr.length - 1) {
          div.innerHTML =
            randomize[i].name +
            " " +
            this.hour1[i - 1] +
            ":" +
            this.minute1[i - 1] +
            " - " +
            this.end;
        } else {
          div.innerHTML =
            randomize[i].name +
            " " +
            this.hour1[i - 1] +
            ":" +
            this.minute1[i - 1] +
            " - " +
            this.hour1[i] +
            ":" +
            this.minute1[i];
        }
      }
      randomize[0].fl = 1;
      randomize[randomize.length - 1].fl = 1;
      this.arr = randomize;
      for (let i = 0; i < this.arr.length; i++) {
        this.arr[i].index = i;
      }
      console.log(randomize);
      let run = document.createElement("DIV");
      run.innerHTML = "סבב: 1";
      result.appendChild(run);
    },
    Allrandom() {
      this.MakeArray();
      if (!this.k && !this.s && !this.e) {
        this.MathRandom();
        this.random();
      }
    },
    noChange() {
      this.MakeArray();
      if (!this.k && !this.s && !this.e) {
        this.arr[0].fl = 1;
        this.arr[this.arr.length - 1].fl = 1;
        for (let i = 0; i < this.arr.length; i++) {
          this.arr[i].index = i;
        }
        this.results = true;
        let result = document.querySelector(".result");
        for (let i = 0; i < this.arr.length; i++) {
          if (this.hour1[i] < 10) {
            this.hour1[i] = "0" + this.hour1[i];
          }
          if (this.minute1[i] < 10) {
            this.minute1[i] = "0" + this.minute1[i];
          }
          let div = document.createElement("DIV");
          result.appendChild(div);
          if (i == 0) {
            div.innerHTML =
              this.arr[i].name +
              " " +
              this.start +
              " - " +
              this.hour1[i] +
              ":" +
              this.minute1[i];
          } else if (i == this.arr.length - 1) {
            div.innerHTML =
              this.arr[i].name +
              " " +
              this.hour1[i - 1] +
              ":" +
              this.minute1[i - 1] +
              " - " +
              this.end;
          } else {
            div.innerHTML =
              this.arr[i].name +
              " " +
              this.hour1[i - 1] +
              ":" +
              this.minute1[i - 1] +
              " - " +
              this.hour1[i] +
              ":" +
              this.minute1[i];
          }
        }
        this.arr[0].fl = 1;
        this.arr[this.arr.length - 1].fl = 1;
        let run = document.createElement("DIV");
        run.innerHTML = "סבב: 1";
        result.appendChild(run);
      }
    },
    GetGroups() {
      const path = `http://localhost:5000/groups`;
      this.$http
        .get(path)
        .then(res => {
          this.Groups = res.data.groups;
          console.log(this.Groups);
        })
        .catch(e => {
          console.log(e);
        });
    },
    AddGroups(payload) {
      const path = `http://localhost:5000/groups`;
      this.$http
        .post(path, payload)
        .then(() => {
          this.GetGroups();
        })
        .catch(error => {
          console.log(error);
          this.GetGroups();
        });
    },
    save() {
      this.GetGroups();
      let group = prompt("איך לקרוא לקבוצה?");
      this.Group.title = group;
      this.Group.run = 1;
      for (let i = 0; i < this.arr.length; i++) {
        this.name.push(this.arr[i].name);
        this.fl.push(this.arr[i].fl);
        this.index.push(this.arr[i].index);
      }
      const payload = {
        title: this.Group.title,
        run: this.Group.run,
        name: this.name,
        fl: this.fl,
        index: this.index,
        add: true,
        id: this.id
      };
      this.AddGroups(payload);
      this.saved = true;
    }
  }
};
</script>
<style scoped>
p {
  direction: rtl;
  color: white;
  font-size: 75px;
}
.kamahav {
  display: block;
  margin-right: 10%;
  margin-top: 1%;
  margin-left: 30%;
}
.Ma {
  margin-top: 0%;
}
.ma {
  margin-top: 8%;
  margin-right: 65%;
}
.input {
  margin-right: 70%;
}
.admatai {
  direstion: rtl;
  display: inline-block;
  margin-right: 15%;
  margin-top: 10%;
  padding-left: 17%;
}
.button {
  margin-right: 10px;
  padding: 20px;
  font-size:20px;
}
.buttons {
  display: block;
  /*padding-left:300px;
  padding-right: 300px;*/
  direction: rtl;
  float: right;
  margin-right: 48%;
  margin-top: 3%;
}
.save {
  margin-left: 38%;
}
.saved {
  margin-left: 46.5%;
}
.DontSave {
  background-color: #4caf50; /* Green */
  border: none;
  color: white;
  padding: 15px 40px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  border-radius: 8px;
  margin-left: 3%;
  /*margin-right:50%;*/
  -webkit-transition-duration: 0.4s; /* Safari */
  transition-duration: 0.4s;
}
</style>
