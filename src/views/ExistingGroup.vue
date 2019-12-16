<template>
  <div>
    <div class="topnav">
      <router-link :to="{ name: 'home', query: { id: this.id } }"
        >בית</router-link
      >
      <router-link :to="{ name: 'newgroup', query: { id: this.id } }">
        צור קבוצה</router-link
      >
      <router-link to="/existing" class="active">קבוצות קיימות</router-link>
      <router-link :to="{ name: 'contact', query: { id: this.id } }"
        >צור קשר</router-link
      >
      <router-link :to="{ name: 'about', query: { id: this.id } }"
        >מי אנחנו</router-link
      >
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
    <div v-if="falseuser" class="username">
      <p class="disconnect">
        בשביל להשתמש בקבוצות קיימות יש להתחבר למשתמש קיים או ליצור חדש.
      </p>
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
        <p
          class="forgot"
          @click="
            Sign = false;
            Login = true;
          "
        >
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
        <p
          class="forgot"
          @click="
            Sign = true;
            Login = false;
          "
        >
          <span class="user">צור משתמש חדש </span>
          <span class="pass">שכחתי את הסיסמא </span>
        </p>
      </div>
    </div>
    <div v-if="username">
      <div v-if="!n">
        <div v-if="ex" class="loya">
          <p>אין קבוצות קיימות למשתמש זה</p>
         <router-link
          :to="{ name: 'newgroup', query: { id: this.id } }"
          class="FNewGroup"
          >צור קבוצה חדשה</router-link
        >
        </div>
        <div v-if="!ex">
          <div class="container">
            <h5 class="loya">בחר קבוצה</h5>
            <steam
              @show-team="showTeam"
              v-for="team in teams"
              :key="team.id"
              :id="team.id"
              :group="team.title"
            >
            </steam>
          </div>
        </div>
        <router-link
          :to="{ name: 'newgroup', query: { id: this.id } }"
          class="NewGroup" v-if="!ex"
          >צור קבוצה חדשה</router-link
        >
      </div>
      <div v-if="n && !edi && !results">
        <button @click="back" class="back">חזור</button>
        <button @click="Edit" class="edit">ערוך</button><br />
        <button @click="DeleteGroup" class="DeleteGroup">מחק קבוצה</button>
        <div>
          <div class="memebersh">
            <h5>{{ g.group }}</h5>
          </div>
        </div>
        <div class="members">
          <div v-for="member in members" :key="member.id" class="member">
            {{ member.name }}
          </div>
        </div>
        <div class="admatai">
          <p class="p">מתי מתחילה השמירה? ועד מתייי?</p>

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
        <div class="buttons">
          <button @click="Allrandom" class="button">רשימה רנדומלית</button>
          <button @click="FairRandom" class="button">רנדומליות הוגנת</button>
          <button @click="NoChange" class="button">אותו הסדר</button>
          <button @click="KeepForward" class="button">
            אותו הסדר, אחד קדימה
          </button>
        </div>
      </div>
      <div v-if="edi">
        <button @click="Save" class="back">חזור</button>
        <button @click="Add" v-if="edi" class="edit">הוסף</button><br />
        <div class="inp" v-for="member in members" :key="member.id">
          <div v-show="member.id" class="result resulted">
            <less @less="less" :id="member.id"> </less>
            <div class="Mname">{{ member.name }}</div>
            <div class="div">
              <button
                v-show="member.id"
                class="EditName"
                @click="EditName(member.id)"
              >
                <i class="el-icon-edit"></i>
              </button>
            </div>
          </div>
          <input
            v-if="!member.id"
            type="text"
            class="names"
            :class="{ error: !k }"
            :value="member.name"
          />
          <button
            v-show="!member.id"
            class="SaveName"
            @click="EditedName(member.id)"
          >
            שמור שם
          </button>
        </div>
        <div v-if="!k">אל תשאירו שדות ריקים</div>
      </div>
      <div v-show="results">
        <div class="result">
          <div class="system">{{ system }}</div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import steam from "@/components/team.vue";
import less from "@/components/less.vue";

export default {
  name: "Exist",
  components: {
    steam,
    less
  },
  data() {
    return {
      Sign: true,
      Login: false,
      Groups: [],
      id: 0,
      username: false,
      falseuser: false,
      Susername: "",
      Msign: "",
      CheckUser: false,
      aviable: true,
      Mlogin: "",
      g: 0,
      run: 2,
      ex: true,
      n: false,
      s: false,
      e: false,
      teams: [],
      members: [],
      start: "",
      end: "",
      arr: [],
      hour1: [],
      minute1: [],
      edi: false,
      results: false,
      l: [],
      k: true,
      beid: 0,
      ed: true,
      system: ""
    };
  },
  created() {
    this.id = this.$route.query.id;
  },
  mounted() {
    console.log(this.id);
    const path = `http://localhost:5000/user/${this.id}`;
    this.$http
      .get(path)
      .then(res => {
        if (res.data.login == "True") {
          this.username = true;
          this.falseuser = false;
          console.log(res.data);
          this.GetGroups(this.id);
        } else {
          this.falseuser = true;
          this.username = false;
          console.log(res.data);
        }
      })
      .catch(error => {
        this.falseuser = true;
        this.username = false;
        console.log(error);
      });
  },
  methods: {
    conected() {
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
    sign() {
      let Susername = document.querySelector(".Susername").value;
      let Semail = document.querySelector(".Semail").value;
      let Spassword = document.querySelector(".Spassword").value;
      console.log(Spassword);
      console.log(Susername);
      console.log(Semail);
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
          console.log(res);
          this.username = true;
          this.falseuser= false;
          this.id = res.data.userInfo
          this.Groups = [];
          this.teams = [];

          this.ex= true;
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
    GetGroups(id) {
      const path = `http://localhost:5000/groups/${id}`;
      this.$http
        .get(path)
        .then(res => {
          this.Groups = res.data.groups;
          console.log(res.data)
          console.log(this.Groups)
          this.teams = this.Groups;
          console.log(this.Groups);
          this.ex = true;
          if (this.Groups.length > 0) {
            this.ex = false;
            console.log(this.ex)
          }
          console.log(this.ex)
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
            console.log(this.id);
            this.GetGroups(this.id);
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    GetMembers(id) {
      const path = `http://localhost:5000/group/${id}`;
      this.$http.get(path).then(res => {
        this.members = res.data.Member;
        console.log(res.data);
      });
    },
    showTeam(id) {
      //const team = this.teams.find(team => team.id == id);
      this.g = id;
      for (let i = 0; i < this.Groups.length; i++) {
        if (this.g === this.Groups[i].id) {
          this.run = this.Groups[i].run;
          console.log(this.run);
        }
      }
      this.n = true;
      this.GetMembers(id);
    },
    back() {
      this.n = false;
      this.GetGroups(this.id);
    },
    Edit() {
      this.edi = true;
      //this.editor = true;
    },
    EditName(id) {
      if (this.ed) {
        //console.log(id);
        const member = this.members.find(member => member.id == id);
        //console.log(member);
        for (let i = 0; i < 1; i++) {
          this.beid = member.id;
        }
        member.id = false;
        this.ed = false;
      }
    },
    EditedName(id) {
      let input = document.querySelector(".names");
      let member;
      if (input.value) {
        this.k = true;
        if (id === false) {
          member = this.members.find(member => member.id == id);
          member.id = this.beid;
          member.name = input.value;
          const payload = {
            name: member.name 
          };
          this.ed = true;
          this.UpdateName(payload, member.id);
        } else {
          let fll = [];
          for (let i = 1; i < this.members.length; i++) {
            fll.push(this.members[i].fl);
          }
          this.members[0].fl = Math.min(...fll);
          this.members[0].name = input.value;
          this.members[0].index = 0;
          const payload = {
            name: input.value,
            fl: this.members[0].fl,
            index: this.members[0].index
          };
          this.AddName(payload, this.g);
        }
      } else {
        this.k = false;
        input.value = "";
      }
    },
    UpdateName(payload, ID) {
      const path = `http://localhost:5000/group/${ID}/member`;
      this.$http
        .put(path, payload)
        .then(() => {
          this.GetGroups();
        })
        .catch(error => {
          console.log(error);
          this.GetGroups;
        });
    },
    Add() {
      this.members.unshift({});
    },
    AddName(payload, ID) {
      const path = `http://localhost:5000/group/${ID}`;
      this.$http
        .post(path, payload)
        .then(() => {
          this.GetMembers(this.g);
        })
        .catch(error => {
          console.log(error);
          this.GetGroups;
        });
    },

    less(id) {
      const member = this.members.find(member => member.id == id);
      console.log(member.id);
      for (let i = 0; i < this.members.length; i++) {
        if (this.members[i].id === id) {
          let sp = this.members.splice(i, 1);
          console.log(sp);
        }
      }
      let inps = document.querySelectorAll(".inp");
      console.log(inps);
      let inp;
      console.log(inp);
      if (inps.length > 2) {
        if (this.l.length < 1) {
          console.log("hello");
          for (let i = 0; i <= this.members.length; i++) {
            if (member.id == i) {
              inp = inps[i - 1];
              break;
            } else {
              continue;
            }
          }
        } else {
          let x = 1;
          for (let i = 0; i < this.l.length; i++) {
            if (member.id > this.l[i]) {
              x += 1;
            } else {
              continue;
            }
          }
          for (let i = 0; i < inps.length; i++) {
            if (member.id - x == i) {
              inp = inps[i];
              break;
            } else {
              continue;
            }
          }
        }
        this.l.push(member.id);
        this.DeleteName(member.id);
        //inp.parentNode.removeChild(inp);
      }
    },
    DeleteName(id) {
      const path = `http://localhost:5000/group/${id}/member`;
      this.$http
        .delete(path)
        .then(() => {
          this.GetGroups();
        })
        .catch(error => {
          console.log(error);
          this.GetGroups();
        });
    },
    DeleteGroup() {
      if (
        confirm(
          "אם תמחק את הקבוצה הזאת כל ההיסטוריה שלה תמחק ביחד איתה. אתה בטוח שאתה רוצה לעשות את זה?"
        )
      ) {
        this.DG(this.g);
      }
    },
    DG(id) {
      const path = `http://localhost:5000/group/${id}`;
      this.$http
        .delete(path)
        .then(() => {
          this.GetGroups(this.id);
          this.n = false;
        })
        .catch(error => {
          console.log(error);
          this.GetGroups();
        });
    },
    Save() {
      if (this.k) {
        this.edi = false;
        this.showTeam(this.g);
      }
    },
    MakeArray() {
      for (let i = 0; i < this.members.length; i++) {
        this.arr[i] = {};
        this.arr[i].name = this.members[i].name;
        this.arr[i].id = this.members[i].id;
        this.arr[i].fl = this.members[i].fl;
      }
      const Time = document.querySelectorAll(".time");
      this.start = Time[1].value;
      this.end = Time[0].value;
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
    },
    MathRandom() {
      for (let i = 0; i < this.arr.length; i++) {
        this.arr[i].random = Math.random();
      }
    },
    random() {
      let randomNumbers = [];
      for (let i = 0; i < this.arr.length; i++) {
        randomNumbers.unshift(this.arr[i].random);
      }
      randomNumbers.sort();
      console.log(randomNumbers);
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
        div.className = "result1";
        result.appendChild(div);
        if (i == 0) {
          div.innerHTML =
            randomize[i].name +
            " " +
            this.hour1[i] +
            ":" +
            this.minute1[i] +
            " - " + this.start 
        } else if (i == this.arr.length - 1) {
          div.innerHTML =
            randomize[i].name +
            " " +
            this.end +  " - " +
            this.hour1[i - 1] +
            ":" +
            this.minute1[i - 1]
        } else {
          div.innerHTML =
            randomize[i].name +
            " " +
            this.hour1[i] +
            ":" +
            this.minute1[i] +
            " - " +
            this.hour1[i - 1] +
            ":" +
            this.minute1[i - 1];
        }
      }
      for (let i = 0; i < randomize.length; i++) {
        randomize[i].index = i;
      }
      let run = document.createElement("DIV");
      this.run += 1;
      run.innerHTML = "סבב:" + this.run;
      result.appendChild(run);
      this.system = "רשימה רנדומלית";
      let idid = [];
      for (let i = 0; i < randomize.length; i++) {
        idid.push(randomize[i].id);
      }
      idid.sort(function(a, b) {
        return a - b;
      });
      console.log(idid);
      let ind = [];
      for (let k = 0; k < randomize.length; k++)
        for (let i = 0; i < randomize.length; i++) {
          if (idid[k] == randomize[i].id) {
            ind.push(randomize[i].index);
          } else {
            continue;
          }
        }
      const payload = {
        index: ind
      };
      this.UpdateIndex(payload, this.g);
    },
    Allrandom() {
      this.MakeArray();
      if (!this.s && !this.e) {
        this.MathRandom();
        this.random();
      }
    },
    NoChange() {
      this.MakeArray();
      if (!this.s && !this.e) {
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
          div.className = "result1";
          result.appendChild(div);
          if (i == 0) {
            div.innerHTML =
              this.arr[i].name +
              " " +
              this.hour1[i] +
              ":" +
              this.minute1[i] +
              " - " +
              this.start 
          } else if (i == this.arr.length - 1) {
            div.innerHTML =
              this.arr[i].name +
              " " + 
              this.end +  " - " +
              this.hour1[i - 1] +
              ":" +
              this.minute1[i - 1]
          } else {
            div.innerHTML =
              this.arr[i].name +
              " " +
              this.hour1[i] +
              ":" +
              this.minute1[i] +
              " - " +
              this.hour1[i-1] +
              ":" +
              this.minute1[i-1];
          }
        }
        let run = document.createElement("DIV");
        this.Group += 1;
        this.run += 1;
        run.innerHTML = "סבב:" + this.run;
        this.system = "אותו סדר";
        result.appendChild(run);
        let idid = [];
        let randomize = this.arr;
        for (let i = 0; i < randomize.length; i++) {
          randomize[i].index = i;
        }
        for (let i = 0; i < randomize.length; i++) {
          idid.push(randomize[i].id);
        }
        idid.sort(function(a, b) {
          return a - b;
        });
        let ind = [];
        for (let k = 0; k < randomize.length; k++)
          for (let i = 0; i < randomize.length; i++) {
            if (idid[k] == randomize[i].id) {
              ind.push(randomize[i].index);
            } else {
              continue;
            }
          }
        const payload = {
          index: ind
        };
        this.UpdateIndex(payload, this.g);
      }
    },
    KeepForward() {
      this.MakeArray();
      if (!this.s && !this.e) {
        let randomize = [];
        for (let i = 0; i < this.arr.length; i++) {
          if (i === 0) {
            randomize[0] = this.arr[this.arr.length - 1];
            continue;
          } else {
            randomize[i] = this.arr[i - 1];
          }
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
        div.className = "result1";
        result.appendChild(div);
        if (i == 0) {
          div.innerHTML =
            randomize[i].name +
            " " +
            this.hour1[i] +
            ":" +
            this.minute1[i] +
            " - " + this.start 
        } else if (i == this.arr.length - 1) {
          div.innerHTML =
            randomize[i].name +
            " " +
            this.end +  " - " +
            this.hour1[i - 1] +
            ":" +
            this.minute1[i - 1]
        } else {
          div.innerHTML =
            randomize[i].name +
            " " +
            this.hour1[i] +
            ":" +
            this.minute1[i] +
            " - " +
            this.hour1[i - 1] +
            ":" +
            this.minute1[i - 1];
        }
      }
        let run = document.createElement("DIV");
        this.run += 1;
        run.innerHTML = "סבב: " + this.run;
        result.appendChild(run);
        this.system = "אותו הסדר, אחד קדימה";
        for (let i = 0; i < randomize.length; i++) {
          randomize[i].index = i;
        }
        let idid = [];
        for (let i = 0; i < randomize.length; i++) {
          idid.push(randomize[i].id);
        }
        idid.sort(function(a, b) {
          return a - b;
        });
        let ind = [];
        for (let k = 0; k < randomize.length; k++)
          for (let i = 0; i < randomize.length; i++) {
            if (idid[k] == randomize[i].id) {
              ind.push(randomize[i].index);
            } else {
              continue;
            }
          }
        const payload = {
          index: ind
        };
        this.UpdateIndex(payload, this.g);
      }
    },
    FairRandom() {
      this.MakeArray();
      this.MathRandom();
      if (!this.s && !this.e) {
        let randomize = [];
        let randomy = [];
        let randomy1 = [];
        let fll = [];
        let arandom = [];
        for (let i = 0; i < this.arr.length; i++) {
          fll[i] = this.arr[i].fl;
        }
        for (let i = 0; i < this.arr.length; i++) {
          if (this.arr[i].fl === Math.min(...fll)) {
            randomy.push(this.arr[i]);
          } else {
            continue;
          }
        }
        if (randomy.length === 1) {
          randomize[0] = randomy[0];
          for (let i = 0; i < this.arr.length; i++) {
            if (randomize[0].id === this.arr[i].id) {
              continue;
            } else {
              arandom.unshift(this.arr[i].random);
            }
          }
          arandom.sort();
          for (let i = 0; i < this.arr.length; i++) {
            if (this.arr[i].random === Math.max(...arandom)) {
              randomize[this.arr.length - 1] = this.arr[i];
            }
          }
        } else {
          for (let i = 0; i < randomy.length; i++) {
            arandom.unshift(randomy[i].random);
          }
          arandom.sort();
          for (let i = 0; i < randomy.length; i++) {
            if (randomy[i].random === Math.min(...arandom)) {
              randomize[0] = randomy[i];
            } else if (randomy[i].random === Math.max(...arandom)) {
              randomize[this.arr.length - 1] = randomy[i];
            } else {
              continue;
            }
          }
        }
        for (let i = 0; i < this.arr.length; i++) {
          if (this.arr[i].id == randomize[0].id) {
            continue;
          } else if (this.arr[i].id === randomize[this.arr.length - 1].id) {
            continue;
          } else {
            randomy1.push(this.arr[i]);
          }
        }
        let arandomy = [];
        for (let i = 0; i < this.arr.length; i++) {
          if (
            randomize[0].id === this.arr[i].id ||
            randomize[this.arr.length - 1].id === this.arr[i].id
          ) {
            continue;
          } else {
            arandomy.unshift(this.arr[i].random);
          }
        }
        arandomy.sort();
        for (let k = 0; k <= randomy1.length - 1; k++) {
          for (let i = 0; i <= randomy1.length - 1; i++) {
            if (randomy1[i].random === arandomy[k]) {
              randomize[k + 1] = randomy1[i];
            } else {
              continue;
            }
          }
        }
        for (let i = 0; i < this.arr.length; i++) {
          if (
            this.arr[i].id == randomize[0].id ||
            this.arr[i].id == randomize[this.arr.length - 1].id
          ) {
            this.members[i].fl += 1;
          } else {
            continue;
          }
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
        div.className = "result1";
        result.appendChild(div);
        if (i == 0) {
          div.innerHTML =
            randomize[i].name +
            " " +
            this.hour1[i] +
            ":" +
            this.minute1[i] +
            " - " + this.start 
        } else if (i == this.arr.length - 1) {
          div.innerHTML =
            randomize[i].name +
            " " +
            this.end +  " - " +
            this.hour1[i - 1] +
            ":" +
            this.minute1[i - 1]
        } else {
          div.innerHTML =
            randomize[i].name +
            " " +
            this.hour1[i] +
            ":" +
            this.minute1[i] +
            " - " +
            this.hour1[i - 1] +
            ":" +
            this.minute1[i - 1];
        }
      }
        let run = document.createElement("DIV");
        this.run += 1;
        run.innerHTML = "סבב: " + this.run;
        result.appendChild(run);
        this.system = "רנדומליות הוגנת";
        for (let i = 0; i < randomize.length; i++) {
          randomize[i].index = i;
        }
        let idid = [];
        for (let i = 0; i < randomize.length; i++) {
          idid.push(randomize[i].id);
        }
        idid.sort(function(a, b) {
          return a - b;
        });
        console.log(idid);
        let ind = [];
        for (let k = 0; k < randomize.length; k++)
          for (let i = 0; i < randomize.length; i++) {
            if (idid[k] == randomize[i].id) {
              ind.push(randomize[i].index);
            } else {
              continue;
            }
          }
        let fair = 1;
        const payload = {
          index: ind,
          fairrandom: fair
        };
        this.UpdateIndex(payload, this.g);
      }
    },
    UpdateIndex(payload, ID) {
      const path = `http://localhost:5000/group/${ID}`;
      this.$http
        .put(path, payload)
        .then(() => {
          this.GetGroups();
        })
        .catch(error => {
          console.log(error);
          this.GetGroups;
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
<style scoped>
.names {
  margin-left: 42%;
  margin-top: 3.5%;
  font-size: 25px;
}
.username {
  direction: rtl;
}
.NewGroup {
  background-color: #4caf50; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  border-radius: 8px;
  margin-left: 47.5%;
  margin-top: 10%;
  font-family: "Varela Round", sans-serif;
  /*margin-right: 40%;*/
  -webkit-transition-duration: 0.4s; /* Safari */
  transition-duration: 0.4s;
}
.NewGroup:hover {
  background-color: #4e8235;
}
.FNewGroup {
  background-color: #4caf50; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  border-radius: 8px;
  margin-top: 10%;
  font-family: "Varela Round", sans-serif;
  /*margin-right: 40%;*/
  -webkit-transition-duration: 0.4s; /* Safari */
  transition-duration: 0.4s;
}
.FNewGroup:hover {
  background-color: #4e8235;
}
.back {
  margin-left: 42.5%;
  margin-top: 2.5%;
}
.edit {
  margin-left: 3%;
  margin-top: 2.5%;
}
.DeleteGroup {
  margin-top: 1.5%;
  margin-left: 45%;
  margin-bottom: -1%;
  background-color: #ba4545;
}
.DeleteGroup:hover {
  background-color: #bf1515;
}
.button {
  margin-left: 2.5px;
  margin-right: 2.5px;
}
.div {
  display: inline-block;
  margin-left: 0%;
}
.resulted {
  padding-bottom: 0.75%;
  padding-top: 0.75%;
  margin-right: 35%;
  margin-left: 35%;
  margin-bottom: -2.5%;
}
.Mname {
  display: inline-block;
  margin-right: 22%;
  margin-left: -20%;
}
.EditName {
  /*margin-top: 1.5%;*/
  /*margin-left: 70%;
  margin-top:-50%;
  padding: 0px;
  margin-bottom: 50%;*/
  background: none;
  font-size: 35px;
}
.SaveName {
  margin-left: 46%;
  display: block;
  margin-top: 1.5%;
  margin-bottom: 1%;
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
.container {
  direction: rtl;
  text-align: center;
  margin-left: 40%;
  margin-right: 35%;
}
.member {
  margin-bottom: 2.5%;
}
.admatai {
  direstion: rtl;
  display: inline-block;
  margin-right: 7%;
  margin-top: -10%;
  padding-left: 17%;
}
.p {
  direction: rtl;
  color: white;
  font-size: 75px;
}
.buttons {
  display: inline-block;
  direction: rtl;
  text-align: center;
  margin-left: 10%;
  margin-right: 60%;
  margin-top: -3%;
  margin-bottom: 2.5%;
}
.button {
  margin-top: 2.5%;
  margin-left: 2.5%;
}
</style>
