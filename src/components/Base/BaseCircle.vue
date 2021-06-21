<template>
    <div class="base-circle">

      <div class="base-circle__name">{{cirlce_name}}</div>

      <div class="base-circle__card">
            <div class="base-circle__box">
              <div class="base-circle__percent">
                <svg class="base-circle__circle">
                  <circle cx="70" cy="70" r="70" :style="`stroke-dashoffset: calc(440 - (440 * ${percent}) / 100);`"></circle>
                  <circle cx="70" cy="70" r="70" :style="`stroke-dashoffset: calc(440 - (440 * ${percent}) / 100);`"></circle>
                </svg>
                <div class="base-circle__number">
                  {{percent}}% <span>Выполнено</span>
                </div>
              </div>
            </div>
      </div>
    </div>
</template>

<script>
    export default {
        props: ['percent', 'cirlce_name']
    }
</script>

<style lang="scss">

.base-circle__name{
  font-size: 22px;
  color: white;
  font-weight: bold;
  margin-bottom: 21px;
}

.base-circle__percent {
  color: #F1F1F1;
  font-weight: bold;
  position: relative;
  font-size: 18px;
  width: 150px;
  height: 150px;
  border-radius: 50%;
  box-shadow: inset 0 0 50px #000;
  background: #222;
  z-index: 1000;

  span{
    color: #A7A7A7
  }
}

.base-circle__percent .base-circle__number {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 50%;
  display: flex;
  flex-direction: column;
  line-height: 120%;
}

.base-circle__percent .base-circle__number h2 {
  color: #777;
  font-weight: 700;
  font-size: 40px;
  transition: 0.5s;
}

.base-circle__card:hover .base-circle__percent .base-circle__number h2 {
  color: #fff;
  font-size: 60px;
}

.base-circle__percent .base-circle__number h2 span {
  font-size: 24px;
  color: #777;
}

.base-circle__card:hover .base-circle__percent .base-circle__number h2 span {
  color: #fff;
  transition: 0.5s;
}

.base-circle__circle {
  position: relative;
  width: 150px;
  height: 150px;
  z-index: 1000;
}

.base-circle__circle circle {
  width: 100%;
  height: 100%;
  fill: none;
  stroke: #191919;
  stroke-width: 10;
  stroke-linecap: round;
  transform: translate(5px, 5px);
}

.base-circle__circle circle:nth-child(2) {
  stroke-dasharray: 440;
  stroke-dashoffset: 440;
}

.base-circle__card:nth-child(2) .base-circle__circle circle:nth-child(2) {
  stroke-dashoffset: calc(440 - (440 * 85) / 100);
  stroke: #FFD15C;
}

@media (max-width: 991px) {
  .container {
    width: 100%;
    flex-direction: column;
  }

  .container .base-circle__card {
    margin: 20px auto;
  }
}
</style>


