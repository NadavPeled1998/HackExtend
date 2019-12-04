<template>
  <div>
    <button @click="$emit('less', id)">-</button>
  </div>
</template>
<script>
export default {
  props: ["id"]
};
</script>
<style scoped>
button {
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
  margin-right: 40%;

  -webkit-transition-duration: 0.4s; /* Safari */
  transition-duration: 0.4s;
}
button:hover {
  background-color: #4e8235;
  color: white;
}
</style>
