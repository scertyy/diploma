<template>
  <div class="app" v-if="!loading">
    <Nav v-if="route.name !== 'auth'"></Nav>
    <div class="app__container" :class="{'app__container_full': route.name === 'auth'}">
      <TopNav v-if="route.name !== 'auth'"></TopNav>
      <div class="app__content" :class="{'app__content_full': route.name === 'auth'}">
        <router-view></router-view>
      </div>
    </div>
  </div>

</template>

<script>
  import Nav from './components/Nav'
  import TopNav from './components/TopNav'
  import {useProfile} from "./composition/useProfile";
  import { useRoute } from 'vue-router'
  import {ref} from 'vue'
  export default {
    components: {
      Nav, TopNav
    },
    setup() {
      const route = useRoute()
      const { getProfile } = useProfile()
      const loading = ref(true);
      if (localStorage.getItem('token_access')) {
        getProfile()
          .then(r => {
              console.log(r);
              loading.value = false;
          })
      }
      return {
        route,
        loading
      }
    }
  }
</script>

<style lang="scss">

  ::-webkit-scrollbar {
    width: 8px; /* ширина для вертикального скролла */
    height: 8px; /* высота для горизонтального скролла */
    background-color: #303030;
  }
  ::-webkit-scrollbar-thumb {
    background-color: #FFD15C;
    border-radius: 9em;
    box-shadow: inset 1px 1px 10px #f3faf7;
  }
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
