<template>
    <div class="circle_container">

      <div class="circle__name">{{cirlce_name}}</div>

      <div class="card">
            <div class="box">
              <div class="percent">
                <svg>
                  <circle cx="70" cy="70" r="70" :style="`stroke-dashoffset: calc(440 - (440 * ${percent}) / 100);`"></circle>
                  <circle cx="70" cy="70" r="70" :style="`stroke-dashoffset: calc(440 - (440 * ${percent}) / 100);`"></circle>
                </svg>
                <div class="number">
                  {{percent}}% <span>Passed</span>
                </div>
              </div>
            </div>
      </div>
    </div>
</template>

<style scoped lang="scss">

.circle__name{
  font-size: 22px;
  color: white;
  font-weight: bold;
  margin-bottom: 21px;
}

.percent {
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

.percent .number {
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

.percent .number h2 {
  color: #777;
  font-weight: 700;
  font-size: 40px;
  transition: 0.5s;
}

.card:hover .percent .number h2 {
  color: #fff;
  font-size: 60px;
}

.percent .number h2 span {
  font-size: 24px;
  color: #777;
}

.card:hover .percent .number h2 span {
  color: #fff;
  transition: 0.5s;
}

.text {
  position: relative;
  color: #777;
  margin-top: 20px;
  font-weight: 700;
  font-size: 18px;
  letter-spacing: 1px;
  text-transform: uppercase;
  transition: 0.5s;
}

.card:hover .text {
  color: #fff;
}

svg {
  position: relative;
  width: 150px;
  height: 150px;
  z-index: 1000;
}

svg circle {
  width: 100%;
  height: 100%;
  fill: none;
  stroke: #191919;
  stroke-width: 10;
  stroke-linecap: round;
  transform: translate(5px, 5px);
}

svg circle:nth-child(2) {
  stroke-dasharray: 440;
  stroke-dashoffset: 440;
}

.card:nth-child(2) svg circle:nth-child(2) {
  stroke-dashoffset: calc(440 - (440 * 85) / 100);
  stroke: #FFD15C;
}

@media (max-width: 991px) {
  .container {
    width: 100%;
    flex-direction: column;
  }

  .container .card {
    margin: 20px auto;
  }
}
</style>

<script type="text/javascript">
  export default {
    props: ['percent', 'cirlce_name']
  }
</script>
