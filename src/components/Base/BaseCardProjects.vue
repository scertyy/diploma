<template>
  <div class="card__projects">
    <h4 class="card__projects_head">Проекты</h4>

    <div
      class="card__projects__name"
      v-for="project in projects"
      :key="project.name"
    >
      {{project.name}}
    </div>

    <div class="card__projects_add">+</div>
  </div>
</template>

<style lang="scss">
  .card__projects{
    width: 100%;
    height: 70%;
    border-radius: 5px;
    padding: 5px 0;

    .card__projects_head{
      color: rgb(144, 144, 144);
      text-align: left;
      margin-bottom: 10px;
    }

    .card__projects__name{
      text-align: left;
      color: white;
      margin: 5px 10px;
      font-size: 20px;
      font-weight: bold;

      &:hover{
        cursor: pointer;
        color: #FFD15C;
      }

      &:nth-of-type(n + 6){
        display: none;
      }
    }

    .card__projects_add{
      color: #FFD15C;
      font-size: 26px;
      line-height: 120%;
      cursor: pointer;
      display: none;
    }
  }

  .card__projects__modal{
    height: 130px;

    .card__projects_head{
      color: white;
      font-size: 22px;
      text-align: left;
      margin: 10px 0;
    }

    .card__projects__name{
      overflow-y: scroll;
      &:nth-of-type(n + 6){
        display: block;
      }
    }

    .card__projects_add{
      display: block;
      margin-left: 10px;
    }
  }
</style>

<script type="text/javascript">
  export default{
    props: ['projects']
  }
</script>
