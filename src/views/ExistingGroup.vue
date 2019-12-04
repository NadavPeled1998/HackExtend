<template>
  <div>
<<<<<<< HEAD:src/views/ExistingGroup.vue
    <div class="topnav">
      <router-link to="/">בית</router-link>
      <router-link to="/newgroup"> צור קבוצה</router-link>
      <router-link to="/existing" class="active">קבוצות קיימות</router-link>
      <router-link to="/contact">צור קשר</router-link>
      <router-link to="/about">מי אנחנו</router-link>
      <router-link to="/" class="logo"
        ><img src="/images\logosh.png" height="18px"
      /></router-link>
    </div>
    <div v-if="!n">
      <div v-if="ex" class="loya">
        <p>אין קבוצות קיימות למשתמש זה</p>
=======
  <div class="topnav">
  <router-link to="/">בית</router-link>
  <router-link to="/newteam"> צור קבוצה</router-link>
  <router-link to="/exist" class="active" >קבוצות קיימות</router-link>
  <router-link to="/contact">צור קשר</router-link>
  <router-link to="/mi" >מי אנחנו</router-link>
  <router-link to="/" class="logo"><img src="/images\logosh.png" height=18px></router-link>
  </div>
    <div v-if="!n">
      <div v-if="ex" class="loya">
        <p>לא יצרת קבוצה עדיין</p>
>>>>>>> b768921fa4cc6f34c95c093d4276eab8d248e7ee:src/views/OldTeam.vue
      </div>
      <div v-if="!ex">
        <h5 class="loya">בחר קבוצה</h5>
        <steam
          @show-team="showTeam"
          v-for="team in teams"
          :key="team.id"
          :id="team.id"
          :group="team.group"
        >
        </steam>
      </div>
<<<<<<< HEAD:src/views/ExistingGroup.vue
      <router-link to="/newgroup" class="button4">צור קבוצה חדשה</router-link>
=======
      <router-link to="/newteam" class="button4">צור קבוצה חדשה</router-link>
>>>>>>> b768921fa4cc6f34c95c093d4276eab8d248e7ee:src/views/OldTeam.vue
    </div>
    <div v-if="n && !edi && !results">
      <button @click="back" class="button1">חזור</button>
      <button @click="Edit" class="button2">ערוך</button><br />
      <button @click="DeleteGroup" class="button1">מחק קבוצה</button>
      <div>
        <div class="memebersh">
          <h5>{{ g.group }}</h5>
        </div>
      </div>
      <div class="members">
        <div v-for="member in members" :key="member.id">
          {{ member.name }}
        </div>
      </div>
      <div class="admatai">
        <span><img src="/images\admatai.png" height="150px" class="ask"/></span>
        <div class="timepart" :class="{ error: s || e }">
          <input type="time" class="time" />
          <input type="time" class="time" />
        </div>
        <br />
      </div>
      <div class="buttons5">
        <button @click="Allrandom" class="button5">רשימה רנדומלית</button>
        <button @click="FairRandom" class="button5">רנדומליות הוגנת</button>
        <button @click="NoChange" class="button5">אותו הסדר</button>
        <button @click="KeepForward" class="button5">
          אותו הסדר, אחד קדימה
        </button>
      </div>
    </div>
    <div v-if="edi">
      <button @click="Save" class="button1">חזור</button>
      <button @click="Add" v-if="edi" class="button2">הוסף</button><br />
      <div class="inp" v-for="member in members" :key="member.id">
        <div v-show="member.id" class="result">{{ member.name }}</div>
        <input
          v-if="!member.id"
          type="text"
          class="names"
          :class="{ error: !k }"
          :value="member.name"
        />
        <less @less="less" :id="member.id"> </less>
<<<<<<< HEAD:src/views/ExistingGroup.vue
        <button v-show="member.id" class="button4" @click="EditName(member.id)">
          ערוך שם
        </button>
        <button
          v-show="!member.id"
          class="button4"
          @click="EditedName(member.id)"
        >
=======
        <button v-show="member.id" @click="EditName(member.id)">
          ערוך שם
        </button>
        <button v-show="!member.id" @click="EditedName(member.id)">
>>>>>>> b768921fa4cc6f34c95c093d4276eab8d248e7ee:src/views/OldTeam.vue
          שמור שם
        </button>
      </div>
      <div v-if="!k">אל תשאירו שדות ריקים</div>
<<<<<<< HEAD:src/views/ExistingGroup.vue
=======
      <button @click="Add" v-if="edi">הוסף</button>
      <div><button @click="Save">שמור</button></div>
>>>>>>> b768921fa4cc6f34c95c093d4276eab8d248e7ee:src/views/OldTeam.vue
    </div>
    <div class="result" v-show="results">
      <div>{{ system }}</div>
    </div>
  </div>
</template>
<script>
import steam from "@/components/team.vue";
import less from "@/components/less.vue";
<<<<<<< HEAD:src/views/ExistingGroup.vue
=======
//import { URL } from "@/services/config.js";
>>>>>>> b768921fa4cc6f34c95c093d4276eab8d248e7ee:src/views/OldTeam.vue

export default {
  name: "Exist",
  components: {
    steam,
    less
  },
  data() {
    return {
      Groups: [],
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
  mounted() {
<<<<<<< HEAD:src/views/ExistingGroup.vue
    const path = `http://localhost:5000/groups`;
    this.$http.get(path).then(res => {
      this.Groups = res.data.groups;
=======
    //const path  =  `http://localhost:5000/groups`
    this.$http.get(URL).then((res) =>{
      this.Groups = res.data;
      console.log(res)
      console.log(this.Groups)
>>>>>>> b768921fa4cc6f34c95c093d4276eab8d248e7ee:src/views/OldTeam.vue
      this.teams = this.Groups;
      this.ex = false;
      if (this.Groups.length < 1) {
        this.ex = true;
      }
    });
  },
  methods: {
<<<<<<< HEAD:src/views/ExistingGroup.vue
    GetGroups() {
      const path = `http://localhost:5000/groups`;
      this.$http
        .get(path)
        .then(res => {
          this.Groups = res.data.groups;
          console.log(this.Groups);
        })
        .catch(error => {
          console.log(error);
        });
    },
    GetMembers(id) {
      const path = `http://localhost:5000/group/${id}`;
      this.$http.get(path).then(res => {
        this.members = res.data.Member;
      });
=======
    GetGroups(){
      //const path = `http://localhost:5000/groups`
      this.$http.get(URL).then((res) => {
        this.Groups = res.data
        console.log(res.data)
        console.log(this.Groups)
      })
      .catch((error) => {
        console.log(error)
      })
>>>>>>> b768921fa4cc6f34c95c093d4276eab8d248e7ee:src/views/OldTeam.vue
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
        this.n = false;
        const path = `http://localhost:5000/groups`;
        this.$http.get(path).then(res => {
          this.Groups = res.data.groups;
          this.teams = this.Groups;
          this.ex = false;
          if (this.Groups.length < 1) {
            this.ex = true;
          }
        });
      }
    },
    DG(id) {
      const path = `http://localhost:5000/group/${id}`;
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
      this.start = Time[0].value;
      this.end = Time[1].value;
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
<<<<<<< HEAD:src/views/ExistingGroup.vue
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
=======
      let run = document.createElement("DIV")
        this.g.run += 1
        run.innerHTML= "run: " + this.g.run
        result.appendChild(run)
        this.system = "random";
>>>>>>> b768921fa4cc6f34c95c093d4276eab8d248e7ee:src/views/OldTeam.vue
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
<<<<<<< HEAD:src/views/ExistingGroup.vue
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
=======
        }let run = document.createElement("DIV")
        this.g.run += 1
        run.innerHTML= "run: " + this.g.run;
        this.system = "No Change";
        result.appendChild(run)
>>>>>>> b768921fa4cc6f34c95c093d4276eab8d248e7ee:src/views/OldTeam.vue
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
<<<<<<< HEAD:src/views/ExistingGroup.vue
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
=======
        }let run = document.createElement("DIV")
        this.g.run += 1
        run.innerHTML= "run: " + this.g.run
        result.appendChild(run)
        this.system = "Kepp forward";
>>>>>>> b768921fa4cc6f34c95c093d4276eab8d248e7ee:src/views/OldTeam.vue
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
    }
  }
};
</script>
<style scoped>
.names {
  margin-left: 42.5%;
  margin-top: 9.5%;
}
.username {
  direction: rtl;
}
</style>
