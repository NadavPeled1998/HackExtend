<template>
  <div>
    <div class="button" @click="$emit('less', id)">
      <i class="el-icon-delete"></i>
    </div>
  </div>
</template>
<script>
export default {
  props: ["id"]
};
</script>
<style scoped>
div {
  margin-top: -2.5%;
  display: inline-block;
  margin-right: 50%;
}
.button {
  text-align: center;
  display: inline-block;
  cursor: pointer;
  /*margin-right: 70%;*/
  /*margin-bottom: 10%;*/
  font-size: 35px;
  -webkit-transition-duration: 0.4s; /* Safari */
  transition-duration: 0.4s;
}
button:hover {
}
</style>
