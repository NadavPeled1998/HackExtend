<template>
  <div>
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
    <div class="buttons">
      <button class="button">רשימה רנדומלית</button>
      <button class="button">רשימה לפי הסדר</button>
    </div>
    <div v-if="Next" class="Ma">
      <p class="ma">מה השמות שלכם?</p>
      <div class="names" v-show="Next" :class="{ error: k }"></div>
    </div>
  </div>
</template>
<script>
export default {
  name: "numbers",
  data() {
    return {
      oval: 2,
      num: 2,
      Next: true
    };
  },
  mounted() {
    let names = document.querySelector(".names");
    for (let i = 0; i < 2; i++) {
      let div = document.createElement("DIV");
      let x = document.createElement("INPUT");
      div.className = "right";
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
          div.className = "right";
          x.className = "name";
          x.setAttribute("type", "text");
          names.appendChild(div);
          names.appendChild(x);
        }
        this.oval = this.num;
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
        let input = document.querySelectorAll(".name");
        names.removeChild(input[input.length - 1]);
      }
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
  margin-top: -3%;
}
.ma {
  margin-top: 8%;
  margin-right: 60%;
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
}
.buttons {
  display: block;
  /*padding-left:300px;
  padding-right: 300px;*/
  direction: rtl;
  float: right;
  margin-right: 50.5%;
  margin-top: 3%;
}
</style>
