<template>
  <div class="home">
    <div v-if="Next">
      <p>how many friends do you have in your team?</p>
      <input type="number" class="input" min="2" v-model="val" @input="numbers" /> <br />
      <div v-if="negative">you must have atleast two people to be a group</div>
      <button @click="numbers">Let's Go</button>
    </div>
    <div v-if="Next">
      <p>what's your names?</p>
      <button @click="add">+</button>
      <button @click="less">-</button>
    </div>
    <div class="names" v-show="Next"></div>
    <div v-if="k">all inputs must have names</div>
    <div v-show="Next">
      <p>which hours?</p>
      <span>Start</span><input type="time" class="time" /> <span>End</span
      ><input type="time" class="time" /><br />
      <div v-if="s">When do you start?</div>
      <div v-if="e">when do you end?</div>
      <button @click="Allrandom">Let's random</button>
      <button @click="noChange">don't change the order</button>
    </div>
    <div v-show="results">
      <div class="result"></div>
      <button @click ="save" v-if="!saved">Save as</button>
      <button v-if="saved">Saved</button>
      <router-link to="/">don't save</router-link>
      
    </div>
  </div>
</template>

<script>
<<<<<<< HEAD
//import { URL } from "@/services/config.js"
=======
>>>>>>> 5757c839563172912e31ee7a760f35f76c046af6

export default {
  name: "home",
  data() {
    return {
      Groups: [],
      Group : {
        title: "",
        run: 1,
      },
      name: [],
      fl: [],
      index: [],
      Next: true,
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
      id: "",
      run: 1,
      names: [],     
    };
  },
  mounted(){
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
      let input = document.querySelector(".input");
      if (input.value > 1) {
        this.negative = false;
        //this.Next = true;
        let names = document.querySelector(".names");
        console.log(names);
        let inputs = document.querySelectorAll(".name");
        if(inputs.length>1){
        for(let i = 0; i<this.oval; i++){
            let names = document.querySelector(".names");
            let input = document.querySelector(".name");
            names.removeChild(input);
        }
        }
        this.oval = this.val
        for (let i = 0; i < input.value; i++) {
          let div = document.createElement("DIV");
          let x = document.createElement("INPUT");
          x.className = "name";
          x.setAttribute("type", "text");
          names.appendChild(div);
          names.appendChild(x);
        }
      } else {
        this.negative = true;
      }
    },
    add() {
      let names = document.querySelector(".names");
      let div = document.createElement("DIV");
      let x = document.createElement("INPUT");
      x.className = "name";
      x.setAttribute("type", "text");
      names.appendChild(div);
      names.appendChild(x);
    },
    less() {
      let inputs = document.querySelectorAll(".name");
      if (inputs.length > 2) {
        let names = document.querySelector(".names");
        let input = document.querySelector(".name");
        names.removeChild(input);
      }
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
        this.start = Time[0].value;
        this.end = Time[1].value;
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
          randomize[0].fl = 1
          randomize[randomize.length-1].fl = 1
          this.arr = randomize
          for(let i = 0; i<this.arr.length; i++){
          this.arr[i].index = i
        }
        console.log(this.arr[3].index)
          console.log(randomize)
      let run = document.createElement("DIV")
        run.innerHTML= "run: " + 1
        result.appendChild(run) 
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
        for(let i = 0; i<this.arr.length; i++){
          this.arr[i].index = i
        }
        console.log(this.arr[3].index)
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
        this.arr[this.arr.length-1].fl = 1
        let run = document.createElement("DIV")
        run.innerHTML= "run: " + 1
        result.appendChild(run) 
      }
    },
    GetGroups(){
      const path = `http://localhost:5000/groups`
      this.$http.get(path).then((res) => {
        this.Groups = res.data.groups;
<<<<<<< HEAD
        console.log(this.Groups)
=======
>>>>>>> 5757c839563172912e31ee7a760f35f76c046af6
      })
      .catch((e) => {
        console.log(e);
      })
    },
    AddGroups(payload){
      const path = `http://localhost:5000/groups`
      this.$http.post(path, payload).then(() =>{
        this.GetGroups();
      })
      .catch((error) => {
        console.log(error);
        this.GetGroups();
      });
    },
      save(){
        this.GetGroups();
        let group = prompt("איך לקרוא לקבוצה?")
        this.Group.title = group;
        this.Group.run = 1;
        for(let i = 0;i<this.arr.length; i++){
          this.name.push(this.arr[i].name)
          this.fl.push(this.arr[i].fl)
          this.index.push(this.arr[i].index)
        };
        const payload = {
          title: this.Group.title,
          run: this.Group.run,
          name: this.name,
          fl: this.fl,
          index: this.index
        }
        console.log(payload)
        this.AddGroups(payload)
        this.saved = true;
      }
  }
};
</script>
