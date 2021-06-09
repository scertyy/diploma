<template>
    <div class="base-circle-icon"
        :style="{
            'background': `url(${src}) center center / cover no-repeat`
        }"
    ></div>
</template>

<script>
    import {computed} from 'vue';
    export default {
        props: {
            src: String,
        },
        setup(props) {

            return {
                src: computed(() => props.src),
            }
        }
    }
</script>


<style lang="scss">
    .base-circle-icon {
        width: 58px;
        height: 58px;
        border-radius: 16px 8px;
        background: white;

        flex-shrink: 0;
    }
</style>