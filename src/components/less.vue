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
