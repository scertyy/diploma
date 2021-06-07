<template>
  <div class="app">
    <Nav  v-if="route.name !== 'auth'"></Nav>
    <div class="app__container" :class="{'app__container_full': route.name === 'auth'}">
      <TopNav v-if="route.name !== 'auth'"></TopNav>
      <div class="app__content" :class="{'app__content_full': route.name === 'auth'}">
        <router-view></router-view>
      </div>
    </div>
  </div>

</template>

<script>
  import { useRoute } from 'vue-router'

  import Nav from './components/Nav'
  import TopNav from './components/TopNav'
  export default {
    components: {
      Nav, TopNav
    },
    setup() {
      const route = useRoute()
      return {
        route,
      }
    }
  }
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.app {
  width: 100vw;
  height: 100vh;
  position: relative;
  background: #252525;
  overflow: hidden;

  display: flex;
}
.app__container {
  height: 100%;
  width: calc(100% - 120px);
  &.app__container_full {
    width: 100%;
  }
}
.app__content {
  height: calc(100% - 90px);
  width: 100%;
  &.app__content_full {
    height: 100%;
  }
}
body {
  margin: 0;
  padding: 0;
}


input, textarea, button {
  -webkit-appearance: none;
  -webkit-box-shadow: none;
  -moz-appearance: none;
  -moz-box-shadow: none;
  box-shadow: none;
  outline: none;
  resize: none;
  border: none;
}
  * {
    box-sizing: border-box!important;
  }
</style>
