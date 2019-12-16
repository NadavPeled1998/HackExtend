<template>
  <div>
    <button @click="$emit('show-team', id)">{{ group }}</button>
  </div>
</template>
<script>
export default {
  props: ["group", "id"]
};
</script>
<style scoped>
div {
  display: inline-block;
}
button {
  background-color: #fafafa; /*#4e8235;#c29929;  Green */
  float: center;
  border: none;
  color: #4e8235;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  border-radius: 8px;
  margin-left: 22.5px;
  margin-bottom: 10%;

  -webkit-transition-duration: 0.4s; /* Safari */
  transition-duration: 0.4s;
}
button:hover {
  background-color: #f0f0f0;
}
</style>
