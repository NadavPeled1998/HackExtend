<template>
  <div class="product">
    <button @click="$emit('show-team', id)">{{ group }}</button>
  </div>
</template>
<script>
export default {
  props: ["group", "id"]
};
</script>
