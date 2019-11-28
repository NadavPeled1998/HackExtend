<template>
  <div>
    <div v-if="!n">
      <div v-if="ex">
        <p>you havent made any group yet</p>
      </div>
      <div v-if="!ex">
        <h2>Choose Group</h2>
        <steam
          @show-team="showTeam"
          v-for="team in teams"
          :key="team.id"
          :id="team.id"
          :group="team.group"
        >
        </steam>
      </div>
      <router-link to="/newteam">Create a New Team</router-link>
    </div>
    <div v-if="n && !edi && !results">
      <button @click="back">come back</button>
      <button @click="Edit">Edit</button>
      <div>
        <h4>{{ g.group }}</h4>
      </div>
      <div v-for="member in members" :key="member.id">{{ member.name }}</div>
      <span>Start</span><input type="time" class="time" /> <span>End</span
      ><input type="time" class="time" /><br />
      <div v-if="s">When do you start?</div>
      <div v-if="e">when do you end?</div>
      <button @click="Allrandom">pure random</button>
      <button @click="FairRandom">fair random</button>
      <button @click="NoChange">don't change the order</button>
      <button @click="KeepForward">move evreybody step forward</button>
    </div>
    <div v-if="edi">
      <div class="inp" v-for="member in members" :key="member.id">
        <div v-show="member.id">{{ member.name }}</div>
        <input
          v-if="!member.id"
          type="text"
          class="name"
          :value="member.name"
        />
        <less @less="less" :id="member.id"> </less>
        <button v-show="member.id" @click="EditName(member.id)">
          edit name
        </button>
        <button v-show="!member.id" @click="EditedName(member.id)">
          save name
        </button>
      </div>
      <div v-if="!k">all inputs must have values</div>
      <button @click="Add" v-if="edi">Add</button>
      <div><button @click="Save">Save</button></div>
    </div>
    <div class="result" v-show="results">
    <div>{{system}}</div>
    </div>
  </div>
</template>
<script>
import steam from "@/components/team.vue";
import less from "@/components/less.vue";
import { URL } from "@/services/config.js";

export default {
  name: "Exist",
  components: {
    steam,
    less
  },
  data() {
    return {
      Groups: [],
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
      g: {},
      edi: false,
      edited: false,
      results: false,
      l: [],
      z: 0,
      k: true,
      beid: 0,
      ed: true,
      newname: "",
      system: ""
    };
  },
  mounted() {
    //const path  =  `http://localhost:5000/groups`
    this.$http.get(URL).then((res) =>{
      this.Groups = res.data;
      console.log(res)
      console.log(this.Groups)
      this.teams = this.Groups;
      this.ex = false
      if(this.Groups.length<1){
        this.ex = true
      }
    })
  },
  methods: {
    GetGroups(){
      //const path = `http://localhost:5000/groups`
      this.$http.get(URL).then((res) => {
        this.Groups = res.data
        console.log(this.Groups)
      })
      .catch((error) => {
        console.log(error)
      })
    },
    showTeam(id) {
      const team = this.teams.find(team => team.id == id);
      this.g = team;
      this.members = team.names;
      this.n = true;
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
        console.log(id);
        const member = this.members.find(member => member.id == id);
        console.log(member);
        for (let i = 0; i < 1; i++) {
          this.beid = member.id;
        }
        member.id = false;
        this.ed = false;
        console.log(this.beid);
        console.log(member.id);
      }
    },
    EditedName(id) {
      console.log(id)
      let input = document.querySelector(".name");
      let member;
      if (input.value) {
        if (id === false) {
          console.log(input.value);
          console.log(id);
          let member = this.members.find(member => member.id == id);
          member.id = this.beid;
          console.log(member.id);
          member.name = input.value;
        } else {
          let ida = [];
          for (let i = 0; i < this.members.length - 1; i++) {
            ida.push(this.members[i].id);
          }
          let fll = [];
          for (let i = 0; i < this.members.length - 1; i++) {
            fll.push(this.members[i].fl);
          }
          this.members[this.members.length - 1].id = Math.max(...ida) + 1;
          this.members[this.members.length - 1].fl = Math.min(...fll);
          let idid = this.members[this.members.length - 1].id;
          console.log(idid);
          console.log(this.members[this.members.length - 1]);
          const member = this.members.find(member => member.id == idid);
          console.log(member.id);
          console.log(ida);
          console.log(this.members);
          this.members[this.members.length - 1].name = input.value;
          this.members.push({});
          this.members.pop();
          //this.$http.put(URL/$this.g.id, )
          //document.querySelectorAll(less)
        }
        const payload = {
          name: member.name,
          fl: member.fl
        }
        this.ed = true;
        this.UpdateName(payload, member.id)
      }
    },
    UpdateName(payload, ID){
      const path = `http://localhost:5000/${ID}/member`
      this.$http.put(path, payload).then(() => {
        this.GetGroups();
      })
      .catch((error) => {
        console.log(error);
        this.GetGroups
      })
    },
    Add() {
      this.members.push({});
      //const path = `http://localhost:5000/group/{}`
      //this.$http.post(path, payload)
    },

    less(id) {
      console.log(id);
      const member = this.members.find(member => member.id == id);
      console.log(member.id);
      for (let i = 0; i < this.members.length; i++) {
        if (this.members[i].id === id) {
          this.members.splice(i, 1);
        }
      }
      console.log(this.members);
      let inps = document.querySelectorAll(".inp");
      console.log(inps);
      let inp;
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
        console.log(this.l);
        console.log(inp);
        inp.parentNode.removeChild(inp);
        const path = `http://localhost:5000/group/${id}/member`;
        this.$http.delete(path).then(() => {
          this.GetGroups();
        })
        .catch((error) => {
          console.log(error);
          this.GetGroups();
        })
      }//i did it very different then what is on the website
    },
    Save() {
      if (this.k) {
        this.edi = false;
      }
    },
    MakeArray() {
      console.log(this.members[0].name);
      for (let i = 0; i < this.members.length; i++) {
        this.arr[i] = {};
        this.arr[i].name = this.members[i].name;
        this.arr[i].id = this.members[i].id;
        this.arr[i].fl = this.members[i].fl;
      }
      console.log(this.arr);
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
      let run = document.createElement("DIV")
        this.g.run += 1
        run.innerHTML= "run: " + this.g.run
        result.appendChild(run) 
        this.system = "random";
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
        console.log(this.arr);
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
        }let run = document.createElement("DIV")
        this.g.run += 1
        run.innerHTML= "run: " + this.g.run;
        this.system = "No Change";
        result.appendChild(run) 
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
        }let run = document.createElement("DIV")
        this.g.run += 1
        run.innerHTML= "run: " + this.g.run
        result.appendChild(run) 
        this.system = "Kepp forward";
      }
    },
    FairRandom() {
      console.log("hello");
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
        }let run = document.createElement("DIV")
        this.g.run += 1
        run.innerHTML= "run: " + this.g.run
        result.appendChild(run)
         this.system = "Fair random";
      }
    }
  }
};
</script>
