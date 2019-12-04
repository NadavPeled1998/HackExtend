const express = require("express");
const cors = require("cors");
//const bodyParser = require('body-parser');

const app = express();

app.use(cors());

const Groups = [
  {
    group: "f",
    id: 1,
    run: 1,
    names: [
      { name: "yehuda", id: 1, fl: 0 },
      { name: "michal", id: 2, fl: 1 },
      { name: "ido", id: 3, fl: 0 },
      { name: "hadas", id: 4, fl: 0 },
      { name: "nadav", id: 5, fl: 1 },
      { name: "uri", id: 6, fl: 0 }
    ]
  },
  {
    group: "friends",
    id: 2,
    run: 1,
    names: [
      { name: "Gilad", id: 1, fl: 0 },
      { name: "Alon", id: 2, fl: 1 },
      { name: "Niv", id: 3, fl: 0 },
      { name: "Ofer", id: 4, fl: 1 },
      { name: "Chuchu", id: 5, fl: 0 }
    ]
  }
];
app.get("/", (req, res) => {
  res.send(Groups);
});
app.post("/", (req, res) => {
  res.send(Groups);
});
app.delete("/:id", (req, res) => {
  res.send(Groups);
});

app.listen(3500);
